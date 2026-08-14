---
layout: doc
title: "工具链"
summary: "编译器、LLVM IR 生成、自举构建与测试运行流程。"
permalink: /toolchain/
prev: /api/
next: /lsp/
---

shadow 的工具链围绕 **LLVM** 构建：编译器将 `.shadow` 源码翻译为 LLVM IR（`.ll`），再由 LLVM 工具链编译为原生可执行文件。

## 编译流程

```
.shadow 源码
     │  shadow（shadow 编译器）
     ▼
.ll（LLVM IR，人类可读）
     │  llc + clang++ 链接（--run 一键完成）
     ▼
可执行文件
```

### 为什么保留 .ll 中间产物

- **可调试**：`.ll` 是文本格式，可直接阅读检查代码生成是否正确。
- **可优化**：可用 `opt` 对 IR 跑额外优化 pass。
- **测试要求**：测试规范要求每个用例生成 `.ll` 并成功编译运行，仅生成 `.ll` 不算完成。

## 编译器命令

### 基本编译

```bash
shadow hello.shadow -o hello.ll
```

- 输入：一个 `.shadow` 主文件（`import` 的依赖模块自动递归加载）。
- 输出：`.ll` LLVM IR 文件。

```bash
shadow hello.shadow --run   # 编译 + 链接 + 运行（一步到位）
```

### 多模块编译

`import` 依赖由编译器自动递归加载，只需指定主文件：

```bash
shadow main.shadow -o program.ll
```

### 自举

shadow 编译器自身由 shadow 语言实现（shadow-0.5），构建工具链也**完全用 shadow 编写**（`tools/*.shadow`），由冻结的 `build/shadow.exe` 编译为原生可执行文件，规避“鸡生蛋”问题。自举通过多阶段固定点验证：

```bash
# 设置 LLVM 工具链（Windows 示例）
export LLVM_HOME="D:/llvm/clang+llvm-22.1.0-x86_64-pc-windows-msvc"

# 1) 自举构建：7 阶段接力，stage2.ll == stage3.ll 即 fixed-point
#    （由冻结的 build/shadow.exe 编出 build/build_shadow.exe 后运行）
build/build_shadow.exe
#    → 产出 build/shadow.exe（stage1→stage2→stage3 固定点）

# 2) 驻留自举（部署路径）：在 build/build_shadow.exe 基础上
#    再做 stage2→stage3→stage4 三重固定点比对后部署
build/build_resident.exe
```

<div class="callout note">
  <p class="callout-title">自举的意义</p>
  <p>“自举”指用 shadow 语言本身实现 shadow 编译器，并用该编译器编译自身源码。fixed-point（<code>stage2.ll == stage3.ll</code>，驻留模式再加 <code>stage3.ll == stage4.ll</code>）证明语言能力足以支撑真实编译器开发。</p>
</div>

<div class="callout tip">
  <p class="callout-title">工具链已 shadow 原生化</p>
  <p>旧的 <code>build_shadow.sh</code> / <code>build_resident.sh</code> / <code>build_run_tests.sh</code> 已由 <code>tools/build_shadow.shadow</code> / <code>tools/build_resident.shadow</code> / <code>tools/build_run_tests.shadow</code> 取代，三者均经冻结的 <code>build/shadow.exe</code> 编译并验证收敛到固定点。完整的构建步骤见[构建指南](/building/)。</p>
</div>

## 生成可执行文件

### 一键运行

`--run` 自动完成 llc + 链接 + 运行（链接 shadow-0.5 自带 rt 运行时层）：

```bash
shadow hello.shadow --run
```

### 手工分步（可选）

先用 `-o` 生成 IR，再用 LLVM 工具链手工编译：

```bash
shadow hello.shadow -o hello.ll
llc -O0 -filetype=obj hello.ll -o hello.o
clang++ hello.o <rt 层 .o 列表> -o hello
```

## 测试流程

