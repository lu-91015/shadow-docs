---
layout: doc
title: "hashmap_contains"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_contains/
---

# `hashmap_contains`

**哈希表** 内置函数。

判断键是否存在。

## 函数签名

```shadow
hashmap_contains(map: dict, key: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `map` | `dict` | 字典 |
| `key` | `string` | 键 |

## 出参

- 类型：`int`
- 说明：存在为 1，否则 0

## 示例

```shadow
if (hashmap_contains(m, "k") == 1) { }
```
