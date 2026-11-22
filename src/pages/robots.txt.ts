import type { APIRoute } from 'astro';

// Search engines are blocked until the site is launched: set PUBLIC_PRODUCTION=true in Netlify to open it up.
export const GET: APIRoute = ({ site }) => {
  const live = import.meta.env.PUBLIC_PRODUCTION === 'true';
  const body = live
    ? `User-agent: *\nAllow: /\n\nSitemap: ${new URL('sitemap-index.xml', site).href}\n`
    : `User-agent: *\nDisallow: /\n`;
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
