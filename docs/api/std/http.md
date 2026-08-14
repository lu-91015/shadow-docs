---
layout: doc
title: "标准库 · http"
summary: "std.http 包导出的公开函数。"
permalink: /api/std/http/
---

# 标准库 · `std.http`

本页列出 `std/http` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.http;` 引入，函数以顶层名直接调用。

## `http_build_get`

构造 GET 请求报文字符串（同时供 http_get 内部与测试断言复用）

```shadow
http_build_get(url: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `url` | `string` |

**出参**：`string`

## `http_build_post`

构造 POST 请求报文字符串（含 Content-Length）

```shadow
http_build_post(url: string, body: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `url` | `string` |
| `body` | `string` |

**出参**：`string`

## `http_get`

http_get(url) -> 完整响应文本（空串表示连接失败）

```shadow
http_get(url: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `url` | `string` |

**出参**：`string`

## `http_post`

http_post(url, body) -> 完整响应文本（空串表示连接失败）

```shadow
http_post(url: string, body: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `url` | `string` |
| `body` | `string` |

**出参**：`string`

## `http_status`

从响应文本解析 HTTP 状态码（首行 "HTTP/1.1 200 OK" 的第二个 token）

```shadow
http_status(resp: string) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `resp` | `string` |

**出参**：`int`

## `http_body`

从响应文本提取 body（首个空行之后），兼容 \r\n\r\n 与 \n\n

```shadow
http_body(resp: string) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `resp` | `string` |

**出参**：`string`
