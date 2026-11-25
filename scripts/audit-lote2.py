#!/usr/bin/env python3
"""Auditoría reproducible de LOTE 2: metadatos, duplicados y miniaturas de selección."""
import csv, hashlib, json, math
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
LOT=ROOT/"public"/"assets"/"LOTE 2"
OUT=ROOT/"docs"/"asset-review"
OUT.mkdir(parents=True,exist_ok=True)
FILES=sorted(p for p in LOT.rglob("*") if p.is_file() and p.suffix.lower() in (".png",".jpg",".jpeg",".webp",".svg"))
META=[]
for p in FILES:
    b=p.read_bytes()
    rec={"name":p.name,"path":p.relative_to(ROOT).as_posix(),
         "bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),
         "extension":p.suffix.lower()}
    if p.suffix.lower()==".svg":
        svg=ET.fromstring(b)
        rec["viewbox"]=svg.attrib.get("viewBox")
        rec["dimensions"]=svg.attrib.get("viewBox","vector")
    else:
        with Image.open(p) as im:
            im.load()
            rec.update(width=im.width,height=im.height,mode=im.mode,format=im.format,
                       has_alpha=("A" in im.getbands() or "transparency" in im.info),
                       aspect=round(im.width/im.height,3))
            thumb=ImageOps.grayscale(im.convert("RGB")).resize((9,8),Image.Resampling.LANCZOS)
            pix=list(thumb.getdata())
            dh=0
            for row in range(8):
                for col in range(8):
                    dh=(dh<<1)|int(pix[row*9+col]>pix[row*9+col+1])
            rec["dhash"]=f"{dh:016x}"
    META.append(rec)
groups=defaultdict(list)
for r in META:groups[r["sha256"]].append(r["path"])
dup={k:v for k,v in groups.items() if len(v)>1}
(OUT/"lote2-manifest.json").write_text(json.dumps({"files":META,"exact_duplicate_groups":dup},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
# Two contact sheets: first identities/product/editorial, second stations/illustrations/OG.
sections=[
    ("lote2-contact-1.jpg",[x for x in META if any(s in x["path"] for s in ("01_Identidad_BG","02_Producto_PB","03_Fotografia_FT"))]),
    ("lote2-contact-2.jpg",[x for x in META if any(s in x["path"] for s in ("04_Estaciones_ES","05_Ilustraciones_IL","06_Iconografia_IC","07_Redes_OG"))])
]
font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",13)
small=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",10)
for name,items in sections:
    cw,ch=290,268
    cols=4
    sheet=Image.new("RGB",(cw*cols,ch*math.ceil(len(items)/cols)),(246,246,244))
    draw=ImageDraw.Draw(sheet)
    for i,rec in enumerate(items):
        px=(i%cols)*cw; py=(i//cols)*ch
        draw.rectangle((px+4,py+4,px+cw-4,py+ch-4),fill="white",outline="#D1D1D1",width=1)
        p=ROOT/rec["path"]
        if p.suffix.lower()==".svg":
            draw.rectangle((px+18,py+18,px+cw-18,py+204),fill="#eeeeee")
            draw.text((px+65,py+84),"SVG / "+p.stem[:14],fill="#222",font=font)
        else:
            with Image.open(p) as im:
                im.thumbnail((cw-30,185),Image.Resampling.LANCZOS)
                if im.mode=="RGBA":
                    # Checker pattern for transparent assets
                    bg=Image.new("RGB",im.size,(235,235,235))
                    bg.paste(im.convert("RGBA"),mask=im.getchannel("A"))
                    im=bg
                else: im=im.convert("RGB")
                sheet.paste(im,(px+(cw-im.width)//2,py+12+(185-im.height)//2))
        nm=rec["name"]
        draw.text((px+12,py+204),nm[:34],font=font,fill=(15,15,15))
        if len(nm)>34:draw.text((px+12,py+222),nm[34:67],font=small,fill=(20,20,20))
        size=(str(rec.get("width","SVG"))+"x"+str(rec.get("height",""))) if "width" in rec else "Vector"
        draw.text((px+12,py+243),size+"  "+str(round(rec["bytes"]/1024))+" KB",font=small,fill=(85,85,85))
    sheet.save(OUT/name,format="JPEG",quality=79,optimize=True)
print("LOTE2 audited",len(META),"files; duplicate groups",len(dup))
for name,items in sections:print(name,len(items),(OUT/name).stat().st_size)
