---
layout: doc
title: "file_write"
summary: "文件 · 内置函数"
permalink: /api/builtins/file_write/
---

# `file_write`

**文件** 内置函数。

将内容写入文件（覆盖）。

## 函数签名

```shadow
file_write(path: string, content: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 文件路径 |
| `content` | `string` | 写入内容 |

## 出参

- 类型：`int`
- 说明：成功为 0，失败为 -1

## 示例

```shadow
file_write("out.txt", "hi");
```
