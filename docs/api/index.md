---
layout: doc
title: "库参考"
summary: "shadow 0.5 内置函数与标准库 API。"
permalink: /api/
prev: /modules/
next: /toolchain/
---

# 库参考

shadow 0.5 的程序可用两类函数：**内置函数**（由编译器直接提供、无需 import）与 **标准库**（`std.*` 包，需 `import`）。

## 内置函数

内置函数由编译器内建，调用前无需声明或导入。按类别列出：

### 输出

| 函数 | 签名 | 返回 |
|------|------|------|
| [`println`](/api/builtins/println/) | `println(args: ...) -> ()` | `()` |
| [`print`](/api/builtins/print/) | `print(args: ...) -> ()` | `()` |
| [`len`](/api/builtins/len/) | `len(x: any) -> int` | `int` |

### 类型转换

| 函数 | 签名 | 返回 |
|------|------|------|
| [`to_string`](/api/builtins/to_string/) | `to_string(x: any) -> string` | `string` |
| [`str`](/api/builtins/str/) | `str(x: any) -> string` | `string` |
| [`int_to_str`](/api/builtins/int_to_str/) | `int_to_str(i: int) -> string` | `string` |
| [`long_to_str`](/api/builtins/long_to_str/) | `long_to_str(i: long) -> string` | `string` |
| [`float_to_str`](/api/builtins/float_to_str/) | `float_to_str(f: float) -> string` | `string` |
| [`double_to_str`](/api/builtins/double_to_str/) | `double_to_str(d: double) -> string` | `string` |
| [`bool_to_str`](/api/builtins/bool_to_str/) | `bool_to_str(b: bool) -> string` | `string` |
| [`char_to_str`](/api/builtins/char_to_str/) | `char_to_str(c: char) -> string` | `string` |

### 数组

| 函数 | 签名 | 返回 |
|------|------|------|
| [`array_push`](/api/builtins/array_push/) | `array_push(arr: array<T>, elems: ...) -> array<T>` | `array<T>` |

### 字符串处理

| 函数 | 签名 | 返回 |
|------|------|------|
| [`substr2`](/api/builtins/substr2/) | `substr2(s: string, start: int, n: int) -> string` | `string` |
| [`str_replace`](/api/builtins/str_replace/) | `str_replace(s: string, from: string, to: string) -> string` | `string` |
| [`str_trim`](/api/builtins/str_trim/) | `str_trim(s: string) -> string` | `string` |
| [`str_to_upper`](/api/builtins/str_to_upper/) | `str_to_upper(s: string) -> string` | `string` |
| [`str_to_lower`](/api/builtins/str_to_lower/) | `str_to_lower(s: string) -> string` | `string` |
| [`str_char_at`](/api/builtins/str_char_at/) | `str_char_at(s: string, idx: int) -> string` | `string` |
| [`str_join`](/api/builtins/str_join/) | `str_join(parts: array<string>, sep: string) -> string` | `string` |
| [`str_format`](/api/builtins/str_format/) | `str_format(fmt: string, args: array<string>) -> string` | `string` |
| [`str_contains`](/api/builtins/str_contains/) | `str_contains(s: string, sub: string) -> int` | `int` |
| [`str_index_of`](/api/builtins/str_index_of/) | `str_index_of(s: string, sub: string) -> int` | `int` |
| [`str_starts_with`](/api/builtins/str_starts_with/) | `str_starts_with(s: string, prefix: string) -> int` | `int` |
| [`str_ends_with`](/api/builtins/str_ends_with/) | `str_ends_with(s: string, suffix: string) -> int` | `int` |
| [`str_split`](/api/builtins/str_split/) | `str_split(s: string, sep: string) -> array<string>` | `array<string>` |
| [`str_eq`](/api/builtins/str_eq/) | `str_eq(a: string, b: string) -> int` | `int` |

### 文件

| 函数 | 签名 | 返回 |
|------|------|------|
| [`file_read`](/api/builtins/file_read/) | `file_read(path: string) -> string` | `string` |
| [`file_write`](/api/builtins/file_write/) | `file_write(path: string, content: string) -> int` | `int` |
| [`file_exists`](/api/builtins/file_exists/) | `file_exists(path: string) -> int` | `int` |
| [`file_delete`](/api/builtins/file_delete/) | `file_delete(path: string) -> int` | `int` |
| [`file_list_dir`](/api/builtins/file_list_dir/) | `file_list_dir(path: string) -> string` | `string` |

### 目录 / 路径

