# TarosynBrand

The independent static extraction of Tarosyn's existing public **Guest Onboarding** landing page.

## Purpose

This repository is intentionally a self-contained static site. It faithfully carries the current Tarosyn Guest Onboarding landing content and visual hierarchy, but does not import the Tarosyn application, make API requests, or depend on application-server availability. Entry and returning-seeker actions are deliberate outbound links to `https://tarosyn.app`.

Deploy this repository directly to the static host used by `tarosyn.com` so the brand and entry experience remain online when the application is unavailable.

## Files

- `index.html` — static corporate/brand landing page
- `project.html` — public living project record: charter, product focus, priorities, and accountability rules
- `project.css` — styles for the public project record
- `styles.css` — all styling; no build required
- `script.js` — mobile navigation only
- `assets/` — local Tarosyn brand assets copied from the app's public asset library
- `robots.txt` and `sitemap.xml` — crawler discovery for `tarosyn.com`
- `site.webmanifest` — browser/app identity metadata

## SEO and discovery

The landing page includes a canonical URL, index/follow crawler directives, keyword and description metadata, Open Graph and Twitter cards, and JSON-LD for the Tarosyn organization, website, and web application. All share-image and schema URLs intentionally resolve on `tarosyn.com`, so deploy this site at that hostname before submitting the sitemap to search engines.

## Deployment

Publish the repository root as a static site. No build command, server runtime, environment variables, API keys, or app routing are required.

Recommended domain structure:

- `tarosyn.com` → this static TarosynBrand deployment
- `tarosyn.app` → the Tarosyn application

This separation keeps the public entry page independently available during application outages.
