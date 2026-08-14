---
layout: doc
title: "path_basename"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/path_basename/
---

# `path_basename`

**目录 / 路径** 内置函数。

返回路径的文件名部分。

## 函数签名

```shadow
path_basename(path: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 路径 |

## 出参

- 类型：`string`
- 说明：文件名

## 示例

```shadow
let f = path_basename("a/b.txt");  // "b.txt"
```
