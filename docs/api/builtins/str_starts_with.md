---
layout: doc
title: "str_starts_with"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_starts_with/
---

# `str_starts_with`

**字符串处理** 内置函数。

判断 s 是否以 prefix 开头。

## 函数签名

```shadow
str_starts_with(s: string, prefix: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `prefix` | `string` | 前缀 |

## 出参

- 类型：`int`
- 说明：是则 1，否则 0

## 示例

```shadow
if (str_starts_with("file.txt", "file") == 1) { }
```
