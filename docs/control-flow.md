---
layout: doc
title: "控制流"
summary: "if / else、while、for...in 遍历与 break / continue。"
permalink: /control-flow/
prev: /types/
next: /functions/
---

shadow 的控制流语句与 C/Java 系语言接近，但 `for` 采用 `for (x in iter)` 迭代形式，更接近现代语言风格。

## if / else

条件分支用 `if (cond) { ... } else { ... }`：

```shadow
let x = 1;
let result = 0;
if (x > 0) {
    result = 1;
} else {
    result = 2;
}
println(result);   // 1
```

### else if 链

```shadow
if (score >= 90) {
    grade = "A";
} else if (score >= 60) {
    grade = "B";
} else {
    grade = "C";
}
```

条件表达式必须是 `bool` 类型（比较或逻辑运算的结果）。

## while

`while (cond) { ... }` 在条件为真时重复执行：

```shadow
let i = 0;
while (i < 3) {
    println(i);
    i = i + 1;
}
// 输出: 0 1 2
```

while 常用于带索引的数组遍历（见[类型系统 - 数组]({{ "/types/#数组-arrayt" | relative_url }})）：

```shadow
let arr = [10, 20, 30];
let i = 0;
while (i < len(arr)) {
    println(arr[i]);
    i = i + 1;
}
```

## for ... in

`for (x in iter) { ... }` 用于迭代数组、dict、set 等可迭代对象。

### 数组迭代

```shadow
dsb codegen_for_loop;
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

### dict 迭代

dict 支持两种形式：单变量（keys）与双变量（keys + values）：

```shadow
let d: dict<string, string> = hashmap_new();
hashmap_insert(d, "a", "1");
hashmap_insert(d, "b", "2");

// 单变量：迭代 keys
for (k in d) {
    println(k);
}

// 双变量：迭代 keys + values
for (k, v in d) {
    println(k + "=" + v);
}
```

### set 迭代

```shadow
let s: set<int> = set_new();
set_add(s, 1);
set_add(s, 2);
for (x in s) {
    println(x);
}
```

## break 与 continue

- `break` —— 立即跳出最近的循环。
- `continue` —— 跳过本次循环体剩余部分，进入下一次迭代。

```shadow
let i = 0;
while (i < 10) {
    i = i + 1;
    if (i == 3) {
        continue;     // 跳过 3
    }
    if (i == 7) {
        break;        // 到 7 停止
    }
    println(i);
}
// 输出: 1 2 4 5 6
```

<div class="callout warn">
  <p class="callout-title">注意</p>
  <p><code>break</code> / <code>continue</code> 仅作用于最近的 <code>while</code> 或 <code>for</code> 循环，不支持跨多层跳转。</p>
</div>

## return

`return expr;` 从函数返回。在 `match` 臂内 `return` 可提前退出整个函数（见[模式匹配]({{ "/pattern-matching/#语句级-match" | relative_url }})）。

```shadow
kimo find(arr: array<int>) -> int {
    for (x in arr) {
        if (x == 42) {
            return 1;    // 提前返回
        }
    }
    return 0;
}
```

## 完整示例

```shadow
dsb control_flow_demo;

kimo main() -> int {
    let arr = [3, 1, 4, 1, 5, 9, 2, 6];

    // while + 索引
    let i = 0;
    let max = 0;
    while (i < len(arr)) {
        if (arr[i] > max) {
            max = arr[i];
        }
        i = i + 1;
    }
    println(max);          // 9

    // for + continue/break
    for (x in arr) {
        if (x == 1) { continue; }
        if (x > 8)  { break; }
        println(x);
    }
    // 输出: 3 4 5
    return 0;
}
```

## 下一步

- [函数与闭包]({{ "/functions/" | relative_url }})：把这些逻辑封装成可复用单元。
- [模式匹配]({{ "/pattern-matching/" | relative_url }})：比 if/else 更强的分支控制。
