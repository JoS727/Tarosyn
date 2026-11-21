# Tarosyn — tarosyn.com brand site

The independent static extraction of Tarosyn's existing public **Guest Onboarding** landing page.

## Purpose

This repository is intentionally a self-contained static site. It faithfully carries the current Tarosyn Guest Onboarding landing content and visual hierarchy, but does not import the Tarosyn application, make API requests, or depend on application-server availability. Entry and returning-seeker actions are deliberate outbound links to `https://tarosyn.app`.

Deploy this repository directly to the static host used by `tarosyn.com` so the brand and entry experience remain online when the application is unavailable.

## Files

- `index.html` — static corporate/brand landing page
- `project.html` — public living project record: charter, product focus, priorities, and accountability rules
- `project.css` — styles for the public project record
- `styles.css` — all styling; no build required
- `script.js` — mobile navigation, progressive reveals, FAQ behavior, and CTA measurement hooks
- `CRO_STRATEGY.md` — conversion rationale, section psychology, CTA measurement plan, claim guardrails, and experiment backlog
- `assets/` — local Tarosyn brand assets copied from the app's public asset library
- `robots.txt` and `sitemap.xml` — crawler discovery for `tarosyn.com`
- `llms.txt` — one-file summary, pricing and page map for AI answer engines
- `what-is-tarosyn/` — canonical description page (definition, pricing, platforms, FAQ) written to be quotable
- `compare/` — comparison hub plus `compare/co-star/` and `compare/the-pattern/`, each describing the competitor only through its own published positioning
- `site.webmanifest` — browser/app identity metadata
- `404.html` — branded not-found page
- `_redirects` — Cloudflare Pages redirects (`/wiki` → `tarosyn.app/wiki`)
- `_headers` — Cloudflare Pages security headers, asset caching, and `noindex` for raw brand-storage folders
- `legal/` — published legal policies (`legal/legal.css` styles them; use root-absolute asset paths such as `/styles.css`)
- `legal.zip` — archive of `legal/` (regenerate with `zip -qr legal.zip legal` after legal edits)
- `tools/check-site.py` — link, sitemap, and file-size checks (run in CI: `python3 tools/check-site.py`)
- `tools/webpify.mjs` — one-off asset utility
- `assets/analytics.js` — GA4 (`G-BZFQJ5J4Y5`, shared with tarosyn.app, cross-domain linked) with Consent Mode defaults; loaded on every page
- Unused brand storage (deck art, logo frames, root PNGs, card borders) was moved to the `archive/brand-assets-2026-11` branch — see its `ARCHIVE_README.md` to restore a file

## Pricing source of truth

Plan names, prices, and Kuu$ allowances on this site must match the app (`JoS727/Tarosyn-Production`: `shared/contracts/tiers.ts` and the tier-settings defaults in `server/routes.ts`). Live tiers, read from `GET /api/tier-settings` on 2026-11-20: Seeker (free, 0 Kuu$), Mystic ($4.99/mo, $25/yr, 40 Kuu$/mo), Seer ($9.99/mo, $83.99/yr, 100 Kuu$/mo), Creator ($29.99/mo, $219.99/yr, 400 Kuu$/mo), Angel ($99/mo, $999/yr, 1,000 Kuu$/mo). Retired aliases that must not be marketed: Founder, Grand Master.

## SEO and discovery

The landing page includes a canonical URL, index/follow crawler directives, keyword and description metadata, Open Graph and Twitter cards, and JSON-LD for the Tarosyn organization, website, and web application. All share-image and schema URLs intentionally resolve on `tarosyn.com`, so deploy this site at that hostname before submitting the sitemap to search engines.

## Deployment

Publish the repository root as a static site. No build command, server runtime, environment variables, API keys, or app routing are required.

Recommended domain structure:

- `tarosyn.com` → this static TarosynBrand deployment
- `tarosyn.app` → the Tarosyn application

This separation keeps the public entry page independently available during application outages.
