#!/usr/bin/env python3
"""Static-site checks for tarosyn.com (run from the repo root, no dependencies).

1. Every local href/src/srcset in every .html page resolves to a file in the repo.
2. Every <loc> in sitemap.xml maps to a page that exists.
3. No published file exceeds Cloudflare Pages' 25 MiB per-file limit.
Exits non-zero with a list of problems.
"""
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".github", "node_modules"}
ATTR = re.compile(r'\b(?:href|src|srcset)="([^"]+)"')
MAX_BYTES = 25 * 1024 * 1024


def resolve(page: Path, ref: str) -> Path | None:
    """Return the filesystem target for a local reference, or None if external/ignorable."""
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#", "//", "javascript:")):
        return None
    path = unquote(urlsplit(ref).path)
    if not path:
        return None
    base = ROOT if path.startswith("/") else page.parent
    target = (base / path.lstrip("/")).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def published_files():
    for f in ROOT.rglob("*"):
        if f.is_file() and not (set(f.relative_to(ROOT).parts) & SKIP_DIRS):
            yield f


def main() -> int:
    problems = []
    pages = [f for f in published_files() if f.suffix == ".html"]
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for raw in ATTR.findall(text):
            # srcset may hold several "url size" candidates
            for ref in [c.strip().split(" ")[0] for c in raw.split(",")] if "," in raw else [raw]:
                target = resolve(page, ref)
                if target is not None and not target.exists():
                    problems.append(f"{page.relative_to(ROOT)}: broken reference {ref}")

    sitemap = ROOT / "sitemap.xml"
    if sitemap.exists():
        for loc in re.findall(r"<loc>https://tarosyn\.com(/[^<]*)</loc>", sitemap.read_text(encoding="utf-8")):
            target = resolve(ROOT / "index.html", loc)
            if target is not None and not target.exists():
                problems.append(f"sitemap.xml: {loc} has no matching page")

    for f in published_files():
        if f.stat().st_size > MAX_BYTES:
            problems.append(f"{f.relative_to(ROOT)}: {f.stat().st_size / 1e6:.1f} MB exceeds the 25 MiB Pages limit")

    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) found across {len(pages)} pages.")
        return 1
    print(f"Site check passed: {len(pages)} pages, all local links and sitemap entries resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
