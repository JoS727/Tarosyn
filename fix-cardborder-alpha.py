#!/usr/bin/env python3
"""
Convert Cardborder.png from a baked-in fake-transparency checkerboard into a
real RGBA PNG with an alpha channel.

The Canva export is colortype 2 (RGB, no alpha). What looks like transparency
in a preview is literally painted pixels: a ~16px checkerboard alternating
between roughly (254,254,254) and (245,245,245). Composited over card art it
would show up as an opaque grey grid.

This finds those two greys and makes them transparent, leaving the frame art
opaque. Pure stdlib — no PIL on this machine.

Usage: python3 fix-cardborder-alpha.py <in.png> <out.png>
"""
import struct
import sys
import zlib


def read_png_rgb(path):
    d = open(path, "rb").read()
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("not a PNG")
    w, h, depth, ctype = struct.unpack(">IIBB", d[16:26])
    if (depth, ctype) != (8, 2):
        raise SystemExit(f"expected 8-bit RGB (depth 8, colortype 2), got {depth}/{ctype}")

    idat = b""
    i = 8
    while i < len(d):
        ln = struct.unpack(">I", d[i:i + 4])[0]
        typ = d[i + 4:i + 8]
        if typ == b"IDAT":
            idat += d[i + 8:i + 8 + ln]
        i += 12 + ln

    raw = zlib.decompress(idat)
    bpp, stride = 3, w * 3 + 1
    prev = bytearray(w * 3)
    rows = []
    for y in range(h):
        f = raw[y * stride]
        line = bytearray(raw[y * stride + 1:(y + 1) * stride])
        for x in range(len(line)):
            a = line[x - bpp] if x >= bpp else 0
            b = prev[x]
            c = prev[x - bpp] if x >= bpp else 0
            if f == 1:
                line[x] = (line[x] + a) & 255
            elif f == 2:
                line[x] = (line[x] + b) & 255
            elif f == 3:
                line[x] = (line[x] + (a + b) // 2) & 255
            elif f == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[x] = (line[x] + pr) & 255
        rows.append(bytes(line))
        prev = line
    return w, h, rows


def write_png_rgba(path, w, h, rows_rgba):
    def chunk(typ, data):
        return (struct.pack(">I", len(data)) + typ + data +
                struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF))

    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    raw = b"".join(b"\x00" + r for r in rows_rgba)
    out = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) +
           chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))
    open(path, "wb").write(out)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "Cardborder.png"
    dst = sys.argv[2] if len(sys.argv) > 2 else "Cardborder-alpha.png"

    w, h, rows = read_png_rgb(src)

    # The checkerboard is near-white and desaturated. Frame art is dark purple,
    # black, or saturated gold — none of it lands in this band.
    def is_checker(r, g, b):
        return (r > 235 and g > 235 and b > 235 and
                max(r, g, b) - min(r, g, b) <= 4)

    cleared = 0
    out_rows = []
    for y in range(h):
        row = rows[y]
        o = bytearray(w * 4)
        for x in range(w):
            r, g, b = row[x * 3], row[x * 3 + 1], row[x * 3 + 2]
            j = x * 4
            o[j], o[j + 1], o[j + 2] = r, g, b
            if is_checker(r, g, b):
                o[j + 3] = 0
                cleared += 1
            else:
                o[j + 3] = 255
        out_rows.append(bytes(o))

    write_png_rgba(dst, w, h, out_rows)
    total = w * h
    print(f"{dst}: {w}x{h} RGBA")
    print(f"transparent: {cleared:,}/{total:,} px ({100 * cleared / total:.1f}%)")
    print(f"opaque frame art: {100 * (total - cleared) / total:.1f}%")


if __name__ == "__main__":
    main()
