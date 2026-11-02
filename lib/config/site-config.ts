/**
 * Site Configuration
 * Handles environment variables for site branding and customization.
 * Per-deployment branding (name, description, title, icon) comes from
 * lib/config/site-brand.generated.ts, which scripts/select-profile.mjs
 * generates at build time from lib/config/site-profiles.json according to
 * VOD_PROFILE (clean | full | dirty). Explicit NEXT_PUBLIC_ environment
 * variables still take precedence when set.
 */

import { SITE_BRAND } from './site-brand.generated';

export interface SiteConfig {
  title: string;
  description: string;
  name: string;
  icon: string;
}

/**
 * Site configuration object
 * Note: NEXT_PUBLIC_ environment variables are statically embedded at build time
 */
export const siteConfig: SiteConfig = {
  title: process.env.NEXT_PUBLIC_SITE_TITLE || SITE_BRAND.title,
  description: process.env.NEXT_PUBLIC_SITE_DESCRIPTION || SITE_BRAND.description,
  name: process.env.NEXT_PUBLIC_SITE_NAME || SITE_BRAND.name,
  icon: process.env.NEXT_PUBLIC_SITE_ICON || SITE_BRAND.icon,
};
