---
layout: doc
title: "关于 shadow"
summary: "shadow 语言的设计目标、核心特性与适用场景。"
permalink: /about/
next: /install/
---

## shadow 是什么

shadow 是一门**粉丝向语言**，以 LLVM 为原生后端，融合了现代语言的工程化特性与系统编程的底层控制力。它的设计目标是在保持 C/C++ 级性能的同时，提供更严格的类型系统、更安全的并发模型与更简洁的语法。

当前版本为 **v0.5**，编译管线已完整自举——编译器由 shadow 自身实现（shadow-0.5），`build/shadow.exe` 编译自身源码达到 fixed-point，并通过全量测试集。

## 设计原则

- **零成本抽象**：trait/impl、泛型、闭包等高层抽象在编译期解析，运行时无额外开销。
- **类型驱动安全**：强类型 + 类型推导，错误在编译期暴露；match 穷尽性受检查，枚举载荷受类型检查约束。
- **显式优于隐式**：模块用 `dsb` 显式声明，可见性用 `pub` 显式标注，没有隐式导出。
- **LLVM 原生**：直接生成 LLVM IR，复用 LLVM 的全套优化 pass 与多平台目标支持。

## 核心特性一览

| 特性 | 说明 |
|------|------|
| 原生 LLVM 后端 | 直接产出 LLVM IR，支持完整优化与跨平台代码生成 |
| 基础类型 | `int` / `long` / `float` / `double` / `string` / `bool` |
| 容器类型 | `array<T>` / `dict<K,V>` / `set<T>` |
| 函数 | `kimo` 关键字定义，带类型参数与返回值 |
| 闭包 | `kimo(params) -> ret { body }` 字面量，自动捕获环境 |
| 结构体 | `struct` + 命名字段，支持省略零初始化与乱序赋值 |
| 枚举 | `enum` + 泛型载荷，`enum Option<T> { Some(T), None }` |
| 模式匹配 | `match` 表达式与语句，支持载荷解构、字面量、通配符 |
| 错误处理 | `try` / `catch` / `throw` 结构化异常 |
| 模块系统 | `dsb` 声明模块，`import` 跨文件复用，`pub` 控制导出 |
| 并发任务 | `spawn` 派生任务；`async`/`await` 协程（测试中） |

## 适用场景

shadow 适合以下场景：

- **系统编程**：编译器、运行时、虚拟机等需要底层控制与高性能的工具链开发。
- **命令行工具**：快速产出原生可执行文件，启动快、依赖少。
- **性能敏感型服务**：LLVM 优化后的代码可用于计算密集型后端逻辑。
- **语言学习与研究**：自举编译器本身就是 shadow 语言能力的最佳实证。

## 本文档的来源

本文档中的**代码示例**均对照 shadow-0.5 编译器实测验证（`build/shadow.exe --check`），并与测试用例集（`test/cases/`）交叉核对。

## 项目状态

- v0.5：编译管线完整自举（fixed-point），严格态 import/可见性模型（Java 风格）。
- 工具链 shadow 原生化：`build_shadow` / `build_resident` / `run_tests` 三个构建工具均已用 shadow 自身实现（源 `tools/*.shadow`、`test/run_tests.shadow`），由冻结的 `build/shadow.exe` 编译并验证收敛到自举固定点。
- 测试覆盖：全量 **955** 用例（PASS=925 / FAIL=0 / SKIP=30），涵盖变量、字符串、数组、dict、set、控制流、函数、闭包、struct、enum、match、try/catch、import、pub 等核心特性。
- 后续路线：完善标准库、强化 trait 系统、修复 async/await 协程运行时、补齐 Web/WASM 目标（对标 Java/Go/Rust 的 web 生态）。
