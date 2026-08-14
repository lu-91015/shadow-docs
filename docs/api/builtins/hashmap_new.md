---
layout: doc
title: "hashmap_new"
summary: "哈希表 · 内置函数"
permalink: /api/builtins/hashmap_new/
---

# `hashmap_new`

**哈希表** 内置函数。

创建一个空字典。

## 函数签名

```shadow
hashmap_new() -> dict
```

## 入参

无参数。

## 出参

- 类型：`dict`
- 说明：空字典（字符串键 → 字符串值）

## 示例

```shadow
let m = hashmap_new();
```
