---
layout: doc
title: "to_string"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/to_string/
---

# `to_string`

**类型转换** 内置函数。

将任意值转换为字符串（等价于 str）。

## 函数签名

```shadow
to_string(x: any) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `x` | `any` | 任意可格式化的值 |

## 出参

- 类型：`string`
- 说明：字符串形式

## 示例

```shadow
let s = to_string(42);
```
