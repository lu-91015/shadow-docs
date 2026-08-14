---
layout: doc
title: "bool_to_str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/bool_to_str/
---

# `bool_to_str`

**类型转换** 内置函数。

将 bool 转换为 "true"/"false"。

## 函数签名

```shadow
bool_to_str(b: bool) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `b` | `bool` | 布尔值 |

## 出参

- 类型：`string`
- 说明："true" 或 "false"

## 示例

```shadow
let s = bool_to_str(true);
```
