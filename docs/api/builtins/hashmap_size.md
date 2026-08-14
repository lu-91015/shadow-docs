---
layout: doc
title: "hashmap_size"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_size/
---

# `hashmap_size`

**哈希表** 内置函数。

返回字典大小。

## 函数签名

```shadow
hashmap_size(map: dict) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `map` | `dict` | 字典 |

## 出参

- 类型：`int`
- 说明：键值对数量

## 示例

```shadow
let n = hashmap_size(m);
```
