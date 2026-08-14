---
layout: doc
title: "str_ends_with"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_ends_with/
---

# `str_ends_with`

**字符串处理** 内置函数。

判断 s 是否以 suffix 结尾。

## 函数签名

```shadow
str_ends_with(s: string, suffix: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `suffix` | `string` | 后缀 |

## 出参

- 类型：`int`
- 说明：是则 1，否则 0

## 示例

```shadow
if (str_ends_with("file.txt", ".txt") == 1) { }
```
