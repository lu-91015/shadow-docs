---
layout: doc
title: "substr2"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/substr2/
---

# `substr2`

**字符串处理** 内置函数。

取从 start 开始、长度为 n 的子串。

## 函数签名

```shadow
substr2(s: string, start: int, n: int) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `start` | `int` | 起始下标（0 基） |
| `n` | `int` | 长度 |

## 出参

- 类型：`string`
- 说明：子串

## 示例

```shadow
let sub = substr2("hello", 1, 3);  // "ell"
```
