# BeeGo · Sitio web (Astro)

Proyecto independiente **BeeGo** dentro de la organización **America-Group-Roofing**.

**Eslogan oficial:** Energía que va contigo.

## Estado actual — 19 de noviembre de 2026

- **Preoperativo / staging**: no constituye un lanzamiento comercial.
- Rama `develop`: aplicación Astro estática y despliegues automáticos de prueba.
- Rama `main`: documentación de referencia; no está vinculada al despliegue de staging.
- Worker Cloudflare: `beego-staging`.
- URL de pruebas: https://beego-staging.america-group-roofing-digital-projects.workers.dev
- Primer despliegue de staging desde `develop` completado correctamente el 19 de noviembre de 2026.
- No hay estaciones públicas verificadas, tarifas aprobadas, pagos ni rentas integradas.

## Stack

- Astro 7, HTML y CSS, con salida estática.
- GitHub como control de versiones.
- Cloudflare Workers con Static Assets como alojamiento de staging.
- Cloudflare CLI `cf` para despliegue de archivos `dist`.
- Node.js >=22.23.4.

## Comandos

```sh
npm install
npm run check
npm run build
npm run dev
```

El `package-lock.json` está pendiente de generar y añadir. Por ello Cloudflare puede omitir la caché de dependencias; el despliegue inicial funcionó correctamente sin ese archivo. No se han subido carpetas generadas como `node_modules` ni `dist`.

## Organización

- `src/pages`: páginas públicas de preparación.
- `src/components`: elementos compartidos.
- `src/layouts`: estructura general.
- `src/styles`: estilos preliminares.
- `public`: recursos estáticos y bloqueo de rastreo de staging.
- `docs`: estado, políticas y assets.

**Este diseño es un andamiaje técnico, no la interfaz premium definitiva.** Se deben incorporar los recursos BeeGo aprobados antes de considerar una publicación comercial.

## Seguridad y gobernanza

- No almacenar credenciales, tokens, documentos internos ni datos personales en el repositorio.
- No confundir renders con prestaciones probadas ni simular estaciones, cobros o devoluciones.
- El acceso por URL al Worker de staging puede ser público. `noindex` y `robots.txt` no sustituyen autenticación.
- Mantener BeeGo separado de otros proyectos de America Group Roofing.
- No promover `develop` a `main` ni usar un dominio de producción sin revisión.

Ver [estado y publicación](docs/ESTADO-Y-PUBLICACION.md).
