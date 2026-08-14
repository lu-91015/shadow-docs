---
layout: doc
title: "str_format"
summary: "字符串处理 · 内置函数"
permalink: /api/builtins/str_format/
---

# `str_format`

**字符串处理** 内置函数。

按 {N} 占位符格式化；用 `{% raw %}{{% endraw %}` 与 `{% raw %}}{% endraw %}` 转义字面花括号；非法索引保留原样。

## 函数签名

```shadow
str_format(fmt: string, args: array<string>) -> string
```

## 入参

| 参数 | 类型 | 说明 |
|------|------|------|
| `fmt` | `string` | 含 {0}{1}… 占位符的模板 |
| `args` | `array<string>` | 占位符对应的实参 |

## 出参

- 类型：`string`
- 说明：格式化结果

## 示例

```shadow
let s = str_format("{0}+{1}", ["a", "b"]);  // "a+b"
```
