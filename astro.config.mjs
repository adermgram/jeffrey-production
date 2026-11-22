import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// TODO: set to the real production domain before launch
export default defineConfig({
  site: 'https://jeffreynortey.com',
  trailingSlash: 'always',
  integrations: [sitemap({ i18n: { defaultLocale: 'en', locales: { en: 'en', tw: 'ak' } } })],
});
