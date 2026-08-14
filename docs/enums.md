---
layout: doc
title: "枚举"
summary: "enum 定义、泛型载荷变体与无载荷变体引用。"
permalink: /enums/
prev: /structs/
next: /pattern-matching/
---

`enum` 定义代数数据类型（和类型）。每个变体可携带载荷（数据），是 shadow 表达"可选值"、"状态机"、"错误类型"的核心工具。

## 定义 enum

### 无载荷枚举

变体不带数据，类似 C 的枚举：

```shadow
enum Color {
    Red;
    Green;
    Blue;
}
```

### 带载荷枚举

变体携带数据，类似 Rust 的 enum：

```shadow
enum Shape {
    Circle(int),       // 单字段载荷
    Rect(int, int),    // 多字段载荷
    Point              // 无载荷
}
```

### 泛型枚举

enum 支持泛型参数 `<T>`：

```shadow
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

## 构造变体

### 带载荷变体

用 `Variant(value)` 构造：

```shadow
let c = Circle(7);          // Shape::Circle, 载荷 7
let r = Rect(3, 5);         // Shape::Rect, 载荷 (3, 5)
let opt = Some(42);         // Option<int>::Some
let none = None;            // Option::None（无载荷，直接引用）
```

### 无载荷变体

直接引用变体名：

```shadow
let red = Color.Red;
let p = Point;
let n = None;
```

<div class="callout note">
  <p class="callout-title">变体引用</p>
  <p>无载荷变体既可直接写名字（<code>None</code>），也可用限定形式（<code>Color.Red</code>）。带载荷变体必须用函数调用形式（<code>Some(42)</code>）。</p>
</div>

## 完整示例：泛型枚举 + match

```shadow
dsb cg_enum_payload_int;

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
    println(r);       // 42
    return 0;
}
```

## 完整示例：多载荷枚举

```shadow
enum Shape {
    Circle(int),
    Rect(int, int),
    Point
}

kimo describe(s: Shape) -> int {
    let out = 0;
    match s {
        Circle(r) => {
            println("circle");
            println(r);
            out = r * 10;
        },
        Rect(w, h) => {
            println("rect");
            out = w * h;
        },
        Point => {
            println("point");
            out = 1;
        }
    }
    return out;
}

kimo main() -> int {
    println(describe(Circle(7)));    // 70
    println(describe(Rect(3, 5)));   // 15
    println(describe(Point));        // 1
    return 0;
}
```

match 详解见[模式匹配](/pattern-matching/)。

## 常见模式

### Option —— 可选值

```shadow
enum Option<T> { Some(T), None }

kimo divide(a: int, b: int) -> Option<int> {
    if (b == 0) {
        return None;
    }
    return Some(a / b);
}

kimo main() -> int {
    let r = divide(10, 2);
    let v = match r {
        Some(x) => x,
        None    => -1,
    };
    println(v);   // 5
    return 0;
}
```

### 状态机

```shadow
enum State {
    Idle,
    Running,
    Stopped
}

kimo next_state(s: State) -> State {
    return match s {
        Idle     => Running,
        Running  => Stopped,
        Stopped  => Idle
    };
}
```

## 与 struct 的对比

| 特性 | struct | enum |
|------|--------|------|
| 类型关系 | 与（AND）：所有字段同时存在 | 或（OR）：一个实例只属于一个变体 |
| 用途 | 描述实体的结构 | 描述互斥的可能性 |
| 载荷 | 命名字段 | 位置载荷或无载荷 |
| 构造 | `T { f: v }` | `Variant(v)` 或 `Variant` |

## 下一步

- [模式匹配](/pattern-matching/)：用 match 处理 enum 的所有变体。
- [错误处理](/error-handling/)：用 enum 表达错误，或用 try/catch。
