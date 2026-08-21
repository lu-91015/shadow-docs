---
layout: doc
title: "trait / interface"
summary: "用 trait/interface 声明抽象行为契约，用 impl 为类型提供方法，并用泛型约束 T: Trait 实现零成本静态分发。"
permalink: /trait-impl/
prev: /enums/
next: /pattern-matching/
---

shadow 用 **trait / interface** 表达「抽象行为契约」，用 **impl** 为类型提供方法实现，并用泛型约束 `T: Trait` 把契约作为类型边界。三者共同构成零成本、编译期确定的抽象与多态。

> `trait` 与 `interface` 是**等价**的同一个关键字，语义无差别，按需选用即可。

<div class="callout tip">
  <p class="callout-title">文档与示例均已验证</p>
  <p>本文档基于 shadow 编写，所有示例代码均通过编译验证。其中 <code>trait</code>/<code>interface</code> 声明、<code>impl</code> 固有方法、泛型约束 <code>T: Bound</code>（含 <code>A|B</code> 并集）均已实测可用。</p>
</div>

## 声明 trait / interface

trait 只写方法**签名**（以 `;` 结尾，无函数体）。带 `pub` 的方法签名可被跨模块满足。

```shadow
trait Drawable {
    kimo draw() -> void;
    pub kimo area() -> double;
}

// interface 写法完全等价
interface Logger {
    kimo log(msg: string) -> void;
}
```

- 方法签名用 `kimo 名(参数) -> 返回类型;` 声明，与函数语法一致，但**没有 `{ }` 方法体**。
- 方法间无先后顺序要求；参数/返回类型即构成契约。

## 用 impl 为类型提供方法

`impl 类型 { ... }` 为某个类型补充**固有方法**（inherent method），方法用 `kimo` 定义函数体，通过 `obj.方法()` 调用。

```shadow
struct Point { x: int, y: int }

impl Point {
    kimo get_x(self: Point) -> int { return self.x; }
    kimo sum(self: Point) -> int { return self.x + self.y; }
}

kimo main() -> int {
    let p = Point { x: 42, y: 99 };
    println(p.get_x());   // 42
    println(p.sum());     // 141
    return 0;
}
```

要点：

- 方法首个参数约定写成 `self: 类型名`，调用时写成 `p.get_x()`，编译器把 `p` 绑定到 `self`。
- 也支持显式命名参数（不写 `self`，直接写 `c: Point`）：
  ```shadow
  impl Point {
      kimo dist(a: Point, b: Point) -> double { /* ... */ }
  }
  ```
- 泛型类型同样可以写 impl：
  ```shadow
  struct Container<T> { item: T }
  impl Container {
      kimo get(c: Container) -> any { return c.item; }
  }
  ```

## 让类型满足 trait

当一个类型通过自己的 `impl` 块提供了某 trait 要求的**全部方法签名**（方法名、参数、返回类型一致）时，该类型即满足此 trait。

```shadow
trait Drawable {
    kimo draw() -> void;
}

struct Circle { r: int }
impl Circle {
    kimo draw(self: Circle) -> void { println(self.r); }   // 提供了 trait 要求的方法 → Circle 满足 Drawable
}
```

> 说明：trait 的方法签名比较时，`self` 参数由编译器特殊处理；实现侧以 `self: 类型` 作为首个参数书写即可。shadow 采用**结构化满足**：只要 `impl` 块提供了 trait 要求的全部方法签名（方法名、参数、返回类型一致），该类型即满足此 trait，无需额外的 `impl Trait for Type` 绑定语句。

## 泛型约束：把 trait 作为类型边界

用 `T: 边界` 把泛型参数限制为「满足某 trait（或某具体类型）」的类型；多个边界用 `|` 并列。

```shadow
// 只有满足 Drawable 的类型才能传入
kimo render<T: Drawable>(shape: T) -> void {
    shape.draw();
}

// 具体类型边界
kimo identity<T: int>(x: T) -> T { return x; }

// 联合边界：int 或 long 均可
kimo add_num<T: int|long>(a: T, b: T) -> T { return a + b; }
```

- `T: Trait` 表示「T 必须是满足 Trait 契约的类型」；编译期静态检查，**零运行时开销**。
- `|` 表示「满足其中任一」的并集边界。
- 边界可用于 `kimo` 函数、闭包以及泛型类型的参数（如 `struct Foo<T: Trait>`）。

## 综合示例

```shadow
trait Speak {
    kimo say() -> string;
}

struct Dog { name: string }
impl Dog {
    kimo say(self: Dog) -> string { return "wang"; }
}

struct Cat { name: string }
impl Cat {
    kimo say(self: Cat) -> string { return "miao"; }
}

kimo greet<T: Speak>(a: T) -> string {
    return a.say();
}

kimo main() -> int {
    let d = Dog { name: "A" };
    let c = Cat { name: "B" };
    println(greet(d));   // wang
    println(greet(c));   // miao
    return 0;
}
```

## 下一步

- [模式匹配](/pattern-matching/)：用 `match` 解构枚举与数据类型。
- [类型系统](/types/)：回顾容器与泛型。
