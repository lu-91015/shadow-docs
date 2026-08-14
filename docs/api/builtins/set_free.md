---
layout: doc
title: "set_free"
summary: "集合 · 内置函数"
permalink: /api/builtins/set_free/
---

# `set_free`

**集合** 内置函数。

释放集合占用的内存。

## 函数签名

```shadow
set_free(set: set) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `set` | `set` | 集合 |

## 出参

- 类型：`int`
- 说明：成功为 0

## 示例

```shadow
set_free(s);
```
