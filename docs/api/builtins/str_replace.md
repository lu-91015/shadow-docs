---
layout: doc
title: "str_replace"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_replace/
---

# `str_replace`

**字符串处理** 内置函数。

将 s 中所有 from 替换为 to。

## 函数签名

```shadow
str_replace(s: string, from: string, to: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `from` | `string` | 被替换子串 |
| `to` | `string` | 替换后的子串 |

## 出参

- 类型：`string`
- 说明：替换后的字符串

## 示例

```shadow
let r = str_replace("a-b-c", "-", ".");  // "a.b.c"
```
