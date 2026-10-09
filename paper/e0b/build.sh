#!/usr/bin/env bash
# Build the Sīdus E0-B paper with pandoc + XeLaTeX.
#   ./build.sh                       preview with a watermark, written to $OUT (default /tmp/sidus-e0b-paper)
#   ./build.sh 10.5281/zenodo.NNNN   release: writes downloads/Sidus_E0B_Research_Paper.{md,pdf} and,
#                                    the first time only, keeps the 8 Oct 2026 version in downloads/archive/
# Needs: pandoc 3, XeLaTeX (titlesec, fancyhdr, tcolorbox, caption, draftwatermark, lmodern), and the fonts
# Noto Serif (+ ExtraBold), Lato, Latin Modern Math, DejaVu Sans Mono.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd); ROOT=$(cd "$HERE/../.." && pwd)
DOI=${1:-}; OUT=${OUT:-${TMPDIR:-/tmp}/sidus-e0b-paper}
ORIG_PDF=6b10e20f38961b0cbaa7a162e62749e918a3b1fd39be10fe83ac654728121c3a
ORIG_MD=d6c3e5d6eefb7a83edc88cbb89d4324c65775691a500632c3e17215332da44dc
sha() { if command -v sha256sum >/dev/null; then sha256sum "$1"; else shasum -a 256 "$1"; fi | cut -d' ' -f1; }
if [ -z "$DOI" ]; then
  SUB=10.5281/zenodo.PENDING
  MARK=(-V 'header-includes=\usepackage{draftwatermark}\SetWatermarkText{PREVIEW: DOI PENDING}\SetWatermarkScale{0.45}\SetWatermarkColor[gray]{0.9}')
else
  [[ "$DOI" =~ ^10\.5281/zenodo\.[0-9]+$ ]] || { echo "DOI must look like 10.5281/zenodo.1234567" >&2; exit 1; }
  SUB=$DOI; MARK=()
fi
rm -rf "$OUT"; mkdir -p "$OUT"; cp -r "$HERE/assets" "$OUT/"
sed "s#ZENODO_DOI#$SUB#g" "$HERE/Sidus_E0B_Research_Paper.source.md" > "$OUT/Sidus_E0B_Research_Paper.md"
(cd "$OUT" && pandoc Sidus_E0B_Research_Paper.md -f markdown -o Sidus_E0B_Research_Paper.pdf --pdf-engine=xelatex \
   -H "$HERE/header.tex" "${MARK[@]}" -V documentclass=article -V fontsize=10pt -V papersize=letter \
   -V geometry:left=60pt,right=60pt,top=55.4pt,bottom=54pt,headheight=12pt,headsep=19.4pt,footskip=26.5pt) 2> "$OUT/build.log" \
   || { cat "$OUT/build.log" >&2; exit 1; }
if grep -q "Missing character" "$OUT/build.log"; then grep "Missing character" "$OUT/build.log" >&2; exit 1; fi
if grep -q ZENODO_DOI "$OUT/Sidus_E0B_Research_Paper.md"; then echo "unsubstituted DOI token" >&2; exit 1; fi
echo "built $OUT/Sidus_E0B_Research_Paper.pdf (DOI $SUB)"
if [ -n "$DOI" ]; then
  mkdir -p "$ROOT/downloads/archive"
  for ext in md pdf; do
    keep="$ROOT/downloads/archive/Sidus_E0B_Research_Paper_2026-10-08.$ext"; cur="$ROOT/downloads/Sidus_E0B_Research_Paper.$ext"
    if [ ! -e "$keep" ]; then
      want=$([ "$ext" = pdf ] && echo $ORIG_PDF || echo $ORIG_MD)
      [ "$(sha "$cur")" = "$want" ] || { echo "$cur is not the 8 Oct original; refusing to archive it" >&2; exit 1; }
      cp "$cur" "$keep"
    fi
    cp "$OUT/Sidus_E0B_Research_Paper.$ext" "$cur"
  done
  echo "release files written to downloads/; 8 Oct originals kept in downloads/archive/"
fi
