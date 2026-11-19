# BeeGo — Sitio web oficial

Repositorio del sitio web de **BeeGo**, proyecto independiente administrado dentro de la organización **America-Group-Roofing**.

> **Estado del proyecto:** planeación y preparación preoperativa. Este repositorio todavía no contiene el sitio web ni tiene un despliegue configurado.

## Identidad de marca

- **Nombre:** BeeGo.
- **Eslogan oficial e inalterable:** Energía que va contigo.
- **Dirección creativa interna:** Urban Energy Tech (no es un segundo eslogan).
- **Mercado inicial previsto:** Tijuana, Baja California, México.
- **Audiencias:** usuarios de baterías portátiles compartidas (B2C) y establecimientos interesados en incorporar estaciones (B2B).
- **Paleta oficial:** amarillo `#FCCF01`, negro `#000000`, blanco `#FFFFFF`, grafito `#171717` y gris claro `#F5F5F3`.
- **Tipografías del Brand Book:** Montserrat para títulos e Inter para interfaz y lectura.

## Fuentes de referencia

Los documentos de proyecto que guían el trabajo son:

1. **BeeGo Brand Book — Versión 2**: identidad visual y verbal, logotipos, sistema cromático y diseño aprobado del power bank.
2. **BeeGo Documento Maestro — V1**: estado y alcance del negocio.
3. **BeeGo Documento Maestro del Sitio Web — V1**: arquitectura, diseño UX/UI, contenido, accesibilidad, seguridad, SEO y evolución prevista.

Los documentos internos no se publicarán en este repositorio sin revisión y autorización. Las características técnicas del producto, las estaciones, las tarifas y las capacidades del proveedor deben validarse antes de afirmarse comercialmente.

## Alcance web planeado

- Inicio y presentación de BeeGo.
- Cómo funciona, producto y preguntas frecuentes.
- Página para negocios y solicitud de evaluación.
- Información corporativa, contacto y centro legal.
- Página de estaciones: **red en desarrollo** hasta que existan ubicaciones operativas y verificadas.
- Precios, renta mediante QR, pagos, devoluciones, seguimiento de renta y disponibilidad sólo cuando las integraciones y los procedimientos estén comprobados.

## Arquitectura técnica propuesta

- **Frontend:** Astro y estándares web, manteniendo el código portable.
- **Control de versiones:** GitHub, repositorio de BeeGo separado de los demás proyectos de America Group Roofing.
- **Alojamiento objetivo:** Cloudflare, con el mecanismo específico de publicación pendiente de selección.
- **Base de datos y otros servicios:** no incorporar hasta que exista una necesidad validada.

No hay todavía una aplicación Astro creada ni un sitio publicado desde este repositorio.

## Reglas de organización y seguridad

1. Mantener a BeeGo aislado de otros proyectos: repositorio, recursos, dominios, variables de entorno y activos propios.
2. Conservar `main` para trabajo aprobado; preferir ramas y revisiones para cambios nuevos cuando inicie el desarrollo.
3. No publicar claves, contraseñas, tokens, archivos `.env` con valores reales, información personal ni documentos internos.
4. Distinguir en contenidos y documentación: **aprobado**, **propuesto** y **pendiente de verificación**.
5. Respetar la identidad oficial; no reinterpretar el logotipo, el eslogan ni el diseño del power bank.
6. Priorizar experiencia móvil, accesibilidad WCAG 2.2 AA, privacidad, rendimiento, seguridad y SEO.
7. Mantener la posibilidad de migración evitando dependencias innecesarias de un proveedor.

## Etapa actual

Preparación del entorno y documentación inicial. **No iniciar despliegues, pagos, publicación comercial ni integraciones con estaciones sin una decisión posterior explícita.**
