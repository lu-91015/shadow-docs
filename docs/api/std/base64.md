---
layout: doc
title: "标准库 · base64"
summary: "std.base64 包导出的公开函数。"
permalink: /api/std/base64/
---

# 标准库 · `std.base64`

本页列出 `std/base64` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.base64;` 引入，函数以顶层名直接调用。

## `base64_encode`

```shadow
base64_encode(s: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`string`

## `base64_decode`

```shadow
base64_decode(s: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`string`

## `hex_encode`

```shadow
hex_encode(s: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`string`

## `hex_decode`

```shadow
hex_decode(s: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`string`
