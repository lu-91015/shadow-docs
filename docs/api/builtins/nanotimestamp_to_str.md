---
layout: doc
title: "nanotimestamp_to_str"
summary: "日期时间 · 内置函数"
permalink: /api/builtins/nanotimestamp_to_str/
---

# `nanotimestamp_to_str`

**日期时间** 内置函数。

将 nanotimestamp 转为字符串。

## 函数签名

```shadow
nanotimestamp_to_str(t: nanotimestamp) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `t` | `nanotimestamp` | 纳秒时间戳 |

## 出参

- 类型：`string`
- 说明：字符串形式

## 示例

```shadow
let s = nanotimestamp_to_str(now_ns());
```
