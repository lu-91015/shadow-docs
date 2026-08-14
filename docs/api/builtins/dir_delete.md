---
layout: doc
title: "dir_delete"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/dir_delete/
---

# `dir_delete`

**目录 / 路径** 内置函数。

删除目录。

## 函数签名

```shadow
dir_delete(path: string) -> int
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
dir_delete("build");
```
