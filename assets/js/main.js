// shadow Language Docs - 前端交互
// 仅在浏览器原生运行，无外部依赖
(function () {
  'use strict';

  // ===== 1. 导航当前页高亮 =====
  // 根据当前 URL 路径匹配 nav 链接，标记 active
  function highlightNav() {
    var path = window.location.pathname.replace(/\.html$/, '').replace(/\/index$/, '/');
    if (path === '') path = '/';
    var links = document.querySelectorAll('.nav-list a');
    links.forEach(function (link) {
      var href = link.getAttribute('href');
      if (!href) return;
      // 移除 relative_url 前缀的 base
      var target = href.replace(/\.html$/, '').replace(/\/index$/, '/');
      if (target === '') target = '/';
      if (target === path) {
        link.classList.add('active');
      }
    });
  }

  // ===== 2. 代码块“复制”按钮 =====
  function addCopyButtons() {
    var blocks = document.querySelectorAll('pre, .highlight pre');
    blocks.forEach(function (pre) {
      // 避免重复添加
      if (pre.parentNode.classList.contains('highlight') && pre.parentNode.querySelector('.copy-btn')) return;
      if (pre.querySelector('.copy-btn')) return;

      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.type = 'button';
      btn.setAttribute('aria-label', '复制代码');
      btn.textContent = '复制';
      btn.style.cssText = [
        'position:absolute',
        'top:8px',
        'right:8px',
        'padding:4px 10px',
        'font-size:12px',
        'font-family:inherit',
        'background:var(--bg-muted)',
        'color:var(--text-soft)',
        'border:1px solid var(--border)',
        'border-radius:5px',
        'cursor:pointer',
        'opacity:0',
        'transition:opacity .15s, background .15s'
      ].join(';');

      // 让父容器成为定位上下文
      var wrapper = pre.parentNode.classList.contains('highlight') ? pre.parentNode : pre;
      wrapper.style.position = wrapper.style.position || 'relative';
      wrapper.appendChild(btn);

      wrapper.addEventListener('mouseenter', function () { btn.style.opacity = '1'; });
      wrapper.addEventListener('mouseleave', function () { btn.style.opacity = '0'; });

      btn.addEventListener('click', function () {
        var text = pre.innerText || pre.textContent;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () { flash(btn, '已复制'); });
        } else {
          // fallback
          var ta = document.createElement('textarea');
          ta.value = text;
          ta.style.position = 'fixed';
          ta.style.left = '-9999px';
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); flash(btn, '已复制'); } catch (e) {}
          document.body.removeChild(ta);
        }
      });
    });
  }
  function flash(btn, msg) {
    var orig = btn.textContent;
    btn.textContent = msg;
    btn.style.background = 'var(--brand-50)';
    btn.style.color = 'var(--brand-600)';
    setTimeout(function () {
      btn.textContent = orig;
      btn.style.background = '';
      btn.style.color = '';
    }, 1400);
  }

  // ===== 3. 外链新窗口打开 =====
  function externalLinks() {
    var links = document.querySelectorAll('a[href^="http"]');
    links.forEach(function (a) {
      if (a.host !== window.location.host) {
        a.setAttribute('target', '_blank');
        a.setAttribute('rel', 'noopener noreferrer');
      }
    });
  }

  // ===== 4. 移动端菜单点击外关闭 =====
  function navOutsideClick() {
    var toggle = document.getElementById('nav-toggle');
    var nav = document.querySelector('.site-nav');
    if (!toggle || !nav) return;
    document.addEventListener('click', function (e) {
      if (!toggle.checked) return;
      if (!nav.contains(e.target)) toggle.checked = false;
    });
  }

  // ===== 5. 滚动时为 header 增加阴影 =====
  function headerShadow() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var onScroll = function () {
      if (window.scrollY > 4) header.style.boxShadow = 'var(--shadow-sm)';
      else header.style.boxShadow = 'none';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ===== 6. 目录侧边栏滚动高亮（scroll-spy）=====
  function tocScrollSpy() {
    var toc = document.querySelector('.doc-toc .section-nav');
    if (!toc) return;
    var links = Array.prototype.slice.call(toc.querySelectorAll('a'));
    if (!links.length) return;
    var map = {};
    links.forEach(function (a) {
      var id = a.getAttribute('href');
      if (id && id.charAt(0) === '#') map[id.slice(1)] = a;
    });
    var heads = Object.keys(map)
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);

    function onScroll() {
      var pos = window.scrollY + 100;
      var current = null;
      heads.forEach(function (h) {
        if (h.offsetTop <= pos) current = h.id;
      });
      links.forEach(function (a) { a.classList.remove('is-active'); });
      if (current && map[current]) map[current].classList.add('is-active');
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ===== 启动 =====
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    highlightNav();
    addCopyButtons();
    externalLinks();
    navOutsideClick();
    headerShadow();
    tocScrollSpy();
  });
})();
