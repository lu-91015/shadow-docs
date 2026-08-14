---
layout: doc
title: "char_to_str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/char_to_str/
---

# `char_to_str`

**类型转换** 内置函数。

将 char 转换为单字符字符串。

## 函数签名

```shadow
char_to_str(c: char) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `c` | `char` | 字符 |

## 出参

- 类型：`string`
- 说明：单字符字符串

## 示例

```shadow
let s = char_to_str('A');
```
