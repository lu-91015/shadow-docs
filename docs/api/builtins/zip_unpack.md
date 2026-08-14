---
layout: doc
title: "zip_unpack"
summary: "压缩 / 哈希 · 内置函数"
permalink: /api/builtins/zip_unpack/
---

# `zip_unpack`

**压缩 / 哈希** 内置函数。

将 .spk 包解包到目录。

## 函数签名

```shadow
zip_unpack(spk: string, out_dir: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `spk` | `string` | .spk 包路径 |
| `out_dir` | `string` | 解包目标目录 |

## 出参

- 类型：`int`
- 说明：成功为 0，失败为 -1

## 示例

```shadow
zip_unpack("x.spk", "out");
```
