---
layout: doc
title: "str_to_lower"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_to_lower/
---

# `str_to_lower`

**字符串处理** 内置函数。

将字符串转为小写。

## 函数签名

```shadow
str_to_lower(s: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |

## 出参

- 类型：`string`
- 说明：全小写

## 示例

```shadow
let r = str_to_lower("ABC");  // "abc"
```
