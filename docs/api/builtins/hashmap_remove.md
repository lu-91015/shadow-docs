---
layout: doc
title: "hashmap_remove"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_remove/
---

# `hashmap_remove`

**哈希表** 内置函数。

移除键值对。

## 函数签名

```shadow
hashmap_remove(map: dict, key: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `map` | `dict` | 字典 |
| `key` | `string` | 键 |

## 出参

- 类型：`int`
- 说明：成功为 0

## 示例

```shadow
hashmap_remove(m, "k");
```
