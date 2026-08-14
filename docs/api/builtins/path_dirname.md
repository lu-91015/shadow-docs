---
layout: doc
title: "path_dirname"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/path_dirname/
---

# `path_dirname`

**目录 / 路径** 内置函数。

返回路径的目录部分。

## 函数签名

```shadow
path_dirname(path: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 路径 |

## 出参

- 类型：`string`
- 说明：父目录

## 示例

```shadow
let d = path_dirname("a/b.txt");  // "a"
```
