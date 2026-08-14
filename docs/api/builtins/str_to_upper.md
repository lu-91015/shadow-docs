---
layout: doc
title: "str_to_upper"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_to_upper/
---

# `str_to_upper`

**字符串处理** 内置函数。

将字符串转为大写。

## 函数签名

```shadow
str_to_upper(s: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |

## 出参

- 类型：`string`
- 说明：全大写

## 示例

```shadow
let r = str_to_upper("abc");  // "ABC"
```
