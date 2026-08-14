---
layout: doc
title: "content_hash"
summary: "压缩 / 哈希 · 内置函数"
permalink: /api/builtins/content_hash/
---

# `content_hash`

**压缩 / 哈希** 内置函数。

计算文件内容的哈希（十六进制字符串）。

## 函数签名

```shadow
content_hash(path: string) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `path` | `string` | 文件路径 |

## 出参

- 类型：`string`
- 说明：十六进制内容哈希

## 示例

```shadow
let h = content_hash("x.spk");
```
