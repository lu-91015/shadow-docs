---
layout: doc
title: "构建指南"
summary: "从源码构建 shadow：bootstrap 链、构建工具、缓存隔离与并行测试。"
permalink: /building/
prev: /lsp/
next: /api/
---

本文面向**开发者**，说明如何从源码构建 shadow 编译器、跑通自举固定点，以及运行测试套件。普通用户请看[快速开始](/getting-started/)与[工具链](/toolchain/)。

## 环境要求

- **LLVM 工具链**（clang+llvm-22.1.0-x86_64-pc-windows-msvc 或等价版本），需设置环境变量 `LLVM_HOME` 指向其根目录。
- **冻结的引导编译器** `build/shadow.exe`：上一轮自举产物，用于编译本轮的构建工具（解决“鸡生蛋”）。

```bash
export LLVM_HOME="D:/llvm/clang+llvm-22.1.0-x86_64-pc-windows-msvc"
```

## 构建工具（shadow 原生）

三个构建工具均用 shadow 自身编写，由冻结的 `build/shadow.exe` 编译为原生 exe：

| 源文件 | 构建产物 | 作用 |
|--------|----------|------|
| `tools/build_shadow.shadow` | `build/build_shadow.exe` | 7 阶段自举，产出 `build/shadow.exe` |
| `tools/build_resident.shadow` | `build/build_resident.exe` | 驻留部署：stage2→3→4 固定点比对后部署 |
| `tools/build_run_tests.shadow` | `build/run_tests.exe` | 测试运行器（源 `test/run_tests.shadow`） |

> 它们本身也是 shadow 程序，因此必须先有 `build/shadow.exe` 才能编译它们——这正是用“上一轮编译器编出本轮工具”的标准解法。

## 自举流程

### 1) `build/build_shadow.exe`：7 阶段接力

```bash
build/build_shadow.exe
```

内部 7 个阶段（均为仓库根执行、使用相对路径）：

1. **precompile**：编译 `rt/rt_zip.c`、`rt/shadow_gc_supplement.c`、`rt/shadow_index.c`、`rt/rt_proc_spawn.c` 等运行时对象。
2. **patch runtime**：用 `llvm-objcopy` 把 `shadow_sys_exec` 重定义为 `shadow_sys_exec_blob`，并链接 `bootstrap/sys_exec_cpa.c`（使 `rt_sys_exec` 走原生 `CreateProcessA`）。
3. **stage1**：冻结的 `build/shadow.exe`（HOST）编译 `src/main.shadow` → `stage1.ll` → `shadow-stage1.exe`。
4. **stage2**：`shadow-stage1.exe` 编译 `src/main.shadow` → `stage2.ll` → `shadow-stage2.exe`。
5. **stage3**：`shadow-stage2.exe` 编译 `src/main.shadow` → `stage3.ll`。
6. **verify fixed-point**：字节比对 `stage2.ll == stage3.ll`，一致则打印 `FIXEDPOINT_OK stage2==stage3`。
7. **deploy + smoke**：`shadow-stage2.exe` 复制为 `build/shadow.exe`，编译全部 `rt/*.c`，最后 `build/shadow.exe --version` 冒烟。

### 2) `build/build_resident.exe`：驻留部署（可选）

`build_resident` 假设 `build/r_stage2.ll` 已由现有 `build/shadow.exe` 编出（即先跑一次 `build/shadow.exe src/main.shadow -o build/r_stage2.ll`），随后：

```
r_stage2.ll → llc + clang++ → r.exe
r.exe 编译 src → r_stage3.ll      ; 比对 stage2 == stage3
r.exe 编译 src → r_stage4.ll      ; 比对 stage3 == stage4（复用 .lu 缓存）
r.exe 部署为 build/shadow.exe
```

两处 `FIXEDPOINT_OK` 即证明本轮自举稳定，可部署。

## 缓存隔离

shadow 使用 `.lu` 增量缓存加速编译，基目录默认 `build/lu_cache`，可被环境变量 `SHADOW_LU_CACHE_DIR` 覆盖：

```bash
export SHADOW_LU_CACHE_DIR=build/lu_cache_manual   # 改用独立缓存目录
```

并行测试时，运行器 `rt/rt_test_par.c` 会为**每个子进程**注入独立的 `SHADOW_LU_CACHE_DIR=build/lu_cache_s&lt;slot&gt;`，避免多 `shadow.exe` 并发写同一缓存目录的竞态。

## 运行测试

```bash
# 串行
build/run_tests.exe

# 并行（推荐 -j 8）
build/run_tests.exe -j 8
# 或 build/run_tests.exe --jobs 8
```

- 用例位于 `test/cases/`，按 `tc` / `codegen` / `exe` / `check` 等模式分组。
- 每用例首部用 `//@desc` / `//@expect` / `//@mode` / `//@skip` / `//@xfail` 指令描述。
- 全量并行回归（`-j 8`）结果：`PASS=925 / FAIL=0 / SKIP=30 / TOTAL=955`。

## 从零冷启动

若没有可用的 `build/shadow.exe`，可用外部引导器冷启动（`BUILD_HOST` 指向任意能编译 `src/main.shadow` 的 shadow 编译器）：

```bash
set BUILD_HOST=other/shadow.exe
build/build_shadow.exe
```

## 下一步

- 返回[工具链](/toolchain/)查看编译器命令与项目结构。
- 阅读[关于 shadow](/about/)了解项目路线图。
