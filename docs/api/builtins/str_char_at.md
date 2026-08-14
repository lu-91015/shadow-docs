---
layout: doc
title: "str_char_at"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_char_at/
---

# `str_char_at`

**字符串处理** 内置函数。

取第 idx 个字符（返回单字符字符串）。

## 函数签名

```shadow
str_char_at(s: string, idx: int) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `idx` | `int` | 下标（负索引回绕，越界返回空串） |

## 出参

- 类型：`string`
- 说明：单字符子串

## 示例

```shadow
let c = str_char_at("abc", 1);  // "b"
```
