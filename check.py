#!/usr/bin/env python3
"""Smoke check: internal links/files/anchors exist, no phone number, no TODO text.
Usage: python3 check.py"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parent


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids, self.placeholders = [], set(), 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if "data-todo" in a:
            self.placeholders += 1
        for key in ("href", "src"):
            if a.get(key):
                self.refs.append(a[key])


errors = []
page = ROOT / "index.html"
text = page.read_text(encoding="utf-8")
scan = Scan()
scan.feed(text)

for ref in scan.refs:
    if ref == "#":
        continue
    u = urlparse(ref)
    if u.scheme in ("http", "https", "mailto"):
        continue
    if u.scheme:
        errors.append(f"unexpected scheme: {ref}")
    elif ref.startswith("#"):
        if ref[1:] not in scan.ids:
            errors.append(f"missing anchor: {ref}")
    elif not (ROOT / u.path).exists():
        # photo.jpg is optional; the page hides it when missing
        if u.path != "photo.jpg":
            errors.append(f"missing file: {ref}")

for pattern, msg in ((r"\+?91\s?7218347988|7218347988|tel:", "phone number"), (r"TODO", "TODO text")):
    if re.search(pattern, text):
        errors.append(f"found {msg} in index.html")

for f in ("style.css", "script.js", "academic_cv.pdf"):
    if not (ROOT / f).exists():
        errors.append(f"missing file: {f}")

if errors:
    print("FAIL")
    print("\n".join(f"  - {e}" for e in errors))
    sys.exit(1)
print(f"OK ({len(scan.refs)} links checked)")
if scan.placeholders:
    print(f"note: {scan.placeholders} placeholder link(s) still marked data-todo")
if not (ROOT / "photo.jpg").exists():
    print("note: photo.jpg not found (profile photo is hidden)")
