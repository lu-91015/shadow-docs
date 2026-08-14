---
layout: doc
title: "file_list_dir"
summary: "文件 · 内置函数"
permalink: /api/builtins/file_list_dir/
---

# `file_list_dir`

**文件** 内置函数。

列出目录条目，以分号分隔（可用 str_split 拆开）。

## 函数签名

```shadow
file_list_dir(path: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 目录路径 |

## 出参

- 类型：`string`
- 说明：分号分隔的目录条目列表

## 示例

```shadow
let items = str_split(file_list_dir("."), ";");
```
