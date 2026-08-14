---
layout: doc
title: "print"
summary: "输出 · 内置函数"
permalink: /api/builtins/print/
---

# `print`

**输出** 内置函数。

向标准输出打印参数，自动按类型格式化，不追加换行。

## 函数签名

```shadow
print(args: ...) -> ()
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `args` | `...` | 任意类型，多个以空格分隔，不换行 |

## 出参

- 类型：`()`
- 说明：无返回值（unit）

## 示例

```shadow
print("loading");
```
