---
layout: doc
title: "函数与闭包"
summary: "kimo 函数定义、参数、返回值与一等闭包。"
permalink: /functions/
prev: /control-flow/
next: /structs/
---

shadow 用 `kimo` 关键字定义函数。函数是一等公民——可作为参数、返回值，也可用 `kimo` 字面量构造闭包。

## 函数定义

基本语法：

```
kimo 名称(参数: 类型, ...) -> 返回类型 {
    语句...
    return 值;
}
```

### 示例

```shadow
dsb func_call;
kimo add(a: int, b: int) -> int {
    return a + b;
}

kimo main() -> int {
    let x = add(1, 2);
    println(x);    // 3
    return 0;
}
```

- 参数必须显式标注类型。
- 返回类型用 `-> Type` 声明。
- 函数体用 `return expr;` 返回。

## 参数类型

参数可接受任何 shadow 类型，包括容器与自定义类型：

```shadow
// 数组参数
kimo sum_array(arr: array<int>) -> int {
    let total = 0;
    for (x in arr) {
        total = total + x;
    }
    return total;
}

// 字符串参数
kimo greet(name: string) -> string {
    return "Hello, " + name;
}

// 多参数
kimo make_point(x: int, y: int) -> int {
    return x + y;
}
```

## 返回值

返回类型可以是基础类型、容器或自定义 struct/enum：

```shadow
// 返回数组
kimo make_range(n: int) -> array<int> {
    return [0, 1, 2, 3, 4];   // 字面量
}

// 返回 struct（见 struct 章节）
kimo build() -> Point {
    return Point { x: 1, y: 2 };
}
```

<div class="callout note">
  <p class="callout-title">无返回值</p>
  <p>不返回值的函数可用 <code>-> void</code> 声明（0.5 支持）；入口 <code>main</code> 约定返回 <code>int</code>，<code>0</code> 表示成功。</p>
</div>

## 函数调用

```shadow
let r1 = add(1, 2);          // 位置参数
let r2 = sum_array([1,2,3]); // 字面量实参
```

## 闭包

闭包是匿名的可调用代码块，用 `kimo` 字面量定义，可捕获外层环境变量。

### 语法

```
kimo(参数: 类型, ...) -> 返回类型 { body }
```

闭包是一个**表达式**，可赋值给变量、作为参数传递、作为返回值。

### 捕获外层变量

```shadow
dsb cg_closure_capture_int;
kimo main() -> int {
    let x = 40;
    let f = kimo() -> int {
        return x + 2;     // 捕获外层 x
    };
    let r = f();          // 调用闭包
    println(r);           // 42
    return 0;
}
```

闭包内 `x` 引用了外层 `let x = 40;` 的绑定。调用 `f()` 时使用捕获的值。

### 闭包作为参数

闭包可作为高阶函数的参数：

```shadow
kimo apply(f: any, n: int) -> any {
    return f(n);
}

kimo main() -> int {
    let doubler = kimo(v: int) -> int {
        return v * 2;
    };
    println(apply(doubler, 21) as int);   // 42
    return 0;
}
```

### 闭包作为返回值

```shadow
kimo make_adder(base: int) -> any {
    return kimo(v: int) -> int {
        return base + v;
    };
}
```

## pub 可见性

模块内的函数默认私有。加 `pub` 前缀可导出供其他模块 `import` 调用：

```shadow
// 模块内私有
kimo helper() -> int { return 1; }

// 导出
pub kimo public_api() -> int {
    return helper();
}
```

详见[模块系统](/modules/)。

## 完整示例

```shadow
dsb functions_demo;

// 普通函数
kimo factorial(n: int) -> int {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// 接收闭包（参数用 any）
kimo twice(f: any, x: int) -> any {
    return f(f(x));
}

kimo main() -> int {
    println(factorial(5));        // 120

    let inc = kimo(v: int) -> int {
        return v + 1;
    };
    println(twice(inc, 10) as int);      // 12
    return 0;
}
```

## 下一步

- [结构体](/structs/)：自定义复合类型，配合函数构建抽象。
- [枚举](/enums/)：用 enum 表达代数数据类型。
