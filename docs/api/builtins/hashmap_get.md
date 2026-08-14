---
layout: doc
title: "hashmap_get"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_get/
---

# `hashmap_get`

**哈希表** 内置函数。

按键取值。

## 函数签名

```shadow
hashmap_get(map: dict, key: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `map` | `dict` | 字典 |
| `key` | `string` | 键 |

## 出参

- 类型：`string`
- 说明：键对应的值（不存在返回空串）

## 示例

```shadow
let v = hashmap_get(m, "k");
```
