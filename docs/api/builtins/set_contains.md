---
layout: doc
title: "set_contains"
summary: "集合 · 内置函数"
permalink: /api/builtins/set_contains/
---

# `set_contains`

**集合** 内置函数。

判断元素是否在集合中。

## 函数签名

```shadow
set_contains(set: set, value: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `set` | `set` | 集合 |
| `value` | `string` | 元素 |

## 出参

- 类型：`int`
- 说明：存在为 1，否则 0

## 示例

```shadow
if (set_contains(s, "x") == 1) { }
```
