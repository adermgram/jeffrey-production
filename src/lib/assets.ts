import vibes from '../assets/work/vibes.jpg';
import threeFaces from '../assets/work/three-faces.png';
import glorified from '../assets/work/glorified.png';
import skits from '../assets/work/skits.webp';

export const work = { vibes, threeFaces, glorified, skits };
export const eventArt: Record<string, ImageMetadata> = { 'three-faces': threeFaces, glorified };

// Gallery: every file in src/assets/gallery, sorted naturally. Astro optimises each to webp + responsive sizes.
const files = import.meta.glob<{ default: ImageMetadata }>('../assets/gallery/*.jpg', { eager: true });
export const portraits = Object.entries(files)
  .sort(([a], [b]) => a.localeCompare(b, undefined, { numeric: true }))
  .map(([, m]) => m.default);
