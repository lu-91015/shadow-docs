---
layout: doc
title: "类型系统"
summary: "字符串、数组、dict、set 容器的创建、操作与遍历。"
permalink: /types/
prev: /syntax/
next: /control-flow/
---

shadow 提供四类核心数据载体：`string`、`array<T>`、`dict<K,V>`、`set<T>`。它们的运行时操作通过内置函数族暴露（如 `str_*`、`hashmap_*`、`set_*`）。

## 字符串

字符串是不可变字节序列，用双引号字面量构造。

### 拼接

用 `+` 运算符拼接：

```shadow
let s = "hello" + " " + "world";   // "hello world"
```

### 运行时函数族

shadow 提供一组 `str_` 前缀的内置函数处理字符串：

```shadow
dsb cg_str_split_join_format;
kimo main() -> int {
    // str_split: 按分隔符切分，返回数组
    let parts = str_split("hello world", " ");
    println(len(parts));           // 2
    println(parts[0]);             // hello
    println(parts[1]);             // world

    // str_join: 用分隔符拼接数组
    let arr = ["hello", "world"];
    println(str_join(arr, ","));   // hello,world

    // str_format: 占位符格式化
    let args = ["Alice", "30"];
    println(str_format("Name: {0}, Age: {1}", args));
    // Name: Alice, Age: 30
    return 0;
}
```

| 函数 | 签名 | 说明 |
|------|------|------|
| `str_split(s, sep)` | `string -> array<string>` | 按分隔符切分 |
| `str_join(arr, sep)` | `array<string> -> string` | 用分隔符拼接 |
| `str_format(fmt, args)` | `string, array -> string` | `{0}`/`{1}` 占位符替换 |
| `len(s)` | `string -> int` | 字符串长度 |

## 数组 array&lt;T&gt;

数组是同类型元素的有序集合，用方括号字面量构造。

### 字面量与索引

```shadow
let data = [1, 2, 3];       // array<int>
println(data[0]);           // 1（读）
data[0] = 10;               // 写
println(len(data));         // 3（长度）
```

### 作为函数参数与返回值

数组可按泛型类型 `array<int>` 标注，作为参数传递或返回：

```shadow
dsb cg_array_fn;

kimo sum_array(arr: array<int>) -> int {
    let total = 0;
    let i = 0;
    while (i < len(arr)) {
        total = total + arr[i];
        i = i + 1;
    }
    return total;
}

kimo modify_array(arr: array<int>) -> array<int> {
    arr[0] = 10;
    return arr;
}

kimo main() -> int {
    let data = [1, 2, 3];
    let s = sum_array(data);
    println(to_string(s));              // 6
    let modified = modify_array(data);
    println(to_string(modified[0]));    // 10
    println(to_string(len(modified)));  // 3
    return 0;
}
```

### 遍历

用 `for (x in arr)` 迭代（详见[控制流]({{ "/control-flow/" | relative_url }})）：

```shadow
let arr = [1, 2, 3];
for (x in arr) {
    println(x);
}
```

<div class="callout note">
  <p class="callout-title">关于扩容</p>
  <p>0.5 提供内建 <code>array_push(arr, v)</code> 追加元素（返回新数组）。固定长度场景仍可用字面量 + 索引赋值。</p>
</div>

## dict&lt;K,V&gt;

`dict<K,V>` 是哈希映射，通过 `hashmap_*` 函数族操作。声明时用 `dict<string, string>` 等泛型标注。

### 创建、插入、遍历

```shadow
dsb cg_dict_for_iter;
kimo main() -> int {
    let d: dict<string, string> = hashmap_new();
    hashmap_insert(d, "hello", "world");
    hashmap_insert(d, "foo", "bar");

    // 单变量迭代 keys
    println("keys:");
    for (k in d) {
        println(k);
    }

    // 双变量迭代 keys + values
    println("values:");
    for (k, v in d) {
        println(v);
    }

    // 双变量配对输出
    println("pairs:");
    for (k, v in d) {
        print(k);
        print("=");
        println(v);
    }

    hashmap_free(d);
    return 0;
}
```

### 查找

```shadow
let d = hashmap_new();
hashmap_insert(d, "key", "value");
hashmap_contains(d, "key");   // 1（存在）
hashmap_get(d, "key");        // "value"
```

| 函数 | 说明 |
|------|------|
| `hashmap_new()` | 创建空 dict |
| `hashmap_insert(d, k, v)` | 插入/更新键值 |
| `hashmap_get(d, k)` | 取值 |
| `hashmap_contains(d, k)` | 是否存在（返回 0/1） |
| `hashmap_free(d)` | 释放（手动内存管理时使用） |

## set&lt;T&gt;

`set<T>` 是去重集合，通过 `set_*` 函数族操作。

### 创建、添加、判定、删除

```shadow
dsb cg_set_int_type;
kimo main() -> int {
    let s: set<int> = set_new();

    println(set_size(s));           // 0
    println(set_contains(s, 42));   // 0

    set_add(s, 42);
    set_add(s, 7);
    set_add(s, 42);                 // 重复，不增加 size

    println(set_contains(s, 42));   // 1
    println(set_contains(s, 100));  // 0
    println(set_size(s));           // 2（42 去重）

    println(set_remove(s, 42));     // 1（删除成功）
    println(set_contains(s, 42));   // 0
    println(set_size(s));           // 1

    set_free(s);
    return 0;
}
```

### 遍历

```shadow
let s: set<int> = set_new();
set_add(s, 1);
set_add(s, 2);
for (x in s) {
    println(x);
}
```

| 函数 | 说明 |
|------|------|
| `set_new()` | 创建空集合 |
| `set_add(s, v)` | 添加元素（自动去重） |
| `set_contains(s, v)` | 是否包含（返回 0/1） |
| `set_size(s)` | 元素个数 |
| `set_remove(s, v)` | 删除元素（返回 0/1） |
| `set_free(s)` | 释放 |

## 类型一览表

| 类型 | 字面量 | 操作函数族 | 遍历 |
|------|--------|-----------|------|
| `string` | `"..."` | `str_*`、`len` | — |
| `array<T>` | `[a, b, c]` | `len`、索引 | `for (x in arr)` |
| `dict<K,V>` | `hashmap_new()` | `hashmap_*` | `for (k in d)` / `for (k,v in d)` |
| `set<T>` | `set_new()` | `set_*` | `for (x in s)` |

## 下一步

- [控制流]({{ "/control-flow/" | relative_url }})：if / while / for 遍历详解。
- [函数与闭包]({{ "/functions/" | relative_url }})：把这些类型传给函数。
