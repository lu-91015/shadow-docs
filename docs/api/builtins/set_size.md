---
layout: doc
title: "set_size"
summary: "集合 · 内置函数"
permalink: /api/builtins/set_size/
---

# `set_size`

**集合** 内置函数。

返回集合大小。

## 函数签名

```shadow
set_size(set: set) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `set` | `set` | 集合 |

## 出参

- 类型：`int`
- 说明：元素数量

## 示例

```shadow
let n = set_size(s);
```
