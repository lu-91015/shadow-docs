---
layout: doc
title: "dir_exists"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/dir_exists/
---

# `dir_exists`

**目录 / 路径** 内置函数。

判断目录是否存在。

## 函数签名

```shadow
dir_exists(path: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 目录路径 |

## 出参

- 类型：`int`
- 说明：存在为 1，否则 0

## 示例

```shadow
if (dir_exists("src") == 1) { }
```
