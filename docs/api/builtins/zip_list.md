---
layout: doc
title: "zip_list"
summary: "压缩 / 哈希 · 内置函数"
permalink: /api/builtins/zip_list/
---

# `zip_list`

**压缩 / 哈希** 内置函数。

列出 .spk 包内的条目。

## 函数签名

```shadow
zip_list(spk: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `spk` | `string` | .spk 包路径 |

## 出参

- 类型：`string`
- 说明：分号分隔的条目列表

## 示例

```shadow
let items = str_split(zip_list("x.spk"), ";");
```
