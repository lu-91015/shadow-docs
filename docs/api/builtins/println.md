---
layout: doc
title: "println"
summary: "输出 · 内置函数"
permalink: /api/builtins/println/
---

# `println`

**输出** 内置函数。

向标准输出打印参数，自动按类型格式化并在末尾追加换行。

## 函数签名

```shadow
println(args: ...) -> ()
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `args` | `...` | 任意类型，多个以空格分隔，末尾换行 |

## 出参

- 类型：`()`
- 说明：无返回值（unit）

## 示例

```shadow
println("hello", 42, true);
```
