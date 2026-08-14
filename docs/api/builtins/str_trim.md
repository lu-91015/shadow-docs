---
layout: doc
title: "str_trim"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_trim/
---

# `str_trim`

**字符串处理** 内置函数。

去除首尾空白字符。

## 函数签名

```shadow
str_trim(s: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |

## 出参

- 类型：`string`
- 说明：去空白后的字符串

## 示例

```shadow
let r = str_trim("  hi  ");  // "hi"
```
