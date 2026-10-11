#!/usr/bin/env python3
"""Build index.html: inline every {{IMG:name}} from assets/images/<name>.jpg or .png as a data URI.

Usage:  python3 build.py
Edit src/template.html (and the images in assets/images), then run this to regenerate index.html.
"""
import base64, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent
src = (root / "src" / "template.html").read_text(encoding="utf-8")

def embed(match):
    name = match.group(1)
    for ext, mime in (("jpg", "image/jpeg"), ("png", "image/png")):
        path = root / "assets" / "images" / f"{name}.{ext}"
        if path.exists():
            return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()
    sys.exit(f"Missing image: assets/images/{name}.jpg or .png")

out = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", embed, src)
if "{{" in out:
    sys.exit("Unresolved placeholder left in template")
(root / "index.html").write_text(out, encoding="utf-8")
print(f"Built index.html ({len(out)//1024} KB)")
