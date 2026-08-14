---
layout: doc
title: "标准库 · reflect"
summary: "std.reflect 包导出的公开函数。"
permalink: /api/std/reflect/
---

# 标准库 · `std.reflect`

本页列出 `std/reflect` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.reflect;` 引入，函数以顶层名直接调用。

## `reflect_int`

构造器：把标量包成带标签的 ReflectValue

```shadow
reflect_int(v: int) -> ReflectValue
```

**入参**

| 参数 | 类型 |
|------|------|
| `v` | `int` |

**出参**：`ReflectValue`

## `reflect_string`

```shadow
reflect_string(s: string) -> ReflectValue
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`ReflectValue`

## `reflect_bool`

```shadow
reflect_bool(b: int) -> ReflectValue
```

**入参**

| 参数 | 类型 |
|------|------|
| `b` | `int` |

**出参**：`ReflectValue`

## `reflect_long`

```shadow
reflect_long(l: long) -> ReflectValue
```

**入参**

| 参数 | 类型 |
|------|------|
| `l` | `long` |

**出参**：`ReflectValue`

## `reflect_any`

```shadow
reflect_any(a: any) -> ReflectValue
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `any` |

**出参**：`ReflectValue`

## `reflect_kind`

类型判定

```shadow
reflect_kind(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_is_int`

```shadow
reflect_is_int(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_is_string`

```shadow
reflect_is_string(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_is_bool`

```shadow
reflect_is_bool(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_is_long`

```shadow
reflect_is_long(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_get_int`

按类型取出（调用方需先确认 kind，否则类型不匹配会得到 0 / 空串）

```shadow
reflect_get_int(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_get_string`

```shadow
reflect_get_string(r: ReflectValue) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`string`

## `reflect_get_bool`

```shadow
reflect_get_bool(r: ReflectValue) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`int`

## `reflect_get_long`

```shadow
reflect_get_long(r: ReflectValue) -> long
```

**入参**

| 参数 | 类型 |
|------|------|
| `r` | `ReflectValue` |

**出参**：`long`
