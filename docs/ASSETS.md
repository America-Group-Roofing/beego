# Auditoría y ubicación de los assets BeeGo

Actualizado: 19 de noviembre de 2026. Revisión para el entorno de pruebas, no aprobación comercial.

Se conservan los 10 archivos PNG/WebP y los 3 SVG originales de la carpeta assets. El archivo .node no es un asset. La revisión técnica se puede consultar en docs/asset-review/inventory.json y el mosaico de las diez imágenes en docs/asset-review/contact-sheet.jpg. El registro de los once derivados está en docs/asset-review/web-derivatives.json.

## Destinos por imagen

| Original | Código de trabajo | Uso |
| --- | --- | --- |
| Batería portátil BeeGo amarilla.png | PB01 | Hero de Inicio, perspectiva de Producto y recorrido ilustrativo |
| Power Bank Amarillo BeeGo.png | PB02 | Inicio H04 y galería de Producto |
| BeeGo_PB05_Lateral_USB_C_Transparente.png | PB05 | Galería: vista lateral USB-C |
| Dispositivo amarillo minimalista en perfil.png | PB04 provisional | Galería: lateral con botón |
| BeeGo_PB06_Contactos_Inferiores_Transparente.png | PB06 | Galería: extremo inferior |
| BeeGo_IL02_Retirar_Bateria_Web.webp | IL02 | Inicio y Cómo funciona, con aviso conceptual |
| Mujer devolviendo batería BeeGo.png | IL03 provisional | Inicio, Cómo funciona y Negocios, con aviso conceptual |
| BeeGo_OG01_Inicio_1200x630.png | OG01 | Vista previa de enlaces en staging |
| BeeGo_IL01_Encontrar_Estacion_Final_Conceptual.png | IL01 | Excluido de la web: mapa con ubicaciones ilustrativas que pueden confundirse con cobertura |
| Power Bank Amarillo con Cables Integrados.png | PB03 provisional | Excluido de la web: contiene símbolos y certificaciones de fabricante no verificadas |
| Tres SVG BG05 de franjas paralelas | BG05 | Uso decorativo, no reemplazan el logotipo oficial |

## Gobierno y publicación

Los originales de assets no se modificaron ni se movieron. Los derivados optimizados WebP, PNG y SVG están en public/assets y se sirven de forma estática. Los once derivados no equivalen a once assets finales aprobados.

Quedan pendientes: logotipos oficiales individuales dentro del repositorio, revisión de licencia de fotografías de personas, especificaciones técnicas verificadas, muestras manufacturadas y validación de los modelos de estación. No se presentan estaciones ni operaciones reales.

Las imágenes de estaciones y devoluciones están etiquetadas como conceptuales. Las vistas de producto se consideran renders de diseño. No se utilizan mapas ficticios, precios inventados ni certificaciones no acreditadas.
