---
layout: doc
title: "set_remove"
summary: "集合 · 内置函数"
permalink: /api/builtins/set_remove/
---

# `set_remove`

**集合** 内置函数。

从集合移除元素。

## 函数签名

```shadow
set_remove(set: set, value: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `set` | `set` | 集合 |
| `value` | `string` | 元素 |

## 出参

- 类型：`int`
- 说明：成功为 0

## 示例

```shadow
set_remove(s, "x");
```