| 函数 | 签名 | 返回 |
|------|------|------|
| [`dir_create`](/api/builtins/dir_create/) | `dir_create(path: string) -> int` | `int` |
| [`dir_delete`](/api/builtins/dir_delete/) | `dir_delete(path: string) -> int` | `int` |
| [`dir_exists`](/api/builtins/dir_exists/) | `dir_exists(path: string) -> int` | `int` |
| [`path_exists`](/api/builtins/path_exists/) | `path_exists(path: string) -> int` | `int` |
| [`path_join`](/api/builtins/path_join/) | `path_join(base: string, child: string) -> string` | `string` |
| [`path_dirname`](/api/builtins/path_dirname/) | `path_dirname(path: string) -> string` | `string` |
| [`path_basename`](/api/builtins/path_basename/) | `path_basename(path: string) -> string` | `string` |
| [`path_normalize`](/api/builtins/path_normalize/) | `path_normalize(path: string) -> string` | `string` |

### 哈希表

| 函数 | 签名 | 返回 |
|------|------|------|
| [`hashmap_new`](/api/builtins/hashmap_new/) | `hashmap_new() -> dict` | `dict` |
| [`hashmap_insert`](/api/builtins/hashmap_insert/) | `hashmap_insert(map: dict, key: string, value: string) -> int` | `int` |
| [`hashmap_get`](/api/builtins/hashmap_get/) | `hashmap_get(map: dict, key: string) -> string` | `string` |
| [`hashmap_contains`](/api/builtins/hashmap_contains/) | `hashmap_contains(map: dict, key: string) -> int` | `int` |
| [`hashmap_remove`](/api/builtins/hashmap_remove/) | `hashmap_remove(map: dict, key: string) -> int` | `int` |
| [`hashmap_size`](/api/builtins/hashmap_size/) | `hashmap_size(map: dict) -> int` | `int` |
| [`hashmap_free`](/api/builtins/hashmap_free/) | `hashmap_free(map: dict) -> int` | `int` |

### 集合

| 函数 | 签名 | 返回 |
|------|------|------|
| [`set_new`](/api/builtins/set_new/) | `set_new() -> set` | `set` |
| [`set_add`](/api/builtins/set_add/) | `set_add(set: set, value: string) -> int` | `int` |
| [`set_contains`](/api/builtins/set_contains/) | `set_contains(set: set, value: string) -> int` | `int` |
| [`set_remove`](/api/builtins/set_remove/) | `set_remove(set: set, value: string) -> int` | `int` |
| [`set_size`](/api/builtins/set_size/) | `set_size(set: set) -> int` | `int` |
| [`set_free`](/api/builtins/set_free/) | `set_free(set: set) -> int` | `int` |

### 日期时间

| 函数 | 签名 | 返回 |
|------|------|------|
| [`date_to_str`](/api/builtins/date_to_str/) | `date_to_str(d: date) -> string` | `string` |
| [`timestamp_to_str`](/api/builtins/timestamp_to_str/) | `timestamp_to_str(t: timestamp) -> string` | `string` |
| [`nanotimestamp_to_str`](/api/builtins/nanotimestamp_to_str/) | `nanotimestamp_to_str(t: nanotimestamp) -> string` | `string` |

### 压缩 / 哈希

| 函数 | 签名 | 返回 |
|------|------|------|
| [`zip_list`](/api/builtins/zip_list/) | `zip_list(spk: string) -> string` | `string` |
| [`content_hash`](/api/builtins/content_hash/) | `content_hash(path: string) -> string` | `string` |
| [`zip_pack`](/api/builtins/zip_pack/) | `zip_pack(src_dir: string, out_spk: string) -> int` | `int` |
| [`zip_unpack`](/api/builtins/zip_unpack/) | `zip_unpack(spk: string, out_dir: string) -> int` | `int` |

### 解析

| 函数 | 签名 | 返回 |
|------|------|------|
| [`parse_int`](/api/builtins/parse_int/) | `parse_int(s: string) -> int` | `int` |
| [`parse_long`](/api/builtins/parse_long/) | `parse_long(s: string) -> long` | `long` |
| [`parse_float`](/api/builtins/parse_float/) | `parse_float(s: string) -> double` | `double` |
| [`parse_bool`](/api/builtins/parse_bool/) | `parse_bool(s: string) -> bool` | `bool` |

## 标准库

标准库按包组织，使用 `import std.<pkg>;` 引入后，函数以顶层名调用。

| 包 | 说明 | 函数数 |
|----|------|--------|
| [`std.base64`](/api/std/base64/) | Base64 / Hex 编解码 | 4 |
| [`std.collections`](/api/std/collections/) | 集合、数组与常用算法 | 13 |
| [`std.http`](/api/std/http/) | HTTP 客户端 | 6 |
| [`std.https`](/api/std/https/) | HTTPS 客户端 | 4 |
| [`std.json`](/api/std/json/) | JSON 解析与构造 | 15 |
| [`std.logging`](/api/std/logging/) | 日志输出 | 7 |
| [`std.net`](/api/std/net/) | 网络（TCP / UDP） | 7 |
| [`std.reflect`](/api/std/reflect/) | 反射与元信息 | 14 |
| [`std.testkit`](/api/std/testkit/) | 测试框架 | 9 |
