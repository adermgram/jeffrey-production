import { en, type Key } from './en';
import { tw } from './tw';
import type { Lang } from '../data/site';

export function useT(lang: Lang) {
  return (key: Key): string => (lang === 'tw' ? (tw[key] ?? en[key]) : en[key]);
}
export type { Key };
