# BeeGo · Estado y publicación

## Alcance de esta rama

La rama develop contiene una base inicial de Astro y páginas de contenido **preoperativo**. No es un sitio comercial listo para publicar.

La rama main sigue reservada para trabajo aprobado. Ningún paso de esta preparación debe combinar develop con main automáticamente.

## Componentes por etapa

### A · Preparación
- Contenido institucional y B2B, sin formularios que aparenten funcionar.
- Página de estaciones en desarrollo, sin mapa ni disponibilidad inventada.
- Render del power bank pendiente de integrar desde el asset oficial.
- Sitio de prueba bloqueado para indexación mediante meta robots y robots.txt; esto NO sustituye la autenticación si se necesita restringir acceso.

### B · Piloto operativo
Sólo al validar equipos, tarifas, contratos, métodos de cobro y devoluciones. No implementar hasta aprobación.

## Cloudflare

- Cuenta: America Group Roofing | Digital Projects.
- Proyecto recomendado: **beego-staging**, separado de cualquier proyecto AGR o futuro.
- Plataforma recomendada a noviembre de 2026: Workers con Static Assets (Cloudflare recomienda Workers para proyectos nuevos).
- Construcción Astro: npm run build (salida dist/).
- Publicación desde GitHub: conectar la aplicación **Cloudflare GitHub App** a la organización America-Group-Roofing y permitir acceso sólo a beego.
- Rama para pruebas: develop; **no seleccionar main como rama de publicación de staging**.
- No crear proyecto productivo ni conectar dominio definitivo antes de la revisión.
- Las URL workers.dev / páginas de prueba pueden ser accesibles públicamente. Robots noindex no equivale a control de acceso.

## Faltantes antes de despliegue

1. Instalar dependencias y generar package-lock.json con Node >=22.23.4.
2. Ejecutar npm run check y npm run build con éxito.
3. Revisar los archivos de marca originales y sustituir los placeholders.
4. Aprobar conexión y parámetros exactos de Workers Builds.
5. Verificar HTTPS, rutas, responsive, accesibilidad y que no existan afirmaciones operativas no validadas.

## Compromisos del repositorio

- Sin .env reales, tokens, números de tarjeta, datos personales ni contratos internos.
- No publicar tarifas ficticias, estaciones simuladas, fotos falsas de sedes ni testimonios inexistentes.
- No confundir mockups con interfaz operativa.
