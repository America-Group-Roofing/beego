#!/usr/bin/env python3
"""Derivados web ligeros del arte BeeGo aprobado para staging.

Fuentes originales conservadas sin modificar en assets/ y public/assets/LOTE 2/.
Los nombres de salida son estables para Astro. Las estaciones y las escenas
editoriales son imágenes ilustrativas y no prueban operación real.
"""
from __future__ import annotations
import hashlib, json, shutil
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/"assets"
LOT=ROOT/"public"/"assets"/"LOTE 2"
OUT=ROOT/"public"/"assets"
AUDIT=ROOT/"docs"/"asset-review"
OUT.mkdir(parents=True,exist_ok=True)
AUDIT.mkdir(parents=True,exist_ok=True)

def source(group,name):
    p=(LOT/group/name) if group else (OLD/name)
    if not p.is_file():raise FileNotFoundError(p)
    return p

# Destino web, categoría origen, nombre original, tamaño máximo, transparencia/márgenes
IMAGES=[
 ("beego-hero.webp","02_Producto_PB","BeeGo_PB01_Hero_Lateral_USB_C_Transparente.png",1050,1350,True),
 ("beego-hero-mobile.webp","02_Producto_PB","BeeGo_PB01_Hero_Lateral_USB_C_Transparente.png",620,820,True),
 ("beego-producto-frontal.webp","02_Producto_PB","BeeGo_PB02_Vista_Frontal_Transparente.png",740,1480,True),
 ("beego-producto-lateral-boton.webp","02_Producto_PB","BeeGo_PB04_Lateral_Boton_Transparente.png",380,1250,True),
 ("beego-producto-lateral-usbc.webp","02_Producto_PB","BeeGo_PB05_Lateral_USB_C_Transparente.png",380,1250,True),
 ("beego-producto-contactos.webp","02_Producto_PB","BeeGo_PB06_Contactos_Inferiores_Transparente.png",1250,430,True),
 ("beego-il-encontrar-conceptual.webp","05_Ilustraciones_IL","BeeGo_IL01_Encontrar_Estacion_Corregido_Master.png",1000,760,False),
 ("beego-il-retirar-conceptual.webp","05_Ilustraciones_IL","BeeGo_IL02_Retirar_Bateria_Master.png",1000,760,False),
 ("beego-il-devolver-conceptual.webp","05_Ilustraciones_IL","BeeGo_IL03_Devolver_Bateria_Final_Transparente.png",1000,760,False),
 ("beego-ft01-urbana.webp","03_Fotografia_FT","Power Bank BeeGo en Plaza Urbana.png",1450,850,False),
 ("beego-ft01-urbana-small.webp","03_Fotografia_FT","Power Bank BeeGo en Plaza Urbana.png",780,460,False),
 ("beego-ft02-cafeteria.webp","03_Fotografia_FT","Power Bank en Cafetería Acogedora.png",900,780,False),
 ("beego-ft03-comercial.webp","03_Fotografia_FT","Power Bank BeeGo en Centro Comercial.png",1000,600,False),
 ("beego-ft04-evento.webp","03_Fotografia_FT","BeeGo_FT04_Evento_Conceptual.png",1000,600,False),
 ("beego-ft05-ciudad.webp","03_Fotografia_FT","Mujer con power bank BeeGo en la ciudad.png",750,940,False),
 ("beego-ft06-hotel.webp","03_Fotografia_FT","Mujer con power bank BeeGo en hotel.png",1050,850,False),
 ("beego-ft07-espera.webp","03_Fotografia_FT","BeeGo_FT07_Sala_de_Espera_Master.png",1100,640,False),
 ("beego-es01-estacion-conceptual.webp","04_Estaciones_ES","BeeGo_ES01_Estacion_Bajie_Blanca_Conceptual_v3.png",750,850,True),
 ("beego-es02-cafe-conceptual.webp","04_Estaciones_ES","Estación BeeGo en café moderno.png",1320,800,False),
 ("beego-logo-panel.webp","01_Identidad_BG","BG04_BeeGo_Fondo_Oscuro_Panel_Amarillo_Master.png",380,320,False)
]
FILES=[]
def record(src,dest,size=None,tag=""):
    data=dest.read_bytes()
    FILES.append(dict(source=src.relative_to(ROOT).as_posix(),
                      output=dest.relative_to(ROOT).as_posix(),
                      bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                      width=size[0] if size else None,height=size[1] if size else None,
                      note=tag))
def trimmed(im,ratio=.022):
    if "A" not in im.getbands():return im
    bb=im.getchannel("A").getbbox()
    if bb:
        pad=int(max(im.size)*ratio)
        im=im.crop((max(0,bb[0]-pad),max(0,bb[1]-pad),min(im.width,bb[2]+pad),min(im.height,bb[3]+pad)))
    return im
