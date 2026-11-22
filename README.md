# Jeffrey Nortey Productions — website

Astro static site (English + Twi). Production-company-first; Jeffrey the personality lives at `/jeffrey/`.

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # -> dist/ (deploy to any static host)
```

## Where things live
| What | File |
|---|---|
| Contact details, socials | `src/data/site.ts` |
| Events + **ticketing embed** | `src/data/events.json` (set `tickets.embedUrl` when the ticketing partner is ready) |
| Copy (EN) / Twi draft | `src/i18n/en.ts`, `src/i18n/tw.ts` (missing Twi keys fall back to English) |
| Pages | `src/views/*.astro` (routes in `src/pages/` and `src/pages/tw/`) |
| Brand tokens | top of `src/styles/global.css` |
| Gallery photos | drop `.jpg` into `src/assets/gallery/` (auto-optimised) |
| Social data | `scripts/build_data.py "<scrape folder>"` -> `src/data/social.json` + thumbnails |
| Logo SVG | `scripts/vectorize_logo.py logo/IMG_1709.PNG` -> `public/brand/` |

`legacy/` holds the previous site for reference; delete once the rebuild is approved.

## Deploying (Netlify)
Build `npm run build`, publish `dist` (already set in `netlify.toml`).

| Environment variable | Purpose |
|---|---|
| `SITE_URL` | Real domain once connected, e.g. `https://jeffreynortey.com` (canonical links, share images, sitemap). Not needed for previews — Netlify's own `URL` is used automatically. |
| `PUBLIC_PRODUCTION` | Set to `true` **at launch**. Until then the site is `noindex` and `robots.txt` blocks search engines. |
