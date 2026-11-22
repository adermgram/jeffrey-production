import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Site URL resolution (so canonical links, share images and the sitemap always match where the site really lives):
//   1. SITE_URL            -> set this in Netlify when the real domain is connected (e.g. https://jeffreynortey.com)
//   2. URL                 -> Netlify's own primary URL (the *.netlify.app address) — used automatically for previews
//   3. fallback            -> the intended production domain
const site = (process.env.SITE_URL || process.env.URL || 'https://jeffreynortey.com').replace(/\/$/, '');

export default defineConfig({
  site,
  trailingSlash: 'always',
  integrations: [sitemap({ i18n: { defaultLocale: 'en', locales: { en: 'en', tw: 'ak' } } })],
});
