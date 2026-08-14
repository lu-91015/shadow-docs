---
layout: doc
title: "parse_float"
summary: "解析 · 内置函数"
permalink: /api/builtins/parse_float/
---

# `parse_float`

**解析** 内置函数。

将字符串解析为 double（失败返回 0.0）。

## 函数签名

```shadow
parse_float(s: string) -> double
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 数字字符串 |

## 出参

- 类型：`double`
- 说明：解析出的浮点数

## 示例

```shadow
let f = parse_float("3.14");
```
