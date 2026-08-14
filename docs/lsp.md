---
layout: doc
title: "LSP 语言服务器"
summary: "shadow 内置的 Language Server Protocol 3.17 服务器：启动方式、编辑器集成、117 项功能清单、命令行诊断与诊断协议。"
permalink: /lsp/
prev: /toolchain/
next: /install/
---

## 概述

shadow 0.5 把**语言服务器**作为编译器的一等公民内置在 `shadow` 可执行文件中。它由
`src/lsp/lsp.shadow`（约 130 KB）实现，完整复刻了 0.3 时代的 117 项 LSP 功能，遵循
**LSP 3.17** 规范，通过 **stdio 上的 JSON-RPC（Content-Length 分帧）** 与任何标准 LSP 客户端通信。

也就是说：你不需要额外安装语言服务器二进制——只要装好了 `shadow`（参见
[安装 shadow](/install/)），就能直接把编辑器接到 `shadow --lsp` 上获得语法高亮、
补全、悬停、跳转、引用、重命名、格式化、语义着色、内联提示、诊断等完整 IDE 体验。

> 编译器即库：`shadow` 的编译管线以库形式（`compile_api`）暴露，CLI 查询命令与 LSP
> 服务器共用同一套类型检查 / 符号索引 / 诊断代码，保证「编辑器里看到的」和「命令行编出来的」完全一致。

## 启动语言服务器

语言服务器以**长驻进程**方式运行，在标准输入读取 JSON-RPC 请求、在标准输出写回响应：

```bash
# 前台长驻（通常不由人直接调用，而是由编辑器的 LSP 客户端拉起）
shadow --lsp
```

- 通信协议：stdio + `Content-Length: N\r\n\r\n{json}` 标准 LSP 分帧。
- 生命周期：`initialize` → `initialized` → … → `shutdown` → `exit`。
- 文档同步：客户端通过 `textDocument/didOpen`、`textDocument/didChange`、
  `textDocument/didSave`、`textDocument/didClose` 维护内存中的文档版本。
- 标准库解析：LSP 同样走 `main_std_root` 机制——`import std.*` 从 `<shadow.exe>/../src/std`
  解析（安装后由安装器摆好，见[安装文档](/install/)）。因此只要在正确安装/仓库根环境下启动，
  标准库补全与跳转即开即用。

## 编辑器集成

`shadow --lsp` 说标准 LSP 3.17，所以**任何通用 LSP 客户端**都能直接连。客户端配置只需告诉它：
「启动命令 = `shadow`，参数 = `--lsp`」。下面是通用客户端配置示例（以 JSON 形式的客户端配置为例）：

```json
{
  "languageId": "shadow",
  "command": "shadow",
  "args": ["--lsp"],
  "filetypes": ["shadow"],
  "rootPatterns": ["shadow.sbg", ".git"],
  "settings": {}
}
```

> **关于官方 VSCode 扩展**：0.5 的 M6（生态完整）阶段规划了 `shadow-vscode` 风格扩展
> （`compilerPath` 指向 `shadow`、LSP 对接），目前**尚未随仓库发布**。在此之前，用任意
> 支持「自定义命令 LSP」的编辑器插件（如 VS Code 的通用 LSP 客户端、Neovim 的
> `lspconfig` + 外部服务器、Helix 的 `language-server` 配置）即可获得全部能力。

## 功能清单（117 项）

下表为 0.5 语言服务器复刻的功能类别与数量（逐项核对以 `develop` 文档 §3.6 为准）。

| 类别 | 功能数 | 关键能力 |
|------|--------|----------|
| 语法与编辑体验 | 6 | 高亮、括号匹配、自动缩进、折叠、注释切换、选区扩展 |
| 代码补全 | 13 | 函数 / 结构体 / 枚举 / 关键字 / 类型 / 成员 / 结构体字面量 / 局部变量 / **跨文件**补全、snippet、前缀过滤、sortText、completion/resolve、触发字符 |
| 悬停与签名 | 9 | Markdown 悬停、函数 / 结构体 / 枚举 / 变量悬停、文档注释提取、签名帮助、活跃参数追踪 |
| 跳转导航 | 7 | 定义 / 声明 / 类型定义 / 实现跳转、文档高亮、文档链接（四级回退路径解析） |
| 引用与重命名 | 3 | **跨文件**引用查找、**跨文件**重命名、prepareRename（关键字拦截） |
| 代码操作与透镜 | 11 | 快速修复（缺 return / 未定义变量 / 缺括号 / 类型转换）、codeAction/resolve、codeLens、executeCommand、applyEdit |
| 格式化 | 5 | 全文 / 范围 / 输入时 / 保存时格式化 + 配置（tabSize / insertSpaces） |
| 诊断 | 7 | **push + pull（LSP 3.17）**、工作区诊断、import 链诊断、版本追踪、refresh、配置（warnOnly / maxItems） |
| 语义着色 | 4 | full / delta（增量）/ range + refresh（多 token 类型） |
| 内联功能 | 5 | inlayHint（变量类型内联）、inlineCompletion（函数调用骨架）、inlineValue、resolve、refresh |
| 类型与调用层次 | 6 | prepareTypeHierarchy / supertypes / subtypes、prepareCallHierarchy / incomingCalls / outgoingCalls |
| 符号与导航 | 7 | documentSymbol、workspace/symbol（深度递归）、workspaceSymbol/resolve、foldingRange、selectionRange、documentHighlight |
| 颜色与联动 | 4 | documentColor（`#RGB`/`#RRGGBB`/`#RRGGBBAA`）、colorPresentation、linkedEditingRange、moniker |
| 文件操作 | 10 | will/did Create/Rename/Delete、原生文件监听、mtime 轮询、四级 import 路径解析、didChangeWatchedFiles |
| 工作区与进度 | 14 | 多根 workspaceFolders、配置拉取/推送、`$/progress`、`cancelRequest`、showMessage/Request、logMessage、showDocument、telemetry、setTrace/logTrace、4 种 refresh |
| SPK 包管理 | 6 | pack / unpack / list、SPK import 解析（幂等解包缓存）、SPK 依赖、SPK native 文件收集 |

