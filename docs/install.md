---
layout: doc
title: "安装 shadow"
summary: "获取安装包、运行安装器、验证 shadow -run 与标准库，以及卸载。"
permalink: /install/
prev: /about/
next: /getting-started/
---

## 下载

<div class="callout note">
  <p class="callout-title">下载 shadow {{ site.shadow_version }}（Windows）</p>
  <p>
    <a class="btn btn-primary" href="https://github.com/{{ site.github_repo }}/releases/download/{{ site.shadow_version }}/shadow-{{ site.shadow_version }}-setup.exe">⬇ shadow-{{ site.shadow_version }}-setup.exe（约 200 MB）</a>
  </p>
  <p>离线自包含安装包：内置 LLVM 工具链与标准库，无需预装 VS / Windows SDK，<code>--run</code> 开箱即用。</p>
</div>

<div class="callout note">
  <p class="callout-title">下载 shadow VS Code 扩展 {{ site.vscode_version }}</p>
  <p>
    <a class="btn btn-primary" href="https://github.com/{{ site.vscode_repo }}/releases/download/{{ site.vscode_version }}/shadow-{{ site.vscode_version }}.vsix">⬇ shadow-{{ site.vscode_version }}.vsix</a>
  </p>
  <p>官方扩展：<strong>运行文件</strong>命令（<code>shadow.exe --run</code>）、基于 <code>cindex</code> 的符号索引（跳转 / 引用 / 重命名）与<strong>重建符号索引</strong>命令。在 VS Code 扩展视图选择「从 VSIX 安装…」并选中该文件即可（详见 <a href="{{ '/lsp/' | relative_url }}">LSP 与编辑器集成</a>）。</p>
</div>

## 概述

shadow {{ site.shadow_version }} 提供**自包含安装包** `shadow-{{ site.shadow_version }}-setup.exe`，安装后无需在目标机器上安装
Visual Studio 或 Windows SDK 即可编译并运行程序。安装包内已包含：

- shadow 编译器本体（`shadow.exe`）
- LLVM 最小工具链（`llc` / `clang++` / `lld-link` / `LLVM-C`）
- 静态 CRT（/MT）+ UCRT + 常用系统库（kernel32 / ws2_32 / …）
- 编译器内置 runtime（`runtime_lib.shadow`）
- 标准库全部包（`std.json` / `std.http` / `std.net` / …）

也就是说，`shadow xxx.shadow --run` 以及 `import std.*` 在装好后开箱即用。

## 运行安装器

双击 `shadow-{{ site.shadow_version }}-setup.exe`，按提示操作：

1. 安装器弹出确认框，说明将设置的环境变量。
2. 选择安装目录（默认 `%LOCALAPPDATA%\shadow`）。
3. 安装完成，弹出结果（含 `shadow --version` 冒烟测试结果）。

> 自动化 / 静默安装：
> ```bash
> shadow-{{ site.shadow_version }}-setup.exe --silent "C:\path\to\install"
> ```
> 结果写入 `%TEMP%\shadow_setup.log`，便于 CI 校验。

## 安装后的目录布局

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

## 环境变量

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

双击安装目录下的 `uninstall.cmd`：

1. 清除上述全部环境变量（`shadow` / `SHADOW_HOME` / `SHADOW_COMPILER` / `LLVM_HOME` / `LIB` / `Path` 中的相关项）。
2. 删除整个安装目录。

> 卸载后同样需要重新打开终端，环境变量修改才对新进程生效。

<div class="callout tip">
  <p class="callout-title">提示</p>
  <p>安装包为离线自包含：目标机器无需联网、无需预装 LLVM / VS / Windows SDK。<code>--run</code> 所需的全部工具链与库均已随包分发。</p>
</div>
