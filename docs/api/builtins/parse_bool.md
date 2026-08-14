---
layout: doc
title: "parse_bool"
summary: "解析 · 内置函数"
permalink: /api/builtins/parse_bool/
---

# `parse_bool`

**解析** 内置函数。

将 "true"/"false" 等解析为 bool。

## 函数签名

```shadow
parse_bool(s: string) -> bool
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `s` | `string` | 布尔字符串 |

## 出参

- 类型：`bool`
- 说明：解析出的布尔值

## 示例

```shadow
let b = parse_bool("true");
```
