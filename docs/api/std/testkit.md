---
layout: doc
title: "标准库 · testkit"
summary: "std.testkit 包导出的公开函数。"
permalink: /api/std/testkit/
---

# 标准库 · `std.testkit`

本页列出 `std/testkit` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.testkit;` 引入，函数以顶层名直接调用。

## `test_reset`

```shadow
test_reset() -> void
```

**出参**：`void`

## `assert_eq_int`

```shadow
assert_eq_int(expected: int, actual: int, name: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `expected` | `int` |
| `actual` | `int` |
| `name` | `string` |

**出参**：`void`

## `assert_eq_str`

```shadow
assert_eq_str(expected: string, actual: string, name: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `expected` | `string` |
| `actual` | `string` |
| `name` | `string` |

**出参**：`void`

## `assert_true`

```shadow
assert_true(cond: int, name: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `cond` | `int` |
| `name` | `string` |

**出参**：`void`

## `assert_false`

```shadow
assert_false(cond: int, name: string) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `cond` | `int` |
| `name` | `string` |

**出参**：`void`

## `test_summary`

返回失败数（0 表示全部通过）

```shadow
test_summary() -> int
```

**出参**：`int`

## `bench_start`

用法：let t = bench_start(); <被测代码>; bench_report("name", bench_elapsed_ns(t));

```shadow
bench_start() -> long
```

**出参**：`long`

## `bench_elapsed_ns`

```shadow
bench_elapsed_ns(start: long) -> long
```

**入参**

| 参数 | 类型 |
|------|------|
| `start` | `long` |

**出参**：`long`

## `bench_report`

```shadow
bench_report(name: string, ns: long) -> void
```

**入参**

| 参数 | 类型 |
|------|------|
| `name` | `string` |
| `ns` | `long` |

**出参**：`void`
