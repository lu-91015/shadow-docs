---
layout: doc
title: "str_index_of"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_index_of/
---

# `str_index_of`

**字符串处理** 内置函数。

返回 sub 在 s 中首次出现的下标。

## 函数签名

```shadow
str_index_of(s: string, sub: string) -> int
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 源字符串 |
| `sub` | `string` | 子串 |

## 出参

- 类型：`int`
- 说明：首次出现下标，未找到返回 -1

## 示例

```shadow
let i = str_index_of("abc", "b");  // 1
```
