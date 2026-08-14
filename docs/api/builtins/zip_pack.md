---
layout: doc
title: "zip_pack"
summary: "压缩 / 哈希 · 内置函数"
permalink: /api/builtins/zip_pack/
---

# `zip_pack`

**压缩 / 哈希** 内置函数。

将目录打包为 .spk。

## 函数签名

```shadow
zip_pack(src_dir: string, out_spk: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `src_dir` | `string` | 源目录 |
| `out_spk` | `string` | 输出 .spk 路径 |

## 出参

- 类型：`int`
- 说明：成功为 0，失败为 -1

## 示例

```shadow
zip_pack("src", "out.spk");
```
