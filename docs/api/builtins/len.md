---
layout: doc
title: "len"
summary: "输出 · 内置函数"
permalink: /api/builtins/len/
---

# `len`

**输出** 内置函数。

返回容器或字符串的长度（字符数 / 元素数）。

## 函数签名

```shadow
len(x: any) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `x` | `any` | 数组 / 字符串 / 集合 / 字典等可度量长度的值 |

## 出参

- 类型：`int`
- 说明：元素个数

## 示例

```shadow
let n = len("abc");  // 3
```