### 支持的 LSP 方法（节选）

- **生命周期**：`initialize` / `initialized` / `shutdown` / `exit`
- **文档同步**：`textDocument/didOpen` / `didChange` / `didClose` / `didSave`，
  `workspace/didChangeConfiguration` / `didChangeWorkspaceFolders`
- **语言特性**：`hover`、`definition` / `declaration` / `typeDefinition` / `implementation`、
  `references`、`documentHighlight`、`documentSymbol`、`semanticTokens/full` / `range` / `full/delta`、
  `completion`（+`resolve`）、`signatureHelp`、`foldingRange`、`selectionRange`、`inlayHint`、
  `documentColor` / `colorPresentation`、`linkedEditingRange`、`moniker`、`formatting` /
  `rangeFormatting` / `onTypeFormatting`、`prepareRename` / `rename`、`codeAction`、`codeLens`、
  `inlineValue` / `inlineCompletion`、`diagnostic`（pull）、`prepareCallHierarchy` / `prepareTypeHierarchy`
- **工作区**：`workspace/diagnostic`、`workspace/symbol`、`workspace/executeCommand`
  （经 `workspace/applyEdit` 回写）

## 命令行诊断（离线等价，CI 友好）

除长驻 `--lsp` 外，`shadow` 还提供一组**一次性**命令行查询子命令，输出与 LSP 同源的诊断 /
符号信息。它们特别适合 CI、pre-commit 钩子，或不想起长驻服务器时做快速检查。

| 命令 | 作用 | 输出 |
|------|------|------|
| `shadow --diag-json <file>` | 机器可读诊断（LSP `publishDiagnostics` 等价） | 第 1 行：`sdiag` JSON 数组；加 `--refs` 时第 2 行输出顶层函数引用计数 `name\|count;...` |
| `shadow --diag-fast <file>` | 快诊断通道：仅 parse、跳过类型检查，复用 `--diag-json` 协议 | 同上（无 `--refs` 第二行） |
| `shadow --check <file>` | 人类可读编译统计 | stage / tokens / funcs / structs / 错误数 等 |
| `shadow --ranges <file>` | 语法区间 dump | 区间序列（供高亮/调试） |
| `shadow --at <file> <line> <col>` | 取某位置处的 AST 节点 | 节点描述（hover / 补全前缀上下文用） |
| `shadow --type-at <file> <line> <col>` | 取某位置处表达式的类型 | `type-at: <类型>` |

示例：

```bash
# 机器可读诊断（第 1 行 JSON 数组，第 2 行 refs 计数）
shadow --diag-json src/main.shadow --refs

# 快诊断（CI 里对单文件秒级检查，不需要类型检查）
shadow --diag-fast src/main.shadow

# 取 (12 行, 8 列) 处的类型
shadow --type-at src/main.shadow 12 8
```

> **机器可读模式细节**：`--diag-json` / `--diag-fast` 是给 LSP 异步 worker 消费的。它们**绝不**
> 把报错文本写进 stdout——读文件失败时只输出 `[]`，保证客户端不会把错误文本当 JSON 解析而断开连接。

## 诊断协议与区间模型

LSP 诊断遵循 **LSP-3 区间模型**：

- 范围以 `{start:{line,character}, end:{line,character}}` 表示，**0-based**（LSP 规范）。
- 编译器内部错误用 `file:line:col` 的 1-based 人类表示；导出给 LSP 时统一做 **1-based → 0-based**
  区间换算，使编辑器高亮精确落在出错字符上。
- 每条诊断含稳定字段：`range`、`severity`、`code`（稳定错误码）、`source`、`message`，
  与编辑器 Problems 面板 / `publishDiagnostics` 直接对应。
- 支持 **push**（`textDocument/publishDiagnostics`）与 **pull**（`textDocument/diagnostic` /
  `workspace/diagnostic`，LSP 3.17）两种模式，并带版本追踪，避免过期文档的诊断覆盖新文档。

## 性能与稳定性

- **长驻压测**：LSP 服务器连续处理 1000+ 文档编辑，内存稳定、无单调增长——依赖运行时 GC
  （分代 STW + 保守扫描）在长驻进程里周期性回收拼接产生的临时字符串。
- **增量诊断**：`--diag-fast` 只做 parse 做快速首个诊断；完整类型检查经 `--diag-json --refs`
  在后台子进程补全，不阻塞编辑器输入。
- **跨文件**：import 链、跨模块符号（含严格态跨包 `pub` 可见性规则）在跳转 / 引用 / 重命名中
  全程生效，与编译器语义一致。

## 已知限制 / 后续

- **官方 VSCode 扩展**尚未随仓库发布（见 M6 规划）；当前需用通用 LSP 客户端接入。
- 含 native 绑定的标准库包（`std.base64` / `std.net` / `std.https` 等带 `.c`）在编辑器内的
  语义着色/跳转已支持，但其 native 编译链路在 `--run` 时才触发（与语言服务器无关）。
- 诊断的 `maxItems` / `warnOnly` 等细粒度配置项已预留接口，具体客户端开关随扩展配套完善。
