---
layout: doc
title: "标准库 · net"
summary: "std.net 包导出的公开函数。"
permalink: /api/std/net/
---

# 标准库 · `std.net`

本页列出 `std/net` 包导出的全部公开函数（`pub kimo`）。
使用前通过 `import std.net;` 引入，函数以顶层名直接调用。

## `net_dial`

net_dial(host, port) -> handle（自动建 socket 并 connect；失败返回 -1）

```shadow
net_dial(host: string, port: int) -> long
```

**入参**

| 参数 | 类型 |
|------|------|
| `host` | `string` |
| `port` | `int` |

**出参**：`long`

## `net_send`

net_send(h, data) -> 已发送字节数（-1 失败）

```shadow
net_send(h: long, data: string) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `h` | `long` |
| `data` | `string` |

**出参**：`int`

## `net_recv`

net_recv(h, maxlen) -> string（单次接收，最多 maxlen 字节；空串表示关闭/错误）

```shadow
net_recv(h: long, maxlen: int) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `h` | `long` |
| `maxlen` | `int` |

**出参**：`string`

## `net_recv_all`

net_recv_all(h) -> string（持续接收直到对端关闭，用于 HTTP 等短连接）

```shadow
net_recv_all(h: long) -> string
```

**入参**

| 参数 | 类型 |
|------|------|
| `h` | `long` |

**出参**：`string`

## `net_close`

net_close(h) -> int（1 成功 / 0 失败）

```shadow
net_close(h: long) -> int
```

**入参**

| 参数 | 类型 |
|------|------|
| `h` | `long` |

**出参**：`int`

## `net_listen`

net_listen(port) -> server handle（-1 失败）

```shadow
net_listen(port: int) -> long
```

**入参**

| 参数 | 类型 |
|------|------|
| `port` | `int` |

**出参**：`long`

## `net_accept`

net_accept(server_h) -> client handle（-1 失败）

```shadow
net_accept(server_h: long) -> long
```

**入参**

| 参数 | 类型 |
|------|------|
| `server_h` | `long` |

**出参**：`long`
