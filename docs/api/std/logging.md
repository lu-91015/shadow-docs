---
layout: doc
title: "标准库 · logging"
summary: "std.logging 包导出的公开函数。"
permalink: /api/std/logging/
---

# 标准库 · `std.logging`

本页列出 `std/logging` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.logging;` 引入，函数以顶层名直接调用。

## `log_set_level`

```shadow
log_set_level(lv: int) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `lv` | `int` |

**出参**：`void`

## `log_level`

```shadow
log_level() -> int
```

**出参**：`int`

## `log_debug`

```shadow
log_debug(s: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`void`

## `log_info`

```shadow
log_info(s: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`void`

## `log_warn`

```shadow
log_warn(s: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`void`

## `log_error`

```shadow
log_error(s: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`void`

## `log_at`

便捷：按显式级别发射（lv<0 视为 DEBUG，>=4 视为 ERROR）

```shadow
log_at(lv: int, s: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `lv` | `int` |
| `s` | `string` |

**出参**：`void`
