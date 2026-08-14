---
layout: doc
title: "array_push"
summary: "数组 · 内置函数"
permalink: /api/builtins/array_push/
---

# `array_push`

**数组** 内置函数。

将元素追加到数组末尾，返回新数组（可变长）。

## 函数签名

```shadow
array_push(arr: array<T>, elems: ...) -> array<T>
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `arr` | `array<T>` | 目标数组 |
| `elems` | `...` | 一个或多个待追加元素（类型须与数组元素一致） |

## 出参

- 类型：`array<T>`
- 说明：追加后的数组

## 示例

```shadow
parts = array_push(parts, "x");
```
