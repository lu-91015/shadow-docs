---
layout: doc
title: "dir_create"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/dir_create/
---

# `dir_create`

**目录 / 路径** 内置函数。

创建目录。

## 函数签名

```shadow
dir_create(path: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 目录路径 |

## 出参

- 类型：`int`
- 说明：成功为 0，失败为 -1

## 示例

```shadow
dir_create("build");
```
