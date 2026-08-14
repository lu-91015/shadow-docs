---
layout: doc
title: "标准库 · json"
summary: "std.json 包导出的公开函数。"
permalink: /api/std/json/
---

# 标准库 · `std.json`

本页列出 `std/json` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.json;` 引入，函数以顶层名直接调用。

## `json_obj_new`

```shadow
json_obj_new() -> JsonObject
```

**出参**：`JsonObject`

## `json_parse_obj`

```shadow
json_parse_obj(text: string) -> JsonObject
```

**入参**

| 参数 | 类型 |
|------|------|
| `text` | `string` |

**出参**：`JsonObject`

## `json_parse_arr`

```shadow
json_parse_arr(text: string) -> array<string>
```

**入参**

| 参数 | 类型 |
|------|------|
| `text` | `string` |

**出参**：`array<string>`

## `json_set`

```shadow
json_set(o: JsonObject, key: string, rawJson: string) -> JsonObject
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |
| `key` | `string` |
| `rawJson` | `string` |

**出参**：`JsonObject`

## `json_get_str`

```shadow
json_get_str(o: JsonObject, key: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |
| `key` | `string` |

**出参**：`string`

## `json_get_int`

```shadow
json_get_int(o: JsonObject, key: string) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |
| `key` | `string` |

**出参**：`int`

## `json_get_bool`

```shadow
json_get_bool(o: JsonObject, key: string) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |
| `key` | `string` |

**出参**：`int`

## `json_get_obj`

```shadow
json_get_obj(o: JsonObject, key: string) -> JsonObject
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |
| `key` | `string` |

**出参**：`JsonObject`

## `json_get_arr`

```shadow
json_get_arr(o: JsonObject, key: string) -> array<string>
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |
| `key` | `string` |

**出参**：`array<string>`

## `json_arr_get_str`

数组元素访问（按索引）

```shadow
json_arr_get_str(a: array<string>, idx: int) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<string>` |
| `idx` | `int` |

**出参**：`string`

## `json_arr_get_int`

```shadow
json_arr_get_int(a: array<string>, idx: int) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<string>` |
| `idx` | `int` |

**出参**：`int`

## `json_arr_get_obj`

```shadow
json_arr_get_obj(a: array<string>, idx: int) -> JsonObject
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<string>` |
| `idx` | `int` |

**出参**：`JsonObject`

## `json_str`

序列化

```shadow
json_str(s: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `s` | `string` |

**出参**：`string`

## `json_encode_obj`

```shadow
json_encode_obj(o: JsonObject) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `o` | `JsonObject` |

**出参**：`string`

## `json_encode_arr`

```shadow
json_encode_arr(a: array<string>) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `a` | `array<string>` |

**出参**：`string`
