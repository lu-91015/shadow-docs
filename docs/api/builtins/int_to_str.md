---
layout: doc
title: "int_to_str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/int_to_str/
---

# `int_to_str`

**类型转换** 内置函数。

将 int 转换为十进制字符串。

## 函数签名

```shadow
int_to_str(i: int) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `i` | `int` | 整数 |

## 出参

- 类型：`string`
- 说明：十进制字符串

## 示例

```shadow
let s = int_to_str(42);  // "42"
```
