---
layout: doc
title: "path_normalize"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/path_normalize/
---

# `path_normalize`

**目录 / 路径** 内置函数。

规范化路径（解析 . / .. 与冗余分隔符）。

## 函数签名

```shadow
path_normalize(path: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 路径 |

## 出参

- 类型：`string`
- 说明：规范化后的路径

## 示例

```shadow
let p = path_normalize("a/./b/../c");  // "a/c"
```
