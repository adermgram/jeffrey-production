# Jeffrey Nortey — Official Website

A fast, self-contained multilingual website built from the Claude Design handoff.
No build step, no framework, no dependencies — just static files.

## Run it

Because the hero uses background videos, open it through a web server (not `file://`):

```bash
cd jeffrey-nortey-site
python3 -m http.server 8000
# then open http://localhost:8000
```

Any static host works too (Netlify, Vercel, GitHub Pages, Cloudflare Pages, S3…):
just upload the whole folder — `index.html` is the entry point.

## What's inside

- `index.html` — page shell, fonts, meta/SEO tags, CSS theme tokens
- `app.js` — the whole site: routing, 7-language content, theme + language
  switch, hero video crossfade, modals, forms, animations
- `assets/` — photos, project posters, logos, favicon
- `uploads/` — the 9 hero background video clips
- `robots.txt`, `sitemap.xml`, `LLMs.txt` — as shipped in the handoff

## Features

- **Pages** (hash routing): Home, About, Work, Comedy, Music & Poetry, Faces,
  Collaborate, Gallery, Press, Events, Contact, Privacy, plus a 404 page.
- **7 languages**: English, Twi, French, Spanish, Portuguese, 中文, 日本語
  (with Noto Sans SC/JP for CJK). Choice is remembered.
- **Light / dark theme** toggle, remembered between visits.
- **Auto-rotating** hero role words and press quotes; scroll-reveal animations;
  crossfading video background on the home hero.
- **Booking modal** and enquiry forms that build a pre-filled email to
  godfreybrewn@gmail.com.
- SEO: per-page `<title>`/description, Open Graph, Twitter cards, JSON-LD.

## Notes

- Small emoji icons (faces, awards, values) load from `emojicdn.elk.sh`, exactly
  as in the original design. They need an internet connection to appear.
- Fonts load from Google Fonts.
- To change any text, edit the `DICT` object at the top of `app.js` — every
  language lives there.
