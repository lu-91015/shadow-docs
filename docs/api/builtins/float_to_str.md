---
layout: doc
title: "float_to_str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/float_to_str/
---

# `float_to_str`

**类型转换** 内置函数。

将 float 转换为字符串。

## 函数签名

```shadow
float_to_str(f: float) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `f` | `float` | 单精度浮点 |

## 出参

- 类型：`string`
- 说明：字符串形式

## 示例

```shadow
let s = float_to_str(1.5f);
```
