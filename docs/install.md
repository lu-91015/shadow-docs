---
layout: doc
title: "安装 shadow"
summary: "获取安装包、运行安装器、验证 shadow -run 与标准库，以及卸载。"
permalink: /install/
prev: /about/
next: /getting-started/
---

{% assign latest = site.data.versions | where: "latest", true | first %}

## 下载

<div class="callout note">
  <p class="callout-title">下载 shadow {{ site.shadow_version }}（Windows · x86_64）</p>
  <p>
    {% assign win_name = latest.downloads.windows | split: "/" | last %}
    <a class="btn btn-primary" href="{{ latest.downloads.windows }}">⬇ {{ win_name }}</a>
  </p>
  <p>自包含 Windows 构建：内置 LLVM 工具链与标准库，无需预装 VS / Windows SDK，<code>--run</code> 开箱即用。</p>
</div>

<div class="callout note">
  <p class="callout-title">下载 shadow {{ site.shadow_version }}（Linux · x86_64）</p>
  <p>
    {% assign lin_name = latest.downloads.linux | split: "/" | last %}
    <a class="btn btn-primary" href="{{ latest.downloads.linux }}">⬇ {{ lin_name }}</a>
  </p>
  <p>自包含 Linux 构建：解压即可用，内置 LLVM 工具链与标准库，<code>--run</code> 开箱即用。</p>
</div>

## 概述

shadow {{ site.shadow_version }} 提供**自包含构建**，无需在目标机器上安装 Visual Studio、Windows SDK 或系统 LLVM 即可编译并运行程序。当前支持两大平台：

- **Windows · x86_64**：`shadow-{{ site.shadow_version }}-windows-x86_64.exe`
- **Linux · x86_64**：`shadow-{{ site.shadow_version }}-linux-x86_64.tar.gz`

构建内已包含：

- shadow 编译器本体（`shadow.exe` / `shadow`）
- LLVM 最小工具链（`llc` / `clang++` / `lld-link` / `LLVM-C`）
- 编译器内置 runtime（`runtime_lib.shadow`）
- 标准库全部包（`std.json` / `std.http` / `std.net` / …）

也就是说，`shadow xxx.shadow --run` 以及 `import std.*` 开箱即用。

## Windows 安装

### 运行安装器

双击 `shadow-{{ site.shadow_version }}-windows-x86_64.exe`，按提示操作：

1. 安装器弹出确认框，说明将设置的环境变量。
2. 选择安装目录（默认 `%LOCALAPPDATA%\shadow`）。
3. 安装完成，弹出结果（含 `shadow --version` 冒烟测试结果）。

> 自动化 / 静默安装：
> ```bash
> shadow-{{ site.shadow_version }}-windows-x86_64.exe --silent "C:\path\to\install"
> ```
> 结果写入 `%TEMP%\shadow_setup.log`，便于 CI 校验。

### 安装后的目录布局

```
<安装目录>/
├── bin/
│   ├── shadow.exe            # 编译器本体
│   ├── LLVM-C.dll            # 运行时（与 exe 同目录）
│   ├── rt/                   # 9 个系统调用层对象（--run 链接用）
│   └── bootstrap/miniz.o     # 压缩/自举辅助对象
├── llvm/                     # 内嵌 LLVM 工具链 + CRT/系统库
│   ├── bin/                  # llc.exe / clang++.exe / lld-link.exe
│   ├── lib/                  # LLVM-C.lib
│   └── crt/                  # libcmt / libucrt / kernel32 / ws2_32 / …
├── src/
│   ├── runtime/runtime_lib.shadow   # 编译器内置 runtime
│   └── std/                  # 标准库：iter.shadow + 全部真实包
│       ├── iter.shadow
│       ├── json/
│       ├── http/
│       └── …（base64 / collections / net / reflect / testkit / …）
└── uninstall.cmd             # 卸载脚本
```

### 环境变量

安装器会写入**用户级**环境变量（新开终端生效）：

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `shadow` | 安装目录 | 编译器根（约定俗成） |
| `SHADOW_HOME` | 安装目录 | 缓存/模块根、运行时定位基准 |
| `SHADOW_COMPILER` | `<安装目录>\bin\shadow.exe` | 显式指向编译器 |
| `LLVM_HOME` | `<安装目录>\llvm` | `--run` 链接时定位 `llc` / `clang++` |
| `LIB` | `<安装目录>\llvm\crt` | 链接器查找 CRT/系统库 |
| `Path` | 追加 `<安装目录>\bin` 与 `<安装目录>\llvm\bin` | 命令行直接调用 `shadow` |

> 若使用 IDE（如 VSCode），请在安装后**重新打开**终端/编辑器，使其继承新环境变量。

## Linux 安装

### 解压即用

下载 `shadow-{{ site.shadow_version }}-linux-x86_64.tar.gz` 后解压到任意目录，并把 `bin` 加入 `PATH`：

```bash
mkdir -p ~/shadow
tar -xzf shadow-{{ site.shadow_version }}-linux-x86_64.tar.gz -C ~/shadow --strip-components=1
export PATH="$HOME/shadow/bin:$PATH"
```

> 持久化：将上面的 `export PATH=...` 写入 `~/.bashrc`（或 `~/.zshrc` / `~/.profile`），新终端即可直接调用 `shadow`。

### 环境变量

建议导出以下变量（与 Windows 对应），便于 `--run` 链接与标准库定位：

| 变量 | 值 | 用途 |
| --- | --- | --- |
| `SHADOW_HOME` | 安装目录 | 缓存/模块根、运行时定位基准 |
| `SHADOW_COMPILER` | `<安装目录>/bin/shadow` | 显式指向编译器 |
| `LLVM_HOME` | `<安装目录>/llvm` | `--run` 链接时定位 `llc` / `clang++` |
| `LD_LIBRARY_PATH` | 追加 `<安装目录>/bin` 与 `<安装目录>/llvm/lib` | 运行期定位 `LLVM-C.so` |
| `PATH` | 追加 `<安装目录>/bin` 与 `<安装目录>/llvm/bin` | 命令行直接调用 `shadow` |

## 验证安装

### 1. 版本检查

```bash
shadow --version
```

### 2. 编译并运行（含标准库）

创建 `hello.shadow`：

```shadow
dsb hello;
import std.json;

kimo main() -> int {
    let o = std.json.json_parse_obj("{\"a\": 1, \"b\": 2}");
    println("std.json OK: a = " + int_to_str(std.json.json_get_int(o, "a")));
    return 0;
}
```

运行：

```bash
shadow hello.shadow --run
# 输出: std.json OK: a = 1
```

如果 `import std.*` 报 `not found`，通常是安装后未重启终端导致 `SHADOW_HOME` 未生效，
或安装目录被移动——重新打开终端，或重新运行安装器即可。

## 卸载

- **Windows**：双击安装目录下的 `uninstall.cmd`，清除上述全部环境变量并删除安装目录。
- **Linux**：删除安装目录，并从 shell 配置中移除相应的 `PATH` / `LD_LIBRARY_PATH` / `SHADOW_*` 导出。

> 卸载后同样需要重新打开终端，环境变量修改才对新进程生效。

<div class="callout tip">
  <p class="callout-title">提示</p>
  <p>安装包为离线自包含：目标机器无需联网、无需预装 LLVM / VS / Windows SDK。<code>--run</code> 所需的全部工具链与库均已随包分发。</p>
</div>
