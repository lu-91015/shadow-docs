---
layout: doc
title: "错误处理"
summary: "try / catch / throw 结构化异常处理。"
permalink: /error-handling/
prev: /pattern-matching/
next: /modules/
---

shadow 提供结构化异常处理：`try` 包裹可能出错的代码，`throw` 抛出异常，`catch` 捕获并恢复。这与基于 `Result` 类型的方式互补——异常用于意外错误传播，`Result` 用于可预期的失败。

## 基本结构

```shadow
try {
    // 可能抛出异常的代码
} catch {
    // 异常发生时执行
}
```

### 示例

```shadow
dsb cg_try_catch_throw;

kimo main() -> int {
    let result = 0;
    try {
        throw "error";        // 抛出异常
        result = 1;           // 不会执行——throw 后控制流跳到 catch
    } catch {
        result = 99;          // 捕获后执行
    }
    println(result);          // 99
    return 0;
}
```

## throw

`throw expr;` 抛出一个异常值。`expr` 通常是字符串（错误信息），但也可为其他类型。

```shadow
throw "division by zero";
throw "file not found: " + path;
```

`throw` 之后的语句不会执行——控制流立即跳转到最近的 `catch`。

## catch

`catch { ... }` 块捕获 try 内抛出的异常并恢复执行。catch 块内可访问抛出的值（依实现而定），执行清理或返回默认值。

```shadow
kimo safe_div(a: int, b: int) -> int {
    try {
        if (b == 0) {
            throw "zero divisor";
        }
        return a / b;
    } catch {
        return -1;            // 出错时返回 -1
    }
}
```

## 控制流

```
try {
    A;
    throw "err";   ← 抛出
    B;             ← 跳过
} catch {
    C;             ← 执行
}
D;                 ← 继续执行
```

执行顺序：A → throw → (跳过 B) → C → D。

## 嵌套 try

内层 catch 不捕获时，异常向外层传播：

```shadow
kimo outer() -> int {
    try {
        inner();
    } catch {
        return 99;            // 捕获 inner 抛出的异常
    }
    return 0;
}

kimo inner() -> void {
    throw "from inner";       // 此函数无 try，异常上抛给调用方
}
```

## 与函数返回的交互

`throw` 会跳过函数的正常返回路径。若 try 块内所有路径都 throw，函数无需显式 return（控制流不会到达末尾）：

```shadow
kimo always_fail() -> int {
    try {
        throw "fatal";
    } catch {
        throw "re-thrown";    // catch 内再次 throw
    }
    // 永远不会到达这里
}
```

## 何时用异常 vs Result

| 场景 | 推荐 |
|------|------|
| 不可恢复的致命错误 | `throw` + 顶层 catch |
| 跨多层调用的错误传播 | `throw`（避免每层都处理） |
| 调用方应显式处理的预期失败 | `Result<T,E>` enum |
| 资源清理（如释放 dict/set） | 手动配对（GC 环境下多数可省略） |

<div class="callout note">
  <p class="callout-title">设计取舍</p>
  <p>shadow 同时支持异常与 <code>Result</code> 风格的 enum。文档建议：<strong>预期错误</strong>（如解析失败、查无此键）用 <code>Result</code> 让调用方显式处理；<strong>意外错误</strong>（如内存不足、不变量破坏）用异常。数据转换类代码建议优先 try/catch，参考 Rust 的错误处理哲学但保持 shadow 的简洁。</p>
</div>

## 完整示例

```shadow
dsb error_demo;

kimo parse_int(s: string) -> int {
    try {
        // 假设 to_int 在无效输入时抛出
        return to_int(s);
    } catch {
        return 0;             // 解析失败返回 0
    }
}

kimo main() -> int {
    let a = parse_int("42");
    let b = parse_int("abc");
    println(a);               // 42
    println(b);               // 0（异常被 catch）
    return 0;
}
```

## 下一步

- [模块系统]({{ "/modules/" | relative_url }})：组织多文件项目，跨模块复用错误类型。
- [库参考]({{ "/api/" | relative_url }})：内置函数的错误行为约定。
