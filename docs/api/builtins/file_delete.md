---
layout: doc
title: "file_delete"
summary: "文件 · 内置函数"
permalink: /api/builtins/file_delete/
---

# `file_delete`

**文件** 内置函数。

删除文件。

## 函数签名

```shadow
file_delete(path: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 文件路径 |

## 出参

- 类型：`int`
- 说明：成功为 0，失败为 -1

## 示例

```shadow
file_delete("a.txt");
```
