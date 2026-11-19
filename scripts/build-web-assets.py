#!/usr/bin/env python3
"""Produce versiones WebP para staging, sin alterar assets/ originales.

Incluye IL01 como ilustración didáctica claramente conceptual.
PB03 se procesa como recorte de cables inferiores sin publicar marcados
técnicos ni sellos de certificación pendientes. No equivale a aprobación comercial.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets"
OUT = ROOT / "public" / "assets"
AUDIT = ROOT / "docs" / "asset-review"
OUT.mkdir(parents=True, exist_ok=True)
AUDIT.mkdir(parents=True, exist_ok=True)

# salida -> (original, max-width, max-height, crop-transparent-margins)
DERIVATIVES = {
    "beego-hero.webp": ("Batería portátil BeeGo amarilla.png", 1050, 1400, True),
    "beego-producto-frontal.webp": ("Power Bank Amarillo BeeGo.png", 740, 1480, True),
    "beego-producto-lateral-usbc.webp": ("BeeGo_PB05_Lateral_USB_C_Transparente.png", 380, 1250, True),
    "beego-producto-lateral-boton.webp": ("Dispositivo amarillo minimalista en perfil.png", 380, 1250, True),
    "beego-producto-contactos.webp": ("BeeGo_PB06_Contactos_Inferiores_Transparente.png", 1250, 430, True),
    "beego-il-encontrar-conceptual.webp": ("BeeGo_IL01_Encontrar_Estacion_Final_Conceptual.png", 1000, 800, False),
    "beego-il-retirar-conceptual.webp": ("BeeGo_IL02_Retirar_Bateria_Web.webp", 1000, 800, False),
    "beego-il-devolver-conceptual.webp": ("Mujer devolviendo batería BeeGo.png", 1000, 800, False),
}
rows=[]
for target, (filename, max_w, max_h, trim) in DERIVATIVES.items():
    source=SRC/filename
    with Image.open(source) as im:
        im.load()
        im=im.convert("RGBA")
        if trim:
            bb=im.getchannel("A").getbbox()
            if bb:
                pad=int(max(im.size)*0.025)
                im=im.crop((max(0,bb[0]-pad),max(0,bb[1]-pad),min(im.width,bb[2]+pad),min(im.height,bb[3]+pad)))
        im.thumbnail((max_w,max_h),Image.Resampling.LANCZOS)
        im.save(OUT/target,format="WEBP",quality=84,method=6,exact=True)
        rows.append({"source":source.relative_to(ROOT).as_posix(),"output":(OUT/target).relative_to(ROOT).as_posix(),"width":im.width,"height":im.height,"bytes":(OUT/target).stat().st_size,"sha256":hashlib.sha256((OUT/target).read_bytes()).hexdigest(),"status":"staging; requiere aprobación editorial para lanzamiento comercial"})
# PB03: recortar únicamente los conectores/cables, evitando marcas CE,
# FCC y RoHS y cifras técnicas no verificadas de la mitad superior.
# Este recorte es una vista parcial de diseño, no el reverso completo.
rear=SRC/"Power Bank Amarillo con Cables Integrados.png"
rear_output=OUT/"beego-producto-cables-posteriores.webp"
with Image.open(rear) as im:
    im.load()
    full=im.convert("RGBA")
    # Original 1024 x 1536: recorte de la sección inferior de cables.
    # Coordenadas proporcionales para no depender de escala JPEG/PNG.
    w,h=full.size
    region=full.crop((int(w*.14),int(h*.67),int(w*.985),int(h*.985)))
    region.thumbnail((730,650),Image.Resampling.LANCZOS)
    region.save(rear_output,format="WEBP",quality=86,method=6,exact=True)
    rows.append({
        "source":rear.relative_to(ROOT).as_posix(),
        "output":rear_output.relative_to(ROOT).as_posix(),
        "width":region.width,"height":region.height,
        "bytes":rear_output.stat().st_size,
        "sha256":hashlib.sha256(rear_output.read_bytes()).hexdigest(),
        "status":"vista parcial de cables; crop excluye especificaciones y sellos no validados"
    })

og=OUT/"beego-og-inicio.png"
shutil.copyfile(SRC/"BeeGo_OG01_Inicio_1200x630.png",og)
rows.append({"source":"assets/BeeGo_OG01_Inicio_1200x630.png","output":"public/assets/beego-og-inicio.png","width":1200,"height":630,"bytes":og.stat().st_size,"sha256":hashlib.sha256(og.read_bytes()).hexdigest(),"status":"vista previa de entorno preoperativo"})
for color in ("amarillo","blanco","negro"):
    filename=f"BG05_franjas_dobles_{color}.svg"
    target=OUT/f"beego-franjas-{color}.svg"
    shutil.copyfile(SRC/filename,target)
    rows.append({"source":f"assets/{filename}","output":(target).relative_to(ROOT).as_posix(),"bytes":target.stat().st_size,"status":"decorativo; no confundir con el archivo vectorial oficial del logotipo"})
(AUDIT/"web-derivatives.json").write_text(json.dumps({"note":"Derivados de staging; IL01 sólo para una ilustración conceptual y PB03 sólo detalle recortado de cables. No deben publicarse certificaciones no acreditadas ni mapas reales simulados.","files":rows},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
for r in rows:print(r["output"],r["bytes"],r.get("width","SVG"),r.get("height",""))
