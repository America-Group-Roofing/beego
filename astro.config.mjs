import { defineConfig } from "astro/config";

// Sitio estático y portable. El dominio se establecerá al aprobar la publicación.
export default defineConfig({
  output: "static",
  trailingSlash: "always",
});
