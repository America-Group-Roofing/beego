# BeeGo — Auditoría e integración LOTE 2
Fecha: 2026-11-25 · Rama develop · 34 códigos maestros · 38 archivos gráficos en LOTE 2.

## Rutas y conservación
- public/assets/LOTE 2/ — archivos recibidos, se conservan originales y sin modificar.
- assets/ — lote previo, conservado para trazabilidad.
- public/assets/ — derivados WebP/PNG/SVG ligeros usados por la aplicación Astro.
- docs/asset-review/lote2-manifest.json — dimensiones, transparencia, SHA-256 y huellas de los 38.
- docs/asset-review/lote2-contact-1.jpg y lote2-contact-2.jpg — comparación visual de los 38.
- docs/asset-review/web-derivatives.json — 42 registros de formatos, pesos y dimensiones derivados.
- scripts/build-web-assets.py — conversión reproducible y nombres estables.

## Matriz de colocación

| Código | Formato y resolución original LOTE 2 | Resultado en el sitio |
|---|---|---|
| BG01 | PNG 1448x1086 | Logo oficial optimizado 473x380: cabecera |
| BG02 | PNG 1448x1086 | Logo monocromático 473x380: disponible para áreas claras |
| BG03 | PNG 1024x1024 | Icono 512, favicon 48, Apple Touch 180 |
| BG04 | PNG 1636x1321 | Panel de logo 380x307: pie oscuro |
| BG05 | 3 SVG 400x48 | Amarillo en hero, negro en contenido, blanco en reserva |
| BG06 | 2 SVG 1440x760 / 390x440 | Red abstracta H05: desktop y móvil |
| PB01 | PNG 1122x1402 | Hero desktop 599x1321 y móvil 372x820; galería |
| PB02 | PNG 887x1774 | Frontal 735x1480; Inicio H04 y Producto |
| PB03 | PNG 887x1774 | Recorte inferior 730x499: cables sin certificaciones |
| PB04 | PNG 887x1774 | Lateral de botón 187x1250; Producto |
| PB05 | PNG 887x1774 | Lateral USB-C 197x1250; Producto |
| PB06 | PNG 2172x724 | Contactos inferiores 1250x336; Producto |
| FT01 | PNG 1672x941 | H02 urbano 1450x816 / móvil 780x439 |
| FT02 | PNG 1402x1122 | Cafetería 900x720; H06 y paso 04 |
| FT03 | PNG 1672x941 | Centro comercial 1000x563; H06 |
| FT04 | PNG 1672x941 | Evento 1000x563; H06 |
| FT05 | PNG 1122x1402 | Ciudad 750x937; H06 |
| FT06 | PNG 1448x1086 | Hotel 1050x788; Negocios |
| FT07 | PNG 1672x941 | Espera 1100x619; Negocios |
| ES01 | PNG 1199x1312 | Estación 689x850; Negocios, ilustrativa |
| ES02 | PNG 1672x941 | Cafetería y estación 1320x743; Inicio H07 y Negocios |
| IL01 | PNG 1448x1086 | Encuentra 1000x750; Inicio H03 y Cómo funciona |
| IL02 | PNG 1448x1086 | Retira 1000x750; Inicio H03 y Cómo funciona |
| IL03 | PNG 1446x1087 | Devuelve 1000x752; Inicio H03 y Cómo funciona |
| IL04 | WebP 1600x920 / 960x2220 | Requisitos de instalación: Negocios desktop/móvil |
| IC01 | SVG 24x24 | Ayuda: batería |
| IC02 | SVG 24x24 | Ayuda: ubicación |
| IC03 | SVG 24x24 | Cómo funciona: consulta de condiciones |
| IC04 | SVG 24x24 | Retiro; preparado como componente reutilizable |
| IC05 | SVG 24x24 | Devolución; preparado como componente reutilizable |
| IC06 | SVG 24x24 | Ayuda y FAQ |
| OG01 | PNG 1200x630 | Vista previa por defecto de páginas generales |
| OG02 | PNG 1200x630 | Vista previa para Negocios |
| OG03 | PNG 1200x630 | Vista previa para Producto |

## Duplicados y mejor diseño
Los SHA de Git confirman seis repeticiones idénticas entre archivos previos y LOTE 2: BG05 amarillo, blanco y negro; PB05; PB06; OG01. No requieren regeneración. Se conserva sólo un derivado activo por caso, sin borrar originales.

PB01-PB04 e IL01-IL03 del lote anterior y del nuevo pueden representar la misma función, pero NO son idénticos. Se eligieron los nuevos por consistencia estética y procedencia, sin asumir que el render valide el hardware. BG01 se usa sobre cabecera clara; BG04 sobre pie oscuro. BG02 queda reservada.

La vista PB03 de origen contiene potencias y sellos no acreditados: únicamente se publica la zona inferior recortada. ES01 y ES02 muestran estaciones conceptuales, no ubicaciones instaladas. Los pasos IL01-IL03 contienen equipos ilustrativos. IL04 representa requisitos de instalación, no uso del producto; por eso pertenece a Negocios y no al paso 04 de Cómo funciona.

Las fotografías FT muestran escenas promocionales que requieren confirmación de derechos de uso, antes de considerarlas testimonios o instalaciones reales.

## Compatibilidad y peso
Los archivos web usan nombres estables, WebP optimizados y variantes mobile para hero, foto principal, fondos BG06 y panel de requisitos IL04. El navegador no descarga los PNG originales grandes para mostrar las páginas. Las composiciones usan retículas fluidas, imágenes responsivas, controles grandes, accesibilidad de teclado y preferencia de movimiento reducido.

La QA automatizada está en scripts/responsive-smoke.mjs y .github/workflows/responsive.yml: Chromium, WebKit y Firefox entre 320 y 3840 px. Una ejecución exitosa no equivale a ensayos físicos de todos los dispositivos.

## Organización futura
LOTE 2 permanece dentro de public/assets para preservar exactamente la ruta de carga original. Antes del lanzamiento comercial, conviene trasladar el archivo maestro fuera de public/ de forma controlada, conservando historial y generando sólo los derivados públicos; no se ha ejecutado ninguna eliminación.

No se publican ubicaciones falsas, tarifas ficticias, cobros operativos, instalaciones supuestamente firmadas, certificaciones ni compatibilidades no verificadas.
