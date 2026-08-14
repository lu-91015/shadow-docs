---
layout: doc
title: "timestamp_to_str"
summary: "日期时间 · 内置函数"
permalink: /api/builtins/timestamp_to_str/
---

# `timestamp_to_str`

**日期时间** 内置函数。

将 timestamp 转为字符串。

## 函数签名

```shadow
timestamp_to_str(t: timestamp) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `t` | `timestamp` | 时间戳 |

## 出参

- 类型：`string`
- 说明：字符串形式

## 示例

```shadow
let s = timestamp_to_str(now());
```
