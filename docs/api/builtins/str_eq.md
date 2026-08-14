---
layout: doc
title: "str_eq"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_eq/
---

# `str_eq`

**字符串处理** 内置函数。

比较两个字符串是否相等（等价于 ==）。

## 函数签名

```shadow
str_eq(a: string, b: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `a` | `string` | 左操作数 |
| `b` | `string` | 右操作数 |

## 出参

- 类型：`int`
- 说明：相等为 1，否则 0

## 示例

```shadow
if (str_eq(a, b) == 1) { }
```