for output,group,name,mw,mh,trim in IMAGES:
    src=source(group,name); dst=OUT/output
    with Image.open(src) as im:
        im.load()
        im=im.convert("RGBA") if ("A" in im.getbands() or "transparency" in im.info) else im.convert("RGB")
        if trim:im=trimmed(im)
        im.thumbnail((mw,mh),Image.Resampling.LANCZOS)
        q=80 if group=="03_Fotografia_FT" else 84
        im.save(dst,format="WEBP",quality=q,method=6,exact=True)
        record(src,dst,im.size,"Conceptual" if group in ("04_Estaciones_ES","05_Ilustraciones_IL") else "Web optimizado")

# PB03 tiene sellos y datos de fabricación no verificados. Sólo el detalle inferior.
rear=source("02_Producto_PB","BeeGo_PB03_Vista_Posterior_Cables_Integrados.png")
with Image.open(rear) as im:
    im=im.convert("RGBA"); w,h=im.size
    crop=im.crop((int(.15*w),int(.70*h),int(.985*w),int(.985*h)))
    crop.thumbnail((730,650),Image.Resampling.LANCZOS)
    dest=OUT/"beego-producto-cables-posteriores.webp"
    crop.save(dest,"WEBP",quality=86,method=6,exact=True)
    record(rear,dest,crop.size,"Recorte inferior: excluye sellos y potencias no verificados")

# Logotipos: escalar su arte original, sin redibujar ni alterar colores.
for filename,output,maxsize in [
 ("BeeGo_BG01_Logo_Oficial_Color_Fondo_Transparente.png","beego-logo-oficial.png",(480,380)),
 ("BeeGo_BG02_Logotipo_Monocromatico_Negro_Oficial.png","beego-logo-monocromo.png",(480,380)),
 ("BG03_Isotipo_Oficial_1024_Transparente.png","beego-isotipo-512.png",(512,512)),
 ("BG03_Isotipo_Oficial_1024_Transparente.png","beego-apple-touch-180.png",(180,180)),
 ("BG03_Isotipo_Oficial_1024_Transparente.png","beego-favicon-48.png",(48,48))
]:
    src=source("01_Identidad_BG",filename)
    with Image.open(src) as im:
        im=im.convert("RGBA")
        if "isotipo" not in output and "favicon" not in output and "apple-touch" not in output:im=trimmed(im,.018)
        im.thumbnail(maxsize,Image.Resampling.LANCZOS)
        dst=OUT/output
        im.save(dst,"PNG",optimize=True)
        record(src,dst,im.size,"Logotipo oficial, arte escalado")
# Versiones vertical y horizontal de requisitos de instalación, sin reprocesar.
for name,out in [
 ("IL04_Requisitos_Instalacion_Desktop.webp","beego-requisitos-desktop.webp"),
 ("IL04_Requisitos_Instalacion_Movil.webp","beego-requisitos-mobile.webp")
]:
    src=source("05_Ilustraciones_IL",name)
    dst=OUT/out
    shutil.copyfile(src,dst)
    with Image.open(dst) as im:record(src,dst,im.size,"Requisitos ilustrativos de instalación B2B")
for name,out in [
 ("BG06_conexiones_desktop.svg","beego-conexiones-desktop.svg"),
 ("BG06_conexiones_movil.svg","beego-conexiones-mobile.svg")
]:
    src=source("01_Identidad_BG",name)
    dst=OUT/out
    shutil.copyfile(src,dst);record(src,dst,tag="Decoración abstracta sin ubicaciones reales")
for i,word in enumerate(("bateria","ubicacion","pago","retiro","devolucion","ayuda"),start=1):
    src=source("06_Iconografia_IC",f"IC{i:02d}_{word}_currentColor.svg")
    dst=OUT/f"beego-icon-{word}.svg"
    shutil.copyfile(src,dst);record(src,dst,tag="SVG lineal 24×24")
for code,output in (("01","inicio"),("02","negocios"),("03","producto")):
    prefix={"01":"BeeGo_OG01_Inicio_1200x630.png",
            "02":"BeeGo_OG02_Para_Negocios_1200x630.png",
            "03":"BeeGo_OG03_Conoce_Tu_BeeGo_1200x630.png"}[code]
    src=source("07_Redes_OG",prefix)
    dst=OUT/f"beego-og-{output}.png"
    shutil.copyfile(src,dst);record(src,dst,(1200,630),"Social 1200×630")
for color in ("amarillo","blanco","negro"):
    src=source("01_Identidad_BG",f"BG05_franjas_dobles_{color}.svg")
    dst=OUT/f"beego-franjas-{color}.svg"
    shutil.copyfile(src,dst);record(src,dst,tag="Franjas dobles oficiales")
(AUDIT/"web-derivatives.json").write_text(json.dumps({
    "notice":"Derivados web del LOTE 2; fuentes originales preservadas; imágenes de estaciones y producto requieren contrastarse con hardware definitivo.",
    "files":FILES},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
for r in FILES:print(r["output"],r["bytes"],r.get("width"),r.get("height"))
