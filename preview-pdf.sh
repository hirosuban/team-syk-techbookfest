#!/bin/bash
# PDFをDockerでビルドして、macのPreviewで開くところまでを1コマンドで行う。
#   ./preview-pdf.sh
# REVIEW_CONFIG_FILEを渡せば別configでもビルドできる（例: 電子書籍版）。
#   REVIEW_CONFIG_FILE=config-ebook.yml ./preview-pdf.sh
set -euo pipefail

cd "$(dirname "$0")"

[ -n "${REVIEW_CONFIG_FILE:-}" ] || REVIEW_CONFIG_FILE=config.yml
export REVIEW_CONFIG_FILE

# config.ymlのbooknameから出力PDFのパスを組み立てる
bookname=$(grep -E '^bookname:' "articles/${REVIEW_CONFIG_FILE}" | head -1 | sed -E 's/^bookname:[[:space:]]*//')
pdf="articles/${bookname}.pdf"

./build-in-docker.sh
open "$pdf"
