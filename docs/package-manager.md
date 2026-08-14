---
layout: doc
title: "包管理（SPK）"
summary: "用 shadow -init 初始化项目、shadow.sbg 清单格式，以及 shadow pkg / pack / unpack / list 管理依赖与 .spk 包。"
permalink: /package-manager/
prev: /modules/
next: /api/
---

## 概述

shadow 用两种载体管理代码复用：

- **`shadow.sbg`** —— 项目 / 包清单（类 TOML 微格式），声明包名、版本与依赖。由 `shadow -init` 生成，编译与包管理都读它。
- **`.spk`** —— 源码包（zip 封装）。`shadow pack` 把目录打成 `.spk`，`shadow unpack` / `list` 读取其内容。

> **注意**：初始化命令是 **`shadow -init`**（带前导短横），**不是** `shadow init`。

## 初始化项目：shadow -init

```bash
shadow -init myapp        # 新建 myapp/ 目录并生成 myapp/shadow.sbg
shadow -init .            # 在当前目录直接生成 shadow.sbg
```

行为：

- 在目标目录生成 `shadow.sbg`；若已存在则报错退出（不会覆盖）。
- 目录不存在时会逐层创建。
- 包名取目录名（默认 `myapp`），版本 `0.1.0`，`abi_version = 1`，`[deps]` 为空。

## shadow.sbg 清单格式

```toml
[package]
name = "myapp"
version = "0.1.0"
abi_version = 1

[deps]
mylib = "./mylib"                  # 本地目录依赖
spkdemo = "./deps/spkdemo.spk"     # 本地 .spk 依赖
# remotelib = "remotelib"          # 远程模块（从 $SHADOW_REGISTRY 拉取）

[native]
# 库自带 native 源文件（.c）在此声明，编译 --run 时收集
```

| 节 | 字段 | 说明 |
|----|------|------|
| `[package]` | `name` | 包名（默认取目录名） |
| | `version` | 语义化版本 |
| | `abi_version` | ABI 版本号（当前固定 `1`） |
| `[deps]` | `name = "path"` | 依赖名 = 路径；支持本地目录、本地 `.spk`、远程模块名 |
| `[native]` | — | 库自带 native 源文件集合（编译期收集） |

依赖解析规则：

- **本地目录**（如 `"./mylib"`）：目录内含 `shadow.sbg` 即被识别为包。
- **本地 `.spk`**：相对路径指向的 `.spk` 文件，按需解包到版本化缓存。
- **远程模块**（仅写模块名，如 `"remotelib"`）：从 `$SHADOW_REGISTRY` 下载对应 `.spk`。

## 包管理命令

### shadow pkg list

```bash
shadow pkg list
```

- 若当前目录有 `shadow.sbg`：解析并展开 `[deps]`，逐行输出 `name  constraint=...  resolved=...  version=...`。
- 否则：列出 `$SHADOW_HOME/pkg/mod` 下已安装的包。
- 若既无 `shadow.sbg` 又未设 `SHADOW_HOME`：提示 `(no shadow.sbg and SHADOW_HOME unset)`。

### shadow pkg install

```bash
shadow pkg install                 # 按当前 shadow.sbg 的 [deps] 安装全部依赖
shadow pkg install mylib@1.2.3     # 安装指定包（必须带版本）
```

- **无参**：读取当前目录 `shadow.sbg`，本地可解析的依赖标记为 `present`（本地 `.spk` 解包进缓存），远程依赖从 registry 下载。
- **带参 `name@version`**：要求已设置 `SHADOW_REGISTRY`（registry 下载基址），从 `<SHADOW_REGISTRY>/<name>/@v/<version>.spk` 下载，解包到 `$SHADOW_HOME/pkg/mod/<name>@<version>`。
- 缓存目录结构对标 Go module cache：`$SHADOW_HOME/pkg/mod/<module>@<version>/`，按包内容 hash 做幂等戳（同版本号重打包也会刷新）。

### 环境变量

| 变量 | 用途 | 默认 |
|------|------|------|
| `SHADOW_REGISTRY` | 包 registry 下载基址，如 `https://example.com/mod`；`pkg install` 远程依赖必需 | 未设置则远程安装报错 |
| `SHADOW_HOME` | 缓存 / 模块根、运行时定位基准；未设时回退 `~/.shadow` | `~/.shadow` |

## SPK 工具链（底层）

`.spk` 是 zip 封装的源码包，可用顶层命令直接操作：

```bash
shadow pack <dir> <out.spk>        # 目录 → .spk（输出 content_hash）
shadow unpack <spk> <out_dir>      # .spk → 目录
shadow list <spk>                  # 列出 .spk 内条目
```

示例：

```bash
shadow pack ./mylib mylib.spk
shadow list mylib.spk
shadow unpack mylib.spk ./out
```

## 完整示例

```bash
# 1. 初始化项目
shadow -init myapp
cd myapp

# 2. 在 shadow.sbg 的 [deps] 声明一个本地依赖
#    [deps]
#    util = "./util"

# 3. 安装依赖（本地目录直接命中，远程走 registry）
shadow pkg install

# 4. 编译运行
shadow main.shadow --run
```

<div class="callout tip">
  <p class="callout-title">提示</p>
  <p>远程包安装依赖自建 registry：设置 <code>SHADOW_REGISTRY</code> 指向提供 <code>/&lt;name&gt;/@v/&lt;version&gt;.spk</code> 布局的 HTTP 服务。当前 <code>pkg</code> 仅提供 <code>list</code> 与 <code>install</code> 两个子命令。</p>
</div>
