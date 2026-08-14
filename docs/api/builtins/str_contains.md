---
layout: doc
title: "str_contains"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_contains/
---

# `str_contains`

**字符串处理** 内置函数。

判断 s 是否包含子串 sub。

## 函数签名

```shadow
str_contains(s: string, sub: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `sub` | `string` | 子串 |

## 出参

- 类型：`int`
- 说明：包含为 1，否则 0

## 示例

```shadow
if (str_contains("abc", "b") == 1) { }
```
