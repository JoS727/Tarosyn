# TarosynBrand

The independent corporate entry landing page for **Tarosyn**.

## Purpose

This repository is intentionally a self-contained static site. It does not import the Tarosyn application, make API requests, or depend on application-server availability. The only application dependency is a user-initiated outbound link to `https://tarosyn.app`.

Deploy this repository directly to the static host used by `tarosyn.com` so the brand and entry experience remain online when the application is unavailable.

## Files

- `index.html` — static corporate/brand landing page
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
