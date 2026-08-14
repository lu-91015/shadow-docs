---
layout: doc
title: "path_exists"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/path_exists/
---

# `path_exists`

**目录 / 路径** 内置函数。

判断任意路径（文件或目录）是否存在。

## 函数签名

```shadow
path_exists(path: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 路径 |

## 出参

- 类型：`int`
- 说明：存在为 1，否则 0

## 示例

```shadow
if (path_exists("a.txt") == 1) { }
```
