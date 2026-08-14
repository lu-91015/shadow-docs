---
layout: doc
title: "hashmap_free"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_free/
---

# `hashmap_free`

**哈希表** 内置函数。

释放字典占用的内存。

## 函数签名

```shadow
hashmap_free(map: dict) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `map` | `dict` | 字典 |

## 出参

- 类型：`int`
- 说明：成功为 0

## 示例

```shadow
hashmap_free(m);
```
