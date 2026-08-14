#!/usr/bin/env node
/**
 * Wrap bare <img src="assets/...(png|jpg)"> in <picture> with a WebP source,
 * keeping the original as the fallback <img>. Only rewrites when a sibling
 * .webp actually exists on disk, so a missing conversion can never produce a
 * broken <source>.
 *
 * Skips <img> already inside a <picture> (the hero, handled by hand).
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';

const file = process.argv[2];
const root = dirname(file);
let html = readFileSync(file, 'utf8');

let wrapped = 0;
let skippedNoWebp = 0;

// Match a standalone <img ...> whose src is a local raster asset.
html = html.replace(/<img\b([^>]*?)src="(assets\/[^"]+\.(?:png|jpe?g))"([^>]*?)>/g,
  (match, pre, src, post, offset, full) => {
    // Already inside a <picture>? Look back a short window for an unclosed tag.
    const before = full.slice(Math.max(0, offset - 400), offset);
    const lastOpen = before.lastIndexOf('<picture');
    const lastClose = before.lastIndexOf('</picture>');
    if (lastOpen > lastClose) return match;   // inside a picture already

    const webp = src.replace(/\.(png|jpe?g)$/, '.webp');
    if (!existsSync(join(root, webp))) { skippedNoWebp++; return match; }

    wrapped++;
    return `<picture><source type="image/webp" srcset="${webp}">${match}</picture>`;
  });

writeFileSync(file, html);
console.log(`${file}: wrapped ${wrapped} img(s); skipped ${skippedNoWebp} (no .webp on disk)`);
