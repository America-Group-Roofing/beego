# BeeGo · Estado y publicación

**Actualizado:** 19 de noviembre de 2026.

## Estado técnico verificado

La conexión GitHub → Cloudflare se encuentra operativa.

| Parámetro | Valor |
|---|---|
| Cuenta Cloudflare | America Group Roofing \| Digital Projects |
| Organización GitHub | America-Group-Roofing |
| Repositorio | beego |
| Rama del Worker staging | develop |
| Directorio raíz | / |
| Comando de compilación | `npm run build` |
| Comando de despliegue | `npm run deploy:staging` |
| Preview builds | Desactivadas |
| Worker | `beego-staging` |
| Plataforma | Cloudflare Workers con Static Assets |
| URL de staging | https://beego-staging.america-group-roofing-digital-projects.workers.dev |

Se corrigió una conexión que inicialmente apuntaba a `main`, que carece de `package.json`. El Worker se renombró de `beego` a `beego-staging` para coincidir con `cloudflare.config.ts`. La ejecución posterior compiló las seis páginas y desplegó correctamente los archivos estáticos.

## Archivos de configuración

- `package.json`: Astro, scripts `build` y `deploy:staging`.
- `cloudflare.config.ts`: Worker `beego-staging`.
- `astro.config.mjs`: salida estática con URLs terminadas en barra.
- `public/robots.txt` y `src/layouts/BaseLayout.astro`: no indexar staging.
- `.github/workflows/validate.yml`: compilación y comprobación de fundamentos.

## Pendientes de calidad

1. Generar `package-lock.json` desde el archivo `package.json` vigente y añadirlo al repositorio para builds reproducibles y caché.
2. Incorporar assets oficiales BeeGo y reemplazar placeholders.
3. Evaluar protección con Cloudflare Access si las vistas de staging contienen material no público.
4. Efectuar pruebas manuales de teclado, navegación, zoom, diseño responsive y accesibilidad.
5. Establecer documentos y canales reales de soporte antes de habilitar formularios u operaciones.
6. Mantener despliegues de pruebas sin habilitar pagos, rentas o estaciones ficticias.

## Límites y seguridad

Esta URL de Workers puede ser accesible a cualquier persona que conozca la dirección. `noindex` y `robots.txt` sólo son señales para buscadores; no son controles de acceso.

**No utilizar `main` como rama de despliegue de este entorno.** No conectar un dominio principal ni publicar comercialmente sin autorización adicional.

No se han creado bases de datos D1, R2, integraciones de pago ni sistemas de renta.