测试用例位于 `test/cases/`（按 `tc` / `codegen` / `exe` / `check` 等模式分组），每个用例是一个可独立编译运行的 `.shadow` 文件。测试运行器为**原生 shadow 实现** `test/run_tests.shadow`（由 `tools/build_run_tests.shadow` 构建为 `build/run_tests.exe`），对每个用例执行：

1. `build/shadow.exe <case>.shadow`（按模式走 `--check` / `-o .ll` / `--run`）
2. 比对输出与 `//@expect`（或 `#@expect`）注释中的期望值

```bash
# 串行（默认 -j 1）
build/run_tests.exe

# 并行：每用例作为独立 shadow.exe 子进程（CreateProcessA）启动
build/run_tests.exe -j 8          # 短选项
build/run_tests.exe --jobs 8      # 长选项，等价
```

<div class="callout tip">
  <p class="callout-title">并行（-j）注意事项</p>
  <p>并行模式下每个子进程写入独立的 <code>SHADOW_LU_CACHE_DIR</code> 缓存目录（<code>build/lu_cache_s&lt;slot&gt;</code>），避免多 <code>shadow.exe</code> 并发写同一 <code>build/lu_cache</code> 的竞态。全量并行回归 <code>-j 8</code> 结果与串行一致（PASS=925 / FAIL=0 / SKIP=30）。</p>
</div>

<div class="callout warn">
  <p class="callout-title">测试约定</p>
  <p>每个测试用例文件首部含 <code>//@desc</code>（描述）、<code>//@expect</code>（期望输出）等指令，另支持 <code>//@mode</code> / <code>//@skip</code> / <code>//@xfail</code>。测试脚本据此自动验证。<strong>仅生成 .ll 而未编译运行视为未完成</strong>。</p>
</div>

## 项目结构

```
shadow-0.5/
├── src/                    # 编译器源码（shadow 语言实现）
│   ├── main.shadow         # 主入口（CLI / LSP / 查询）
│   ├── lexer/ parser/ type_checker/ hir/ mir/ codegen/ api/ lsp/
│   └── gc/ sbg/ spk/ semver/ std/ runtime/   # 子系统
├── test/
│   ├── cases/              # 用例（tc/codegen/exe/check 等分组）
│   └── run_tests.shadow    # 测试运行器（源）；构建出 build/run_tests.exe
├── tools/                  # 构建工具（shadow 原生）
│   ├── build_shadow.shadow     # → build/build_shadow.exe（7 阶段自举）
│   ├── build_resident.shadow   # → build/build_resident.exe（驻留部署）
│   └── build_run_tests.shadow  # → build/run_tests.exe（测试运行器）
├── rt/                     # C 运行时层（rt_core.c / rt_fs.c / rt_test_par.c …）
├── bootstrap/              # runtime_for_selfhost.o / miniz.o / sys_exec_cpa.c
├── std/                    # 标准库（.spk 源 + .sbg 字节码）
└── build/                  # 构建产物（build/shadow.exe 等）
```

## 调试技巧

### 查看 IR

编译后直接阅读 `.ll`，检查：

- 类型是否正确（`i32` / `i64` / `double` / `ptr`）。
- 控制流是否正确（基本块、分支）。
- 函数签名是否匹配。

### 逐步验证

对每个新特性，建议：

1. 先写最小 `.shadow` 用例。
2. 生成 `.ll` 检查 IR 合理性。
3. 编译为 `.exe` 运行验证输出。
4. 加入 `test/cases/` 对应分组作为回归测试。

## 常见问题

| 问题 | 排查 |
|------|------|
| `undefined symbol` | 链接时漏了 rt 层 .o / 跨模块符号未 `pub` |
| `segmentation fault` | 检查 `hashmap_free`/`set_free` 是否误调或漏调 |
| IR 类型不匹配 | 检查 `let` 类型标注与字面量是否一致 |
| `match` 未覆盖 | 加 `_` 兜底臂 |

## 下一步

- 阅读[构建指南](/building/)了解自举与测试的完整步骤。
- 返回[首页](/)。
- 阅读[关于 shadow](/about/)了解项目路线图。
