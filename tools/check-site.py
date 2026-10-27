#!/usr/bin/env python3
"""Static-site checks for tarosyn.com (run from the repo root, no dependencies).

1. Every local href/src/srcset in every .html page resolves to a file in the repo.
2. Every <loc> in sitemap.xml maps to a page that exists.
3. No published file exceeds Cloudflare Pages' 25 MiB per-file limit.
4. Every url() in site CSS, every icon in site.webmanifest, and every
   https://tarosyn.com/... og:image / twitter:image / JSON-LD asset exists.
5. Every image a page or stylesheet references stays under IMAGE_BUDGET
   (oversized images made mobile pages look broken in the past).
6. Basic HTML sanity: non-void tags are balanced on every page.
Exits non-zero with a list of problems.
"""
import re
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".github", "node_modules"}
ATTR = re.compile(r'\b(?:href|src|srcset)="([^"]+)"')
MAX_BYTES = 25 * 1024 * 1024
IMAGE_BUDGET = 400 * 1024
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico", ".svg"}
CSS_URL = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)")
ABS_ASSET = re.compile(r"https://tarosyn\.com(/[^\"'\s,]+\.(?:png|jpe?g|webp|ico|svg))")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


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


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        elif any(t == tag for t, _ in self.stack):
            while self.stack and self.stack[-1][0] != tag:
                t, line = self.stack.pop()
                if t not in {"p", "li", "dt", "dd", "option"}:  # optional end tags
                    self.errors.append(f"<{t}> opened on line {line} is never closed")
            self.stack.pop()
        else:
            self.errors.append(f"stray </{tag}> on line {self.getpos()[0]}")


def main() -> int:
    problems = []
    pages = [f for f in published_files() if f.suffix == ".html"]
    referenced = set()
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for raw in ATTR.findall(text):
            # srcset may hold several "url size" candidates
            for ref in [c.strip().split(" ")[0] for c in raw.split(",")]:
                target = resolve(page, ref)
                if target is not None and not target.exists():
                    problems.append(f"{page.relative_to(ROOT)}: broken reference {ref}")
                elif target is not None:
                    referenced.add(target)
        for ref in ABS_ASSET.findall(text):
            target = resolve(ROOT / "index.html", ref)
            if not target.exists():
                problems.append(f"{page.relative_to(ROOT)}: broken absolute asset https://tarosyn.com{ref}")
            else:
                referenced.add(target)
        checker = TagBalance()
        checker.feed(text)
        checker.close()
        leftover = [f"<{t}> opened on line {line} is never closed" for t, line in checker.stack
                    if t not in {"p", "li", "dt", "dd", "option"}]
        for err in checker.errors + leftover:
            problems.append(f"{page.relative_to(ROOT)}: {err}")

    for css in [f for f in published_files() if f.suffix == ".css"]:
        for ref in CSS_URL.findall(css.read_text(encoding="utf-8")):
            if ref.startswith(("data:", "http")) or ref == "x.webp":  # x.webp = @supports feature probe
                continue
            target = (ROOT / ref.lstrip("/")) if ref.startswith("/") else (css.parent / ref)
            if not target.resolve().exists():
                problems.append(f"{css.relative_to(ROOT)}: broken url({ref})")
            else:
                referenced.add(target.resolve())

    manifest = ROOT / "site.webmanifest"
    if manifest.exists():
        for icon in json.loads(manifest.read_text(encoding="utf-8")).get("icons", []):
            target = resolve(ROOT / "index.html", icon["src"])
            if not target.exists():
                problems.append(f"site.webmanifest: missing icon {icon['src']}")
            else:
                referenced.add(target)

    for target in sorted(referenced):
        if target.suffix.lower() in IMAGE_EXT and target.stat().st_size > IMAGE_BUDGET:
            problems.append(f"{target.relative_to(ROOT)}: referenced image is "
                            f"{target.stat().st_size / 1024:.0f} KB (budget {IMAGE_BUDGET // 1024} KB)")

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
    print(f"Site check passed: {len(pages)} pages, {len(referenced)} referenced files; all local links, "
          "CSS urls, manifest icons and sitemap entries resolve, images are within budget, tags balance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
