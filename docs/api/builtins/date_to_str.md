---
layout: doc
title: "date_to_str"
summary: "日期时间 · 内置函数"
permalink: /api/builtins/date_to_str/
---

# `date_to_str`

**日期时间** 内置函数。

将 date 转为字符串。

## 函数签名

```shadow
date_to_str(d: date) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `d` | `date` | 日期 |

## 出参

- 类型：`string`
- 说明：字符串形式

## 示例

```shadow
let s = date_to_str(today());
```
