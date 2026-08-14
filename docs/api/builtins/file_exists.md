---
layout: doc
title: "file_exists"
summary: "文件 · 内置函数"
permalink: /api/builtins/file_exists/
---

# `file_exists`

**文件** 内置函数。

判断文件是否存在。

## 函数签名

```shadow
file_exists(path: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 文件路径 |

## 出参

- 类型：`int`
- 说明：存在为 1，否则 0

## 示例

```shadow
if (file_exists("a.txt") == 1) { }
```
