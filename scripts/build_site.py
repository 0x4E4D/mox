"""Build the standalone site from the latest G2 prototype.

Usage: python3 scripts/build_site.py <prototypes dir> <output dir>
Copies g2.html as index.html without the "All versions" button, plus only the images it references.
"""
import os, re, shutil, sys

src, out = sys.argv[1], sys.argv[2]
html = open(os.path.join(src, "g2.html"), encoding="utf-8").read()
html = re.sub(r"<!--back-->.*?<!--/back-->", "", html, flags=re.S)
html = re.sub(r"<title>.*?</title>", '<title>Mox</title>\n<link rel="icon" href="img/mark.svg" type="image/svg+xml">', html, count=1, flags=re.S)
os.makedirs(out, exist_ok=True)
open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
refs = sorted(set(re.findall(r"(img/[\w./-]+\.(?:jpg|jpeg|png|svg|webp|gif))", html)) | {"img/mark.svg"})
for r in refs:
    os.makedirs(os.path.join(out, os.path.dirname(r)), exist_ok=True)
    shutil.copyfile(os.path.join(src, r), os.path.join(out, r))
print(f"Built {out}/index.html with {len(refs)} images")
