---
layout: doc
title: "语法基础"
summary: "变量声明、字面量、基础类型与注释——shadow 程序的原子构件。"
permalink: /syntax/
prev: /getting-started/
next: /types/
---

## 模块声明

每个 `.shadow` 文件以 `dsb` 开头声明所属模块名：

```shadow
dsb my_module;
```

模块名用于跨文件 `import` 引用（详见[模块系统]({{ "/modules/" | relative_url }})）。一个文件 = 一个模块。

## 变量声明

使用 `let` 绑定变量。shadow 是**静态类型**语言，但大多数情况下类型可由右侧表达式推导，无需显式标注。

### 类型推导

```shadow
let x = 42;          // 推导为 int
let name = "Alice";  // 推导为 string
let pi = 3.14;       // 推导为 float/double
let flag = true;     // 推导为 bool
```

### 显式类型标注

当需要指定更精确的类型时，用 `let name: Type = value;`：

```shadow
dsb cg_long_var;
kimo main() -> int {
    let x: long = 100000;
    println(0);
    return 0;
}
```

显式标注在以下场景有用：

- 指定更宽的整型（`long` vs 默认 `int`）。
- 区分 `float` 与 `double` 精度。
- 容器类型的泛型参数（`array<int>`、`dict<string, string>`）。

## 基础类型

| 类型 | 说明 | 字面量示例 |
|------|------|-----------|
| `int` | 默认整数类型 | `42`, `-7` |
| `long` | 宽整数 | `100000` (显式标注) |
| `float` | 单精度浮点 | `1.5` (显式标注) |
| `double` | 双精度浮点 | `2.5`, `1e3` |
| `string` | 字符串 | `"hello"` |
| `bool` | 布尔 | `true`, `false` |

### 浮点字面量

```shadow
let x = 1e3;          // 科学计数法，double
let f: float = 1.5;   // 显式 float
let d: double = 2.5;  // 显式 double
```

## 字符串字面量

字符串用双引号包裹：

```shadow
let greeting = "Hello, World!";
let empty = "";
```

字符串支持 `+` 拼接，以及一组运行时函数（`str_split` / `str_join` / `str_format` 等，详见[类型系统 - 字符串]({{ "/types/#字符串" | relative_url }})）。

## 数组字面量

用方括号构造数组字面量：

```shadow
let arr = [1, 2, 3];           // array<int>
let names = ["Alice", "Bob"];  // array<string>
```

数组细节见[类型系统 - array]({{ "/types/#数组-arrayt" | relative_url }})。

## 注释

shadow 使用 C 风格注释：

```shadow
// 单行注释

/*
   多行注释
   可跨行
*/
```

## 语句与分号

shadow 语句以分号 `;` 结尾。块语句 `{ ... }` 内可包含多条语句。

```shadow
kimo main() -> int {
    let a = 1;
    let b = 2;
    let c = a + b;   // 3
    return c;
}
```

## 表达式

常见运算符：

| 类别 | 运算符 |
|------|--------|
| 算术 | `+` `-` `*` `/` |
| 比较 | `==` `!=` `<` `>` `<=` `>=` |
| 逻辑 | `&&` `\|\|` `!` |
| 赋值 | `=` `+=` `-=` 等 |

字符串 `+` 表示拼接。比较与逻辑运算结果为 `bool`。

## 完整示例

```shadow
dsb syntax_demo;

kimo main() -> int {
    // 基础类型变量
    let count: int = 10;
    let ratio: double = 0.5;
    let label: string = "demo";
    let enabled: bool = true;

    // 算术与比较
    let doubled = count * 2;
    let is_big = doubled > 15;

    if (is_big && enabled) {
        println(label + " ok");
    }
    return 0;
}
```

## 下一步

- [类型系统]({{ "/types/" | relative_url }})：深入 string / array / dict / set 容器。
- [控制流]({{ "/control-flow/" | relative_url }})：if / while / for 详解。
