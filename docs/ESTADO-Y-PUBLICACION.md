# BeeGo · Estado y publicación

## Alcance de esta rama

La rama \`develop\` contiene una base inicial de Astro y páginas de contenido **preoperativo**. La rama \`main\` sigue reservada para trabajo aprobado. No mezclar las ramas automáticamente.

## Arquitectura

- Frontend: Astro 7, totalmente estático.
- Infraestructura propuesta: **Cloudflare Workers con Static Assets**.
- CLI actual para proyectos nuevos: **cf 1.0.0-rc.1** (Cloudflare).
- Worker exclusivo de pruebas: **beego-staging**.
- Build: \`npm run build\` (crea \`./dist\`).
- Despliegue previsto: \`npm run deploy:staging\` (publica \`./dist\` usando \`cloudflare.config.ts\`).
- No hay Worker de producción configurado.
- No hay base de datos, pagos, renta ni API conectada.

## Conectar GitHub a Cloudflare

Cloudflare requiere que su propia **Cloudflare GitHub App** sea autorizada para la organización \`America-Group-Roofing\` y el repositorio \`beego\`. El conector de GitHub de ChatGPT es una aplicación distinta y no concede esos permisos automáticamente.

1. Cloudflare → Workers & Pages → Create application → GitHub (o Worker → Settings → Builds → Connect).
2. Autorizar la Cloudflare GitHub App para \`America-Group-Roofing\` y sólo el repositorio \`beego\`.
3. Elegir la rama \`develop\` como fuente del proyecto de pruebas.
4. Configurar build \`npm run build\`, deploy \`npm run deploy:staging\`, Node >=22.23.4.
5. Verificar que el Worker destino se llame exactamente \`beego-staging\`.
6. Comprobar la compilación y la URL de pruebas antes de compartirla.

**La conexión de ChatGPT con GitHub y Cloudflare no equivale a la conexión GitHub → Cloudflare Builds.**

## Seguridad y publicación

- La URL workers.dev puede ser públicamente accesible incluso en staging. El archivo robots.txt y noindex no son autenticación.
- No desplegar a un dominio principal de BeeGo sin autorización adicional.
- Revisar fotos, logotipos y avisos legales antes del sitio comercial.
- No subir archivos .env reales, tokens, datos personales o documentos internos.
- No publicar falsas estaciones, tarifas, transacciones o confirmaciones de devolución.

## Verificación previa

1. \`npm install\` en una máquina/runner con acceso a npm; generar y conservar \`package-lock.json\`.
2. \`npm run check\` y \`npm run build\`.
3. Confirmar que las páginas de prueba indiquen que BeeGo está en preparación.
4. Revisar accesibilidad, enlaces y responsive.
5. Autorizar y probar la publicación independiente de \`beego-staging\`.
