---
layout: doc
title: "long_to_str"
summary: "类型转换 · 内置函数"
permalink: /api/builtins/long_to_str/
---

# `long_to_str`

**类型转换** 内置函数。

将 long 转换为十进制字符串。

## 函数签名

```shadow
long_to_str(i: long) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `i` | `long` | 长整数 |

## 出参

- 类型：`string`
- 说明：十进制字符串

## 示例

```shadow
let s = long_to_str(9000000000L);
```
