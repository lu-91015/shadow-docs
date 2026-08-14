---
layout: doc
title: "double_to_str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/double_to_str/
---

# `double_to_str`

**类型转换** 内置函数。

将 double 转换为字符串。

## 函数签名

```shadow
double_to_str(d: double) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `d` | `double` | 双精度浮点 |

## 出参

- 类型：`string`
- 说明：字符串形式

## 示例

```shadow
let s = double_to_str(3.14159);
```
