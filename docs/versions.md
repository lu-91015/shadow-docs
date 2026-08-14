---
layout: doc
title: "shadow 版本"
summary: "所有发布版本与下载入口。当前最新稳定版：{{ site.shadow_version }}。"
permalink: /versions/
prev: /install/
next: /getting-started/
---

## 当前版本

当前最新稳定版本为 **shadow {{ site.shadow_version }}**。

<a class="btn btn-primary" href="https://github.com/{{ site.github_repo }}/releases/download/{{ site.shadow_version }}/shadow-{{ site.shadow_version }}-setup.exe">⬇ 下载 shadow {{ site.shadow_version }}（Windows，约 200 MB）</a>

安装与验证步骤见 [安装 shadow]({{ '/install/' | relative_url }})。

## 所有版本

下表列出 shadow 的全部发布版本。最新版以高亮标记。

<div class="versions-table-wrap">
<table class="versions-table">
  <thead>
    <tr>
      <th>版本</th>
      <th>渠道</th>
      <th>发布日期</th>
      <th>说明</th>
      <th>下载</th>
    </tr>
  </thead>
  <tbody>
  {% for v in site.data.versions %}
    <tr{% if v.latest %} class="is-latest"{% endif %}>
      <td>{% if v.latest %}<strong>{{ v.version }} · 最新</strong>{% else %}{{ v.version }}{% endif %}</td>
      <td>{{ v.channel | default: "stable" }}</td>
      <td>{{ v.date }}</td>
      <td>{{ v.notes }}</td>
      <td><a class="btn btn-sm btn-primary" href="{{ v.download }}">setup.exe</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

## 发布说明

{% for v in site.data.versions %}
### shadow {{ v.version }}{% if v.latest %} <span class="badge-latest">最新</span>{% endif %}

- **发布日期**：{{ v.date }}
- **渠道**：{{ v.channel | default: "stable" }}
- **说明**：{{ v.notes }}
- **下载**：<{{ v.download }}>

{% endfor %}

<div class="callout tip">
  <p class="callout-title">提示</p>
  <p>发版后只需更新 <code>_config.yml</code> 的 <code>shadow_version</code>，或在 <code>_data/versions.yml</code> 顶部追加一条（也可运行 <code>tools/sync_version.sh</code> 自动从编译器仓库同步最新 git tag）。全站下载链接会随之更新。</p>
</div>
