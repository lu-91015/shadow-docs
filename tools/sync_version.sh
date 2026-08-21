#!/usr/bin/env bash
# =============================================================================
# sync_version.sh — 半自动同步 shadow 版本号到文档站
#
# 做什么：
#   1. 从 shadow 编译器仓库读取最新 git tag（或 GitHub Releases 最新一条）
#   2. 写回 _config.yml 的 shadow_version（全站下载链接的唯一来源）
#   3. 在 _data/versions.yml 顶部追加该版本条目，并把旧条的 latest 改为 false
#
# 为什么是「半自动」：
#   GitHub Pages 构建期既不能联网也不能跑自定义插件，无法在构建时自动识别版本。
#   因此由发版脚本/人工在发版时跑一次本脚本，把版本「固化」进仓库。
#
# 用法：
#   bash tools/sync_version.sh [shadow 仓库路径]
#   默认路径：../shadow-0.5（相对于本脚本所在目录）
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SHADOW_REPO="${1:-../shadow-0.5}"

# 从 _config.yml 读 github_repo（找不到则用默认值）
GH_REPO="$(grep -E '^github_repo:' "$DOCS_DIR/_config.yml" | sed -E 's/.*:[[:space:]]*"?(.*)"?$/\1/' || true)"
GH_REPO="${GH_REPO:-lu-91015/shadow}"

echo "→ 文档目录: $DOCS_DIR"
echo "→ 编译器仓库: $SHADOW_REPO"
echo "→ GitHub 仓库: $GH_REPO"

# ---- 1. 识别最新版本 tag ----
LATEST_TAG=""
if [ -d "$SHADOW_REPO/.git" ]; then
  LATEST_TAG="$(git -C "$SHADOW_REPO" describe --tags --abbrev=0 2>/dev/null || true)"
fi
if [ -z "$LATEST_TAG" ]; then
  LATEST_TAG="$(gh release list --repo "$GH_REPO" --limit 1 2>/dev/null | awk 'NR==1{print $1}' || true)"
fi
if [ -z "$LATEST_TAG" ]; then
  echo "✗ 无法从 $SHADOW_REPO 或 GitHub Releases 识别最新版本 tag" >&2
  exit 1
fi
echo "→ 识别到最新版本: $LATEST_TAG"

CONFIG="$DOCS_DIR/_config.yml"
VERSIONS="$DOCS_DIR/_data/versions.yml"

# ---- 2. 写回 _config.yml 的 shadow_version ----
sed -i -E "s/^(shadow_version:).*/\1 \"$LATEST_TAG\"/" "$CONFIG"
echo "→ 已更新 $CONFIG : shadow_version = \"$LATEST_TAG\""

# ---- 3. 更新 _data/versions.yml ----
if grep -q "version: \"$LATEST_TAG\"" "$VERSIONS"; then
  echo "→ $LATEST_TAG 已存在于 $VERSIONS（仅确保 latest 标记正确）"
  # 确保该条目是 latest，其余不是
  sed -i -E "s/^(  latest: )true/\1false/" "$VERSIONS"
  # 把匹配版本的 latest 行改回 true（按 version 行后紧跟的 latest 行处理）
  awk -v ver="$LATEST_TAG" '
    /^  version: "/ { in_block = (index($0, ver) > 0) }
    in_block && /^  latest: / { sub(/latest: .*/, "latest: true"); in_block = 0 }
    { print }
  ' "$VERSIONS" > "$VERSIONS.tmp" && mv "$VERSIONS.tmp" "$VERSIONS"
else
  # 旧版本 latest 全部置 false，再在顶部追加新条目
  sed -i -E "s/^(  latest: )true/\1false/" "$VERSIONS"
  WIN_URL="https://github.com/${GH_REPO}/releases/download/${LATEST_TAG}/shadow-${LATEST_TAG}-windows-x86_64.exe"
  LIN_URL="https://github.com/${GH_REPO}/releases/download/${LATEST_TAG}/shadow-${LATEST_TAG}-linux-x86_64.tar.gz"
  {
    echo "- version: \"$LATEST_TAG\""
    echo "  date: \"$(date +%Y-%m-%d)\""
    echo "  latest: true"
    echo "  channel: stable"
    echo "  notes: \"TODO: 填写 ${LATEST_TAG} 的发布说明\""
    echo "  downloads:"
    echo "    windows: \"$WIN_URL\""
    echo "    linux: \"$LIN_URL\""
    echo ""
  } | cat - "$VERSIONS" > "$VERSIONS.tmp" && mv "$VERSIONS.tmp" "$VERSIONS"
  echo "→ 已追加 $LATEST_TAG 到 $VERSIONS（请补全 notes 与历史版本的 latest 标记）"
fi

echo "完成。请运行 jekyll build 校验，再 git commit / git push。"
