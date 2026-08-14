---
layout: doc
title: "parse_long"
summary: "解析 · 内置函数"
permalink: /api/builtins/parse_long/
---

# `parse_long`

**解析** 内置函数。

将字符串解析为 long（失败返回 0）。

## 函数签名

```shadow
parse_long(s: string) -> long
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 数字字符串 |

## 出参

- 类型：`long`
- 说明：解析出的长整数

## 示例

```shadow
let n = parse_long("9000000000");
```
