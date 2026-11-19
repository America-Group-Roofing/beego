#!/usr/bin/env python3
"""Validación visual reproducible de originales en assets/.

Genera un inventario JSON y vistas reducidas para auditoría de diseño.
No altera los originales, no significa aprobación de marca ni publica imágenes.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "assets"
DEST = ROOT / "docs" / "asset-review"
EXTENSIONS = {".png", ".webp", ".jpg", ".jpeg"}
LIMIT = 30_000_000


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"):
        if Path(f).is_file():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def fill_card(path: Path, size: tuple[int, int]) -> Image.Image:
    width, height = size
    bg = Image.new("RGB", (width, height), "#F5F5F3")
    d = ImageDraw.Draw(bg)
    square = 16
    for y in range(0, height, square):
        for x in range(0, width, square):
            if ((x // square) + (y // square)) % 2:
                d.rectangle((x, y, x + square - 1, y + square - 1), fill="#E9E9E5")
    with Image.open(path) as src:
        src.thumbnail((width - 24, height - 24), Image.Resampling.LANCZOS)
        rgba = src.convert("RGBA")
        bg.paste(rgba, ((width - rgba.width) // 2, (height - rgba.height) // 2), rgba)
    return bg


def main():
    paths = sorted(p for p in SOURCE.iterdir() if p.is_file() and p.suffix.lower() in EXTENSIONS)
    if not paths:
        raise SystemExit("No hay imágenes para revisar")
    DEST.mkdir(parents=True, exist_ok=True)
    rows = []
    cell_w, cell_h = 570, 420
    cols = 2
    thumb_w, thumb_h = 560, 350
    sheet = Image.new("RGB", (cols * cell_w, ((len(paths) + cols - 1) // cols) * cell_h), "white")
    drawer = ImageDraw.Draw(sheet)
    title_font, sub_font = font(17), font(14)
    for i, p in enumerate(paths):
        data = p.read_bytes()
        if len(data) > LIMIT:
            raise ValueError(f"Archivo supera límite de revisión: {p}")
        try:
            with Image.open(p) as im:
                im.verify()
            with Image.open(p) as im:
                im.load()
                w, h = im.size
                alpha = "A" in im.getbands() or "transparency" in im.info
                bbox = im.convert("RGBA").getchannel("A").getbbox() if alpha else None
                mode, fmt = im.mode, im.format
        except (UnidentifiedImageError, OSError) as err:
            raise RuntimeError(f"Imagen inválida: {p.name}: {err}") from err
        row = {
            "path": p.relative_to(ROOT).as_posix(),
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "width": w, "height": h,
            "format": fmt, "mode": mode,
            "has_alpha": bool(alpha),
            "alpha_content_bbox": bbox,
            "review_status": "pendiente de validación final",
            "production_ready": False,
        }
        rows.append(row)
        thumb = fill_card(p, (thumb_w, thumb_h))
        x = (i % cols) * cell_w + 5
        y = (i // cols) * cell_h + 5
        sheet.paste(thumb, (x, y))
        label = p.name
        if len(label) > 49:
            label = label[:46] + "..."
        drawer.text((x + 5, y + 355), label, font=title_font, fill="#171717")
        drawer.text((x + 5, y + 383), f"{w} x {h} px  |  {len(data)/1024:.0f} KiB  |  alfa: {'si' if alpha else 'no'}", font=sub_font, fill="#52524d")
    doc = {
        "generated": str(date.today()),
        "source_directory": "assets/",
        "count_raster": len(rows),
        "disclaimer": "Revisión técnica automatizada. No certifica fidelidad visual, licencia de uso, fabricante ni operación real.",
        "files": rows,
    }
    (DEST / "inventory.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sheet.save(DEST / "contact-sheet.jpg", "JPEG", quality=76, optimize=True)
    print(f"Auditoría técnica: {len(rows)} imágenes válidas.")
    for it in rows:
        print(f"{it['path']}: {it['width']}x{it['height']} {it['format']} {it['bytes']} bytes alpha={it['has_alpha']}")
    print(f"Hoja de revisión: {(DEST/'contact-sheet.jpg').stat().st_size} bytes")


if __name__ == "__main__":
    main()
