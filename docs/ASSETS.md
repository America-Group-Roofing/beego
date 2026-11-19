# BeeGo — control de los 12 assets prioritarios

Corte: 19 de noviembre de 2026. **Staging, no lanzamiento comercial.** Fuente: inventario de 12 assets proporcionado por la dirección del proyecto.

## Matriz exacta de colocación

| Código | Material encontrado | Uso acordado | Estado técnico |
|---|---|---|---|
| PB01 | Batería portátil BeeGo amarilla.png | Inicio H01, hero | Integrado en `/assets/beego-hero.webp` |
| PB02 | Power Bank Amarillo BeeGo.png | Inicio H04, P01 galería frontal | Integrado |
| PB03 | Power Bank Amarillo con Cables Integrados.png | P01 detalle posterior y cables | Integrado **parcialmente** como recorte inferior sin datos técnicos ni sellos no verificados |
| PB04 | Dispositivo amarillo minimalista en perfil.png | P01 lateral con botón | Integrado, código provisional |
| PB05 | BeeGo_PB05_Lateral_USB_C_Transparente.png | P01 lateral USB-C | Integrado |
| PB06 | BeeGo_PB06_Contactos_Inferiores_Transparente.png | P01 contactos inferiores | Integrado |
| FT01 | **No aparece en `assets/`** | Inicio H02, fotografía urbana | **Pendiente de entrega**; no sustituida artificialmente |
| IL01 | BeeGo_IL01_Encontrar_Estacion_Final_Conceptual.png | Inicio H03 paso 1, Cómo funciona | Integrado sólo como imagen **conceptual**; el mapa visible es ficticio y no refleja estaciones reales |
| IL02 | BeeGo_IL02_Retirar_Bateria_Web.webp | Inicio H03 paso 2, Cómo funciona | Integrado como representación conceptual |
| IL03 | Mujer devolviendo batería BeeGo.png | Inicio H03 paso 3, Cómo funciona | Integrado como representación conceptual |
| BG05 | BG05_franjas_dobles_amarillo/blanco/negro.svg | Sistema gráfico, especialmente H03 y divisores | Integrado en hero, H03 y otras secciones; tres variantes registradas |
| OG01 | BeeGo_OG01_Inicio_1200x630.png | Metadatos Open Graph | Integrado en el layout global de staging |

**Resumen:** 11/12 códigos de producción tienen ubicación en la interfaz o metadata. FT01 está ausente. PB03 se utiliza sólo como detalle parcial de cables, no se presenta la parte que contiene certificaciones y especificaciones no verificadas. Entre los 12, BG05 es un grupo de tres variantes.

## Procedencia y control

- Los originales se conservan intactos en `assets/`. No se han movido ni sobrescrito.
- Los derivados optimizados se guardan en `public/assets/` y se generan mediante `scripts/build-web-assets.py`.
- Inventario original: `docs/asset-review/inventory.json`, hoja de contacto: `docs/asset-review/contact-sheet.jpg`, derivados y trazabilidad: `docs/asset-review/web-derivatives.json`.
- El archivo `assets/.node` no es una imagen ni cuenta en la cifra.
- Los textos e ilustraciones de estaciones siguen etiquetados como **conceptuales**, sin insinuar localizaciones, compatibilidad, disponibilidad ni devoluciones confirmadas.
- El recorte de PB03 no valida que los cables de un producto manufacturado tengan las especificaciones del diseño.
- El registro de códigos PB04 e IL03 es provisional hasta aprobar el catálogo final de nombres.

## Pendientes para aprobación comercial

FT01, logotipos oficiales individuales optimizados, derechos de uso de imágenes con personas, dimensiones técnicas de fabricación, certificaciones verificadas, hardware final de estaciones y las condiciones reales de renta. La imagen OG01 comunica que la red está en desarrollo. La funcionalidad de estaciones no es un mapa activo.

La página sólo es una presentación de staging preoperativo, **no debe publicarse como anuncio de operaciones habilitadas**.
