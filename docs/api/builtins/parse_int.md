---
layout: doc
title: "parse_int"
summary: "解析 · 内置函数"
permalink: /api/builtins/parse_int/
---

# `parse_int`

**解析** 内置函数。

将字符串解析为 int（失败返回 0）。

## 函数签名

```shadow
parse_int(s: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 数字字符串 |

## 出参

- 类型：`int`
- 说明：解析出的整数

## 示例

```shadow
let n = parse_int("42");
```
