---
layout: doc
title: "模式匹配"
summary: "match 表达式与语句、枚举载荷解构、字面量匹配与通配符。"
permalink: /pattern-matching/
prev: /enums/
next: /error-handling/
---

`match` 是 shadow 最强大的控制结构。它对值进行模式测试，匹配成功后执行对应臂（arm），并支持载荷解构。match 分为**表达式**（产生值）与**语句**（执行副作用）两种形式。

## match 表达式

`match` 作为表达式，每个臂 `=>` 右侧产生一个值，整个 match 的值就是匹配臂的值。

### 字面量匹配

```shadow
let x = 2;
let r = match x {
    1 => 10,
    2 => 20,
    3 => 30,
};
println(r);   // 20
```

### 枚举变体匹配 + 载荷解构

```shadow
dsb cg_enum_payload_int;

enum Option<T> {
    Some(T),
    None,
}

kimo main() -> int {
    let x = Some(42);
    let r = match x {
        Some(v) => v,    // 解构载荷到 v
        None    => 0,
    };
    println(r);          // 42
    return 0;
}
```

`Some(v)` 中的 `v` 是绑定变量，match 成功后它绑定载荷值。

## 语句级 match

match 作为语句时，臂内是语句块，执行副作用，不产生值。

### 解构多字段载荷

```shadow
dsb cg_match_stmt_destructure;

enum Shape {
    Circle(int),
    Rect(int, int),
    Point
}

kimo describe(s: Shape) -> int {
    let out = 0;
    match s {
        Circle(r) => {              // 单字段解构
            println("circle");
            println(r);
            out = r * 10;
        },
        Rect(w, h) => {             // 多字段解构
            println("rect");
            println(w);
            println(h);
            out = w * h;
        },
        Point => {                  // 无载荷变体
            println("point");
            out = 1;
        }
    }
    return out;
}
```

### 通配符 `_`

用 `_` 匹配任意值，常作兜底：

```shadow
kimo pick(s: Shape) -> int {
    match s {
        Rect(w, h) => { return w + h; },
        _          => { }            // 其余情况什么都不做
    }
    return -1;
}
```

### match 臂内 return

臂内 `return` 会提前退出**整个函数**（不仅仅是 match）：

```shadow
kimo pick(s: Shape) -> int {
    match s {
        Rect(w, h) => { return w + h; },   // 直接返回 pick
        _          => { }
    }
    return -1;   // 仅在 _ 分支走到这里
}
```

## 模式类型

| 模式 | 示例 | 说明 |
|------|------|------|
| 字面量 | `1`, `"hi"`, `true` | 精确匹配值 |
| 变体（无载荷） | `Point`, `None` | 匹配该变体 |
| 变体（带载荷） | `Some(v)`, `Rect(w, h)` | 解构载荷到变量 |
| 通配符 | `_` | 匹配任意，兜底 |
| 绑定 | `v` | 匹配任意并绑定到 v |

## 臂的语法

两种形式：

```
// 单表达式臂
Pattern => expr,

// 语句块臂
Pattern => {
    stmt1;
    stmt2;
},
```

语句块臂末尾的 `,` 可选但建议保留。

<div class="callout warn">
  <p class="callout-title">穷尽性</p>
  <p>shadow 的 match 鼓励穷尽所有变体。若有未覆盖的变体且无 <code>_</code> 兜底，可能触发警告或运行时未匹配错误。建议总用 <code>_</code> 作为最后一个臂。</p>
</div>

## 完整示例

```shadow
dsb match_demo;

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
            println(w);
            println(h);
            out = w * h;
        },
        Point => {
            println("point");
            out = 1;
        }
    }
    return out;
}

kimo pick(s: Shape) -> int {
    match s {
        Rect(w, h) => { return w + h; },
        _ => { }
    }
    return -1;
}

kimo main() -> int {
    let a = describe(Circle(7));     // 70
    let b = describe(Rect(3, 5));    // 15
    let c = describe(Point);         // 1
    println(a);
    println(b);
    println(c);
    println(pick(Rect(4, 6)));       // 10
    return 0;
}
```

## match vs if/else

| 场景 | 推荐结构 |
|------|---------|
| 布尔条件分支 | `if/else` |
| 值的多路分发（字面量/变体） | `match` |
| 需要解构 enum 载荷 | `match`（唯一选择） |
| 链式比较判断 | `if/else if` |

## 下一步

- [错误处理](/error-handling/)：try/catch 与 throw。
- [模块系统](/modules/)：组织多文件项目。
