import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
const read = (p) => readFileSync(new URL("../" + p, import.meta.url), "utf8");
const exists = (p) => existsSync(new URL("../" + p, import.meta.url));
const publicFiles = [
  "src/pages/index.astro", "src/pages/como-funciona.astro", "src/pages/bateria-beego.astro",
  "src/pages/estaciones.astro", "src/pages/negocios.astro", "src/pages/ayuda.astro",
  "src/pages/404.astro", "src/components/Footer.astro", "src/components/Header.astro",
  "src/layouts/BaseLayout.astro"
];
const home = read("src/pages/index.astro");
const stations = read("src/pages/estaciones.astro");
const product = read("src/pages/bateria-beego.astro");
const layout = read("src/layouts/BaseLayout.astro");
const css = read("src/styles/global.css");
assert.ok(home.includes("Energía que va contigo"), "Conservar eslogan oficial");
assert.ok(stations.includes("Aún no hay estaciones disponibles para mostrar"), "No inventar ubicaciones");
assert.ok(layout.includes("noindex, nofollow"), "Mantener staging sin indexación");
assert.ok(read("public/robots.txt").includes("Disallow: /"), "Mantener directivas robots staging");
for (const color of ["#FCCF01", "#000000", "#FFFFFF", "#171717", "#F5F5F3"]) assert.ok(css.includes(color), "Falta color oficial " + color);
for (const name of [
  "beego-hero.webp", "beego-producto-frontal.webp", "beego-producto-lateral-usbc.webp",
  "beego-producto-lateral-boton.webp", "beego-producto-contactos.webp",
  "beego-il-retirar-conceptual.webp", "beego-il-devolver-conceptual.webp",
  "beego-il-encontrar-conceptual.webp", "beego-producto-cables-posteriores.webp",
  "beego-og-inicio.png", "beego-franjas-amarillo.svg"
]) assert.ok(exists("public/assets/" + name), "Asset faltante " + name);
assert.ok(home.includes("beego-il-encontrar-conceptual.webp"), "Imagen IL01 debe estar en H03");
assert.ok(product.includes("beego-producto-cables-posteriores.webp"), "Falta PB03");
const forbidden = [
  /vista de desarrollo/i, /entorno de pruebas/i, /etapa preoperativa/i,
  /sitio en desarrollo/i, /diseño de referencia/i, /especificaciones técnicas por validar/i,
  /pendiente de validación/i, /red en desarrollo/i, /cómo funcionaría/i,
  /formulario.*se activará/i, /imagen conceptual/i, /esta versión/i,
  /red en preparación/i
];
for (const path of publicFiles) for (const rule of forbidden) {
  assert.ok(!rule.test(read(path)), "Texto interno en " + path + ": " + rule);
}
console.log("BeeGo: identidad, recursos, redacción pública y staging verificados.");
