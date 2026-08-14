---
layout: doc
title: "file_read"
summary: "文件 · 内置函数"
permalink: /api/builtins/file_read/
---

# `file_read`

**文件** 内置函数。

读取文本文件的全部内容。

## 函数签名

```shadow
file_read(path: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 文件路径 |

## 出参

- 类型：`string`
- 说明：文件全部内容（读取失败返回空串）

## 示例

```shadow
let src = file_read("main.shadow");
```
