---
layout: doc
title: "hashmap_insert"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_insert/
---

# `hashmap_insert`

**哈希表** 内置函数。

向字典插入键值对（覆盖已有键）。

## 函数签名

```shadow
hashmap_insert(map: dict, key: string, value: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `map` | `dict` | 字典 |
| `key` | `string` | 键 |
| `value` | `string` | 值 |

## 出参

- 类型：`int`
- 说明：成功为 0

## 示例

```shadow
hashmap_insert(m, "k", "v");
```
