#!/usr/bin/env python3
"""把 Markdown 正文里的根相对链接 ](/path) 改写为 ]({{ "/path" | relative_url }})。

Jekyll 会在 Markdown 渲染前先解析 Liquid，因此 relative_url 能自动带上 site.baseurl，
修复 GitHub Pages 子路径（/shadow-docs）下裸根链接 404 的问题。

- 只处理以 / 开头的根相对链接，不动 http(s) 外链，也不动 ./ ../ 相对链接。
- 已经写成 Liquid 的链接 (]({{) 不会重复处理。
- 不处理 _site 目录。
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 需要扫描的目录：仓库根目录的 .md 与 docs/ 下所有 .md
SCAN_DIRS = [ROOT, os.path.join(ROOT, "docs")]

LINK_RE = re.compile(r'\]\((/[^)]+)\)')


def transform(text):
    return LINK_RE.sub(lambda m: ']({{ "%s" | relative_url }})' % m.group(1), text)


def main():
    changed = 0
    total = 0
    for base in SCAN_DIRS:
        for dirpath, dirnames, filenames in os.walk(base):
            if "_site" in dirpath.split(os.sep):
                continue
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                path = os.path.join(dirpath, fn)
                with open(path, "r", encoding="utf-8") as f:
                    src = f.read()
                new = transform(src)
                if new != src:
                    n = len(LINK_RE.findall(src))
                    total += n
                    changed += 1
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new)
                    rel = os.path.relpath(path, ROOT)
                    print("  %3d  %s" % (n, rel))
    print("替换文件数: %d, 替换链接数: %d" % (changed, total))


if __name__ == "__main__":
    main()
