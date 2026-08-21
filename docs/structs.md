---
layout: doc
title: "结构体"
summary: "struct 定义、命名字段构造、字段访问与零初始化。"
permalink: /structs/
prev: /functions/
next: /enums/
---

`struct` 定义命名字段的复合类型。shadow 的 struct 构造非常灵活：支持省略字段（零初始化）与乱序赋值（按名落位）。

## 定义 struct

```shadow
struct Point {
    x: int;
    y: int;
}
```

字段用 `字段名: 类型;` 声明，每行一个。字段类型可以是基础类型、容器或 `any`（任意类型）。

## 构造实例

用 `TypeName { field: value, ... }` 字面量构造：

```shadow
let p = Point { x: 1, y: 2 };
```

### 完整示例：省略字段与乱序赋值

```shadow
dsb cg_struct_named_fields;

struct S {
    a: int;
    b: int;
    s: string;
    arr: any;
}

kimo main() -> int {
    // 省略字段 → 零值（b=0，s=""）
    let x = S { a: 1 };
    println(x.a);       // 1
    println(x.b);       // 0
    println(len(x.s));  // 0

    // 乱序字段 → 按名字落位
    let y = S { s: "hi", a: 7, b: 8 };
    println(y.a);       // 7
    println(y.b);       // 8
    println(len(y.s));  // 2

    // 全字段
    let z = S { a: 10, b: 20, s: "abc", arr: [1, 2, 3] };
    println(z.a + z.b); // 30
    return 0;
}
```

### 关键特性

| 特性 | 说明 |
|------|------|
| **省略字段** | 未指定的字段自动初始化为零值（`int` → `0`，`string` → `""`） |
| **乱序赋值** | 字段可按任意顺序书写，编译器按名字匹配 |
| **字段访问** | 用 `实例.字段名` 读写 |

## 字段访问

```shadow
let p = Point { x: 3, y: 4 };
println(p.x);       // 3（读）
p.x = 10;           // 写
println(p.x);       // 10
```

字段访问也支持链式与在表达式中使用：

```shadow
let p1 = Point { x: 1, y: 2 };
let p2 = Point { x: 3, y: 4 };
let dx = p2.x - p1.x;   // 2
```

## any 字段

字段类型可声明为 `any`，表示接受任意类型值：

```shadow
struct Mixed {
    id: int;
    data: any;
}

let m = Mixed { id: 1, data: [10, 20, 30] };
let m2 = Mixed { id: 2, data: "text" };
```

<div class="callout warn">
  <p class="callout-title">注意</p>
  <p><code>any</code> 字段在编译期不进行类型检查，使用时需自行保证类型正确。优先使用具体类型以获得类型安全。</p>
</div>

## 作为函数参数与返回值

```shadow
struct Rect {
    w: int;
    h: int;
}

kimo area(r: Rect) -> int {
    return r.w * r.h;
}

kimo make_square(side: int) -> Rect {
    return Rect { w: side, h: side };
}

kimo main() -> int {
    let s = make_square(5);
    println(area(s));    // 25
    return 0;
}
```

## 嵌套 struct

struct 字段类型可以是另一个 struct：

```shadow
struct Point { x: int; y: int; }
struct Circle {
    center: Point;
    radius: int;
}

let c = Circle {
    center: Point { x: 0, y: 0 },
    radius: 10,
};
println(c.center.x);    // 0
println(c.radius);      // 10
```

## 可见性

默认 struct 是模块私有的。加 `pub` 可导出：

```shadow
pub struct PublicPoint {
    x: int;
    y: int;
}
```

详见[模块系统]({{ "/modules/" | relative_url }})。

## 下一步

- [枚举]({{ "/enums/" | relative_url }})：表示代数数据类型（和类型）。
- [模式匹配]({{ "/pattern-matching/" | relative_url }})：解构 struct 字段。
