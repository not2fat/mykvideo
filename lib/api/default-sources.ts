import type { VideoSource } from '@/lib/types';

// Default video sources are selected at build time by
// scripts/select-sources.mjs from lib/api/source-profiles/*.json,
// driven by the VOD_PROFILE environment variable (clean | full | dirty).
// The generated file is committed as a clean-profile baseline so that a
// plain `next build` also works; every Pages build regenerates it first.
export { DEFAULT_SOURCES } from './default-sources.generated';
export type { VideoSource };
