// Single source of truth for contact + social details.
// Everything here was taken from the previous site / poster; items marked CONFIRM need the client's sign-off.
export const site = {
  name: 'Jeffrey Nortey Productions',
  short: 'JN Productions',
  city: 'Accra, Ghana',
  // CONFIRM: this is the email the old site used for bookings. Replace with the production company's inbox.
  email: 'godfreybrewn@gmail.com',
  whatsapp: '233248070738',
  phoneDisplay: '+233 24 807 0738',
  socials: {
    youtube: 'https://www.youtube.com/@jeffreynortey6854',
    instagram: 'https://www.instagram.com/jeffreynortey1',
    vibes: 'https://www.instagram.com/vibesthemovie',
    facebook: 'https://www.facebook.com/share/19aXf7zJxV/',
    linkedin: 'https://www.linkedin.com/in/jeffrey-nortey/',
    x: 'https://x.com/nortey_jeffrey',
  },
  launchYear: 2017, // YouTube channel joined Oct 2017 (from scrape)
};

export type Lang = 'en' | 'tw';
export const routes = ['services', 'work', 'media', 'gallery', 'events', 'jeffrey', 'contact'] as const;
export type Route = (typeof routes)[number] | '';

export const href = (lang: Lang, route: Route = '') =>
  (lang === 'en' ? '/' : '/tw/') + (route ? route + '/' : '');
