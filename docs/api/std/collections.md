---
layout: doc
title: "标准库 · collections"
summary: "std.collections 包导出的公开函数。"
permalink: /api/std/collections/
---

# 标准库 · `std.collections`

本页列出 `std/collections` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.collections;` 引入，函数以顶层名直接调用。

## `set_new`

```shadow
set_new() -> StringSet
```

**出参**：`StringSet`

## `set_add`

返回更新后的集合（结构体按值传递，需重新赋值）

```shadow
set_add(s: StringSet, k: string) -> StringSet
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `StringSet` |
| `k` | `string` |

**出参**：`StringSet`

## `set_contains`

```shadow
set_contains(s: StringSet, k: string) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `StringSet` |
| `k` | `string` |

**出参**：`int`

## `set_remove`

```shadow
set_remove(s: StringSet, k: string) -> StringSet
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `StringSet` |
| `k` | `string` |

**出参**：`StringSet`

## `set_size`

```shadow
set_size(s: StringSet) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `StringSet` |

**出参**：`int`

## `set_keys`

```shadow
set_keys(s: StringSet) -> array<string>
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `StringSet` |

**出参**：`array<string>`

## `arr_sum_int`

```shadow
arr_sum_int(a: array<int>) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |

**出参**：`int`

## `arr_max_int`

```shadow
arr_max_int(a: array<int>) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |

**出参**：`int`

## `arr_min_int`

```shadow
arr_min_int(a: array<int>) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |

**出参**：`int`

## `arr_contains_int`

```shadow
arr_contains_int(a: array<int>, v: int) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |
| `v` | `int` |

**出参**：`int`

## `arr_find_int`

返回首次出现下标，无则 -1

```shadow
arr_find_int(a: array<int>, v: int) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |
| `v` | `int` |

**出参**：`int`

## `arr_sort_int`

升序排序（插入排序，返回新数组，不修改入参）

```shadow
arr_sort_int(a: array<int>) -> array<int>
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |

**出参**：`array<int>`

## `arr_reverse_int`

```shadow
arr_reverse_int(a: array<int>) -> array<int>
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<int>` |

**出参**：`array<int>`
