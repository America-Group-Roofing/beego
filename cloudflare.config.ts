import { defineConfig } from "cf/config";

// Entorno exclusivo de BeeGo. No desplegar una versión comercial a producción.
// Cloudflare CLI cf sirve los archivos precompilados de Astro desde ./dist.
export default defineConfig({
  worker: {
    name: "beego-staging",
    compatibilityDate: "2026-11-19",
  },
});
