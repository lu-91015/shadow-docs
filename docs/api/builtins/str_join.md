---
layout: doc
title: "str_join"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_join/
---

# `str_join`

**字符串处理** 内置函数。

用 sep 将字符串数组连接成一个字符串。

## 函数签名

```shadow
str_join(parts: array<string>, sep: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `parts` | `array<string>` | 片段列表 |
| `sep` | `string` | 连接符 |

## 出参

- 类型：`string`
- 说明：拼接结果

## 示例

```shadow
let s = str_join(parts, ",");
```
