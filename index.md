---
layout: default
title: "shadow — 粉丝向语言"
description: "shadow 是一门原生 LLVM 后端、内建 trait/impl、模式匹配与泛型的粉丝向语言（v0.5）。"
---

<section class="hero">
  <span class="badge">v{{ site.shadow_version }} · 编译管线完整自举</span>
  <h1>用 <span class="accent">shadow</span> 写粉丝向代码</h1>
  <p class="tagline">
    shadow 是一门原生 LLVM 后端、内建 trait/impl、模式匹配与泛型的粉丝向语言。
    语法简洁，类型严格，编译期保证内存安全。
  </p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="https://github.com/{{ site.github_repo }}/releases/download/{{ site.shadow_version }}/shadow-{{ site.shadow_version }}-setup.exe">⬇ 下载 shadow {{ site.shadow_version }}</a>
    <a class="btn btn-secondary" href="https://github.com/{{ site.vscode_repo }}/releases/download/{{ site.vscode_version }}/shadow-{{ site.vscode_version }}.vsix">VS Code 扩展 ⬇</a>
    <a class="btn btn-secondary" href="{{ '/getting-started/' | relative_url }}">快速开始 →</a>
    <a class="btn btn-secondary" href="{{ '/versions/' | relative_url }}">历史版本</a>
  </div>

  <div class="hero-preview">
    <div class="code-card">
      <div class="code-card-header">
        <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
        <span class="filename">hello.shadow</span>
      </div>
{% highlight shadow %}
dsb hello;

kimo main() -> int {
    let name = "shadow";
    println("Hello, " + name + "!");

    // 模式匹配 + 枚举载荷
    let opt = Some(42);
    let v = match opt {
        Some(x) => x,
        None    => 0,
    };
    println(v);
    return 0;
}
{% endhighlight %}
    </div>
  </div>
</section>

<section class="features">
  <div class="feature-card">
    <div class="icon">LL</div>
    <h3>原生 LLVM 后端</h3>
    <p>直接生成 LLVM IR，复用成熟的优化与目标平台支持，性能对标 C/C++。</p>
  </div>
  <div class="feature-card">
    <div class="icon">{ }</div>
    <h3>trait / impl 系统</h3>
    <p>基于 trait 与 impl 的抽象，零成本静态分发，支持泛型约束与多态。</p>
  </div>
  <div class="feature-card">
    <div class="icon">⇄</div>
    <h3>并发与任务</h3>
    <p>spawn 派生任务、async/await 协程（测试中，见路线图）。</p>
  </div>
  <div class="feature-card">
    <div class="icon">≡</div>
    <h3>模式匹配</h3>
    <p>强大的 match 表达式，支持枚举载荷解构、字面量匹配与通配符。</p>
  </div>
  <div class="feature-card">
    <div class="icon">T</div>
    <h3>泛型与类型推导</h3>
    <p>完整的泛型系统（enum&lt;T&gt;、array&lt;T&gt;、dict&lt;K,V&gt;），let 绑定自动推导。</p>
  </div>
  <div class="feature-card">
    <div class="icon">⌘</div>
    <h3>模块与可见性</h3>
    <p>dsb 声明模块，import 跨文件复用，pub 精确控制导出边界。</p>
  </div>
  <div class="feature-card">
    <div class="icon">!</div>
    <h3>结构化错误处理</h3>
    <p>try / catch / throw 三件套，配合 Result 风格的类型安全返回。</p>
  </div>
  <div class="feature-card">
    <div class="icon">λ</div>
    <h3>一等闭包</h3>
    <p>kimo 字面量定义闭包，自动捕获环境变量，可作为参数与返回值传递。</p>
  </div>
  <div class="feature-card">
    <div class="icon">⎈</div>
    <h3>自举编译器</h3>
    <p>编译器由 shadow 自身实现并自举：shadow-0.5 的 shadow.exe 编译自身源码达到 fixed-point。</p>
  </div>
</section>

<footer class="home-footer">
  <p>作者 · 李豆沙 &nbsp;·&nbsp; <a href="https://space.bilibili.com/1703797642" target="_blank" rel="noopener">哔哩哔哩主页 ↗</a></p>
</footer>
