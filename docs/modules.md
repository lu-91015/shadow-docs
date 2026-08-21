---
layout: doc
title: "模块系统"
summary: "dsb 声明、import 导入与 pub 可见性控制。"
permalink: /modules/
prev: /error-handling/
next: /package-manager/
---

shadow 的模块系统基于文件：**一个 `.shadow` 文件 = 一个模块**。模块用 `dsb` 声明名字，用 `import` 跨文件引用，用 `pub` 控制哪些项对外可见。

## dsb 模块声明

每个 `.shadow` 文件首行用 `dsb` 声明模块名：

```shadow
dsb mylib;
```

模块名用于被其他文件 `import`。模块顶层可包含：

- `let` 常量（`pub let` 可导出）
- `kimo` 函数（`pub kimo` 可导出）
- `struct` 定义（`pub struct` 可导出）
- `enum` 定义（`pub enum` 可导出）

### 示例模块

```shadow
dsb dotqual_mod;

pub let ANSWER: int = 7;
pub let GREETING: string = "hi";

pub kimo helper() -> int {
    return 42;
}
```

这个 `dotqual_mod` 模块导出两个常量和一个函数。

## import 导入

用 `import <模块名>;` 引入另一个模块。导入后可直接调用其 `pub` 项。

### 文件布局

```
mylib.shadow      ← dsb mylib;  定义 pub 项
test_main.shadow  ← import mylib;  使用
```

### 使用示例

```shadow
// test_main.shadow
dsb test_main;

import mylib;

kimo main() -> int {
    println(pub_sum(19, 23));     // 调用 mylib 的 pub 函数
    println(make_point(3, 4));
    return 0;
}
```

`import mylib;` 后，`mylib` 中所有 `pub` 函数/常量/类型直接可用（无需限定前缀）。

### 模块限定访问

也可用限定形式访问：

```shadow
import mylib;
println(mylib.ANSWER);        // dsb 名限定访问
```

0.5 还支持完整路径限定（点号=目录路径），无需 `import` 也可访问：

```shadow
println(pkg.mylib.ANSWER);    // 完整路径限定（需能解析到文件）
```

<div class="callout note">
  <p class="callout-title">查找规则</p>
  <p><code>import mylib;</code> 会在主文件同目录（或嵌套子目录）查找 <code>mylib.shadow</code>。模块名与文件名必须一致（0.5 严格态：<code>dsb</code> 名必须等于文件名 basename）。<code>import</code> 依赖由编译器自动递归加载，无需在命令行显式列出。</p>
</div>

## pub 可见性

默认所有顶层项是**模块私有**的。加 `pub` 前缀才对外可见。

### 私有 vs 公开

```shadow
dsb mylib;

// 私有函数：只能在本模块内调用
kimo priv_add(a: int, b: int) -> int {
    return a + b;
}

// 公开函数：可被 import 方调用
pub kimo pub_sum(x: int, y: int) -> int {
    return priv_add(x, y);     // 模块内可调用私有
}

struct PrivPoint {             // 私有 struct
    x: int;
    y: int;
}

pub kimo make_point(px: int, py: int) -> int {
    let p = PrivPoint{ x: px, y: py };   // 模块内可构造私有 struct
    return p.x + p.y;
}
```

### 可见性规则表

| 项 | 默认 | 加 `pub` |
|----|------|---------|
| `let` 常量 | 模块私有 | 可被 import 方访问 |
| `kimo` 函数 | 模块私有 | 可被 import 方调用 |
| `struct` | 模块私有 | 可被 import 方构造 |
| `enum` | 模块私有 | 可被 import 方使用变体 |

模块**内部**可自由访问本模块的所有项（无论是否 `pub`）。

## 完整示例：多模块项目

### mylib.shadow（被导入方）

```shadow
dsb mylib;

// 私有：仅本模块用
kimo priv_add(a: int, b: int) -> int {
    return a + b;
}

pub kimo pub_sum(x: int, y: int) -> int {
    return priv_add(x, y);
}

struct PrivPoint {
    x: int;
    y: int;
}

pub kimo make_point(px: int, py: int) -> int {
    let p = PrivPoint{ x: px, y: py };
    return p.x + p.y;
}
```

### test_main.shadow（导入方）

```shadow
dsb test_main;

import mylib;

kimo main() -> int {
    println(pub_sum(19, 23));      // 42（调用 pub 函数）
    println(make_point(3, 4));     // 7
    return 0;
}
```

编译只需指定主文件（`import` 自动递归加载 `mylib`）：

```bash
shadow test_main.shadow -o program.ll
shadow test_main.shadow --run
```

## 模块常量

模块顶层可定义 `pub let` 常量，供其他模块读取：

```shadow
// config.shadow
dsb config;
pub let MAX_CONN: int = 100;
pub let VERSION: string = "1.0";
```

```shadow
// main.shadow
dsb main;
import config;
kimo main() -> int {
    println(config.MAX_CONN);
    println(config.VERSION);
    return 0;
}
```

## 编译多模块项目

`import` 是编译期解析的符号依赖，由编译器自动递归加载（`main_load_combined` 按 import 图拼装 combined 源码）。只需指定主文件：

```bash
shadow main.shadow -o out.ll
```

<div class="callout warn">
  <p class="callout-title">注意</p>
  <p>被 import 的模块必须能被解析到：同目录、嵌套子目录（点号=目录，如 <code>import a.b.c</code> → <code>a/b/c.shadow</code>）。解析失败会报模块加载诊断。</p>
</div>

## 下一步

- [库参考]({{ "/api/" | relative_url }})：内置函数与标准库 API。
- [工具链]({{ "/toolchain/" | relative_url }})：编译器、IR 生成与构建流程。
