---
layout: doc
title: "快速开始"
summary: "从零编写并运行第一个 shadow 程序。"
permalink: /getting-started/
prev: /install/
next: /syntax/
---

## 环境准备

运行 shadow 程序需要：

1. **shadow 编译器**（`shadow`）：将 `.shadow` 源码编译为 LLVM IR，并可直接链接运行。
2. **LLVM 工具链**：`llc` / `clang++`（仅 `--run` 链接时使用，随编译器分发环境）。

## 创建项目

用 `shadow -init` 初始化一个新项目（注意是 **`-init`**，带前导短横，不是 `init`）：

```bash
shadow -init myapp     # 新建 myapp/ 并生成 myapp/shadow.sbg
cd myapp
```

它会在目录里生成 `shadow.sbg` 项目清单（包名取目录名，版本 `0.1.0`），记录包信息与依赖。
包管理、依赖声明与 `.spk` 包的完整用法见 [包管理（SPK）]({{ "/package-manager/" | relative_url }})。

## 第一个程序

创建 `hello.shadow`：

```shadow
dsb hello;

kimo main() -> int {
    let name = "shadow";
    println("Hello, " + name + "!");
    return 0;
}
```

### 编译并运行

shadow 的标准编译流程是：**源码 → LLVM IR（`.ll`）→ 可执行文件**。

```bash
# 方式一：编译 + 链接 + 运行（一条命令）
shadow hello.shadow --run
# 输出: Hello, shadow!

# 方式二：只生成 LLVM IR
shadow hello.shadow -o hello.ll
```

<div class="callout note">
  <p class="callout-title">为什么先生成 .ll？</p>
  <p>shadow 以 LLVM 为原生后端。<code>.ll</code> 是人类可读的 LLVM IR 中间产物，便于调试与优化观察。生成 <code>.ll</code> 后可用 LLVM 工具链（<code>llc</code>/<code>clang++</code>）进一步编译为可执行文件。</p>
</div>

## 程序结构拆解

一个 shadow 程序的最小骨架：

```shadow
dsb <模块名>;          // 模块声明，每个 .shadow 文件即一个模块

kimo main() -> int {   // 入口函数，返回 int
    // 语句...
    return 0;
}
```

- `dsb` —— 声明当前文件所属模块（详见[模块系统]({{ "/modules/" | relative_url }})）。
- `kimo` —— 函数定义关键字（详见[函数与闭包]({{ "/functions/" | relative_url }})）。
- `main` —— 程序入口，约定返回 `int`，`0` 表示成功。
- `let` —— 变量绑定，类型可省略由推导决定（详见[语法基础]({{ "/syntax/" | relative_url }})）。

## 进阶：使用容器与循环

```shadow
dsb demo;

kimo main() -> int {
    let arr = [1, 2, 3];
    let sum = 0;
    for (x in arr) {
        sum = sum + x;
    }
    println(sum);   // 6
    return 0;
}
```

## 进阶：模式匹配

```shadow
dsb demo;

enum Option<T> {
    Some(T),
    None,
}

kimo main() -> int {
    let x = Some(42);
    let r = match x {
        Some(v) => v,
        None    => 0,
    };
    println(r);     // 42
    return 0;
}
```

## 下一步

- [语法基础]({{ "/syntax/" | relative_url }})：变量、字面量与基础类型。
- [类型系统]({{ "/types/" | relative_url }})：string / array / dict / set 容器详解。
- [函数与闭包]({{ "/functions/" | relative_url }})：`kimo` 定义与闭包捕获。

<div class="callout tip">
  <p class="callout-title">提示</p>
  <p>本文档示例均对照 shadow-0.5 编译器实测验证。编译器命令为 <code>shadow</code>（shadow-0.5 的 <code>build/shadow.exe</code>）。</p>
</div>
