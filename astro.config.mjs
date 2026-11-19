import { defineConfig } from "astro/config";

// Se puede cambiar al dominio final con PUBLIC_SITE_URL al publicar.
const defaultSite = "https://beego-staging.america-group-roofing-digital-projects.workers.dev";
export default defineConfig({
  site: process.env.PUBLIC_SITE_URL || defaultSite,
  output: "static",
  trailingSlash: "always",
});
