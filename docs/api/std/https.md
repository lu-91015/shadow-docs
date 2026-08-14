---
layout: doc
title: "标准库 · https"
summary: "std.https 包导出的公开函数。"
permalink: /api/std/https/
---

# 标准库 · `std.https`

本页列出 `std/https` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.https;` 引入，函数以顶层名直接调用。

## `https_get`

https_get(url) -> 完整响应文本（空串表示连接/TLS 失败）

```shadow
https_get(url: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `url` | `string` |

**出参**：`string`

## `https_post`

https_post(url, body) -> 完整响应文本（空串表示连接/TLS 失败）

```shadow
https_post(url: string, body: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `url` | `string` |
| `body` | `string` |

**出参**：`string`

## `https_status`

从响应文本解析 HTTP 状态码（首行 "HTTP/1.1 200 OK" 的第二个 token）

```shadow
https_status(resp: string) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `resp` | `string` |

**出参**：`int`

## `https_body`

从响应文本提取 body（首个空行之后），兼容 \r\n\r\n 与 \n\n

```shadow
https_body(resp: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `resp` | `string` |

**出参**：`string`
