#!/usr/bin/env python3
"""Build index.html: inline every {{IMG:name}} from assets/images/<name>.jpg as a data URI.

Usage:  python3 build.py
Edit src/template.html (and the images in assets/images), then run this to regenerate index.html.
"""
import base64, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent
src = (root / "src" / "template.html").read_text(encoding="utf-8")

def embed(match):
    name = match.group(1)
    path = root / "assets" / "images" / f"{name}.jpg"
    if not path.exists():
        sys.exit(f"Missing image: {path}")
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()

out = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", embed, src)
if "{{" in out:
    sys.exit("Unresolved placeholder left in template")
(root / "index.html").write_text(out, encoding="utf-8")
print(f"Built index.html ({len(out)//1024} KB)")
