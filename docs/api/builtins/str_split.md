---
layout: doc
title: "str_split"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_split/
---

# `str_split`

**字符串处理** 内置函数。

按 sep 分割字符串为字符串数组。

## 函数签名

```shadow
str_split(s: string, sep: string) -> array<string>
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `sep` | `string` | 分隔符 |

## 出参

- 类型：`array<string>`
- 说明：分割后的片段列表

## 示例

```shadow
let parts = str_split("a,b,c", ",");
```
