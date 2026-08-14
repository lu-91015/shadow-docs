// shadow Language Docs - 站内搜索
// 纯前端：加载 /search.json 后在客户端做子串匹配，无外部依赖
(function () {
  'use strict';

  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  if (!input || !results) return;

  var cache = null;

  function load() {
    if (cache) return Promise.resolve(cache);
    return fetch('/search.json')
      .then(function (r) { return r.json(); })
      .then(function (d) { cache = d; return d; });
  }

  function norm(s) { return (s || '').toLowerCase(); }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function render(q) {
    q = q.trim();
    if (!q) { results.style.display = 'none'; results.innerHTML = ''; return; }
    load().then(function (data) {
      var toks = norm(q).split(/\s+/).filter(Boolean);
      var hits = data.filter(function (item) {
        var hay = norm(item.title + ' ' + item.summary + ' ' + item.text + ' ' + item.url);
        return toks.every(function (t) { return hay.indexOf(t) >= 0; });
      }).slice(0, 12);

      if (!hits.length) {
        results.innerHTML = '<li class="search-no-res">无匹配结果</li>';
        results.style.display = 'block';
        return;
      }
      results.innerHTML = hits.map(function (h) {
        var sum = h.summary
          ? '<span class="search-res-sum">' + escapeHtml(h.summary) + '</span>'
          : '';
        return '<li><a href="' + h.url + '">' + escapeHtml(h.title) + '</a>' + sum + '</li>';
      }).join('');
      results.style.display = 'block';
    }).catch(function () {
      results.innerHTML = '<li class="search-no-res">搜索索引加载失败</li>';
      results.style.display = 'block';
    });
  }

  input.addEventListener('input', function () { render(this.value); });
  input.addEventListener('focus', function () { if (this.value.trim()) render(this.value); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      var a = results.querySelector('a');
      if (a) window.location.href = a.getAttribute('href');
    } else if (e.key === 'Escape') {
      results.style.display = 'none';
      input.blur();
    }
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.search-wrap')) results.style.display = 'none';
  });
})();
