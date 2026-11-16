"""Wrap app.html (artifact-style fragment) into a full standalone page in docs/index.html for hosting."""
from pathlib import Path

here = Path(__file__).parent
src = (here / "app.html").read_text(encoding="utf-8")
head = (
    '<!doctype html><html lang="nl"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    '<meta name="apple-mobile-web-app-capable" content="yes">'
    '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
    '<meta name="theme-color" content="#121417">'
    '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
    'body{margin:0}[hidden]{display:none!important}</style></head><body>'
)
out = here / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(head + src + "</body></html>", encoding="utf-8")
print("built", out, out.stat().st_size, "bytes")
