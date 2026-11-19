import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const read = (file) => readFileSync(new URL("../" + file, import.meta.url), "utf8");

const home = read("src/pages/index.astro");
const stations = read("src/pages/estaciones.astro");
const layout = read("src/layouts/BaseLayout.astro");
const css = read("src/styles/global.css");
const robots = read("public/robots.txt");

assert.ok(home.includes("Energía que va contigo"), "Debe conservarse el eslogan oficial.");
assert.ok(home.includes("Aún no ofrecemos rentas al público"), "Debe aclararse la etapa preoperativa.");
assert.ok(stations.includes("Estamos desarrollando nuestra red de estaciones en Tijuana"), "No deben simularse estaciones.");
assert.ok(layout.includes("noindex, nofollow"), "Staging debe evitar indexación.");
assert.ok(robots.includes("Disallow: /"), "Staging debe bloquear rastreo.");
for (const color of ["#FCCF01", "#000000", "#FFFFFF", "#171717", "#F5F5F3"]) {
  assert.ok(css.includes(color), "Falta color oficial " + color);
}
console.log("Revisión documental básica: correcta.");
