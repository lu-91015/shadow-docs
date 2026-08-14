---
layout: doc
title: "path_join"
summary: "目录 / 路径 · 内置函数"
permalink: /api/builtins/path_join/
---

# `path_join`

**目录 / 路径** 内置函数。

跨平台地拼接路径分量。

## 函数签名

```shadow
path_join(base: string, child: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `base` | `string` | 基础路径 |
| `child` | `string` | 子路径 |

## 出参

- 类型：`string`
- 说明：拼接后的路径

## 示例

```shadow
let p = path_join("a", "b.txt");  // "a/b.txt"
```
