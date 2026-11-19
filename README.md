# BeeGo · Web (Astro)

Repositorio de **BeeGo**, proyecto independiente dentro de la organización **America-Group-Roofing**.

**Eslogan oficial:** Energía que va contigo.

## Estado

**Preparación preoperativa**, no lanzamiento comercial. La rama develop contiene la base del proyecto; main conserva la documentación aprobada. No hay estaciones públicas verificadas, rentas, tarifas, pagos ni soporte operativo habilitado desde esta base.

## Stack inicial

- Astro 7 (renderizado estático, sin adaptador de servidor).
- HTML y CSS accesibles; interactividad sólo cuando haga falta.
- GitHub para control de versiones.
- Cloudflare Workers con Static Assets como destino propuesto; staging no conectado ni publicado por defecto.
- Node.js >= 22.23.4.

## Desarrollo local

1. Instala la versión de Node de .nvmrc.
2. Ejecuta npm install para generar el lockfile.
3. Ejecuta npm run check y npm run build.
4. Ejecuta npm run dev para una vista local.

No se han generado ni subido carpetas node_modules o dist, ni un lockfile inventado.

## Estructura

- src/layouts: marco de página.
- src/components: cabecera y pie de página.
- src/pages: páginas públicas iniciales.
- src/styles: estilos base.
- docs: acuerdos de publicación y assets.
- public: directivas de no indexación de staging.

La interfaz es un **andamiaje funcional**, no el diseño visual final. Los logos, render oficial y fotografías deben incorporarse de sus fuentes aprobadas.

## Gobernanza

Los documentos maestros y el Brand Book BeeGo tienen prioridad sobre los placeholders. No mezclar recursos de otras marcas ni confirmar funciones de renta sin validación.

Lee docs/ESTADO-Y-PUBLICACION.md antes de conectar un despliegue.
