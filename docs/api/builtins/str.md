---
layout: doc
title: "str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/str/
---

# `str`

**类型转换** 内置函数。

将任意值转换为字符串（to_string 的别名）。

## 函数签名

```shadow
str(x: any) -> string
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
let s = str(3.14);
```
