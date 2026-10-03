# Investor Page Design QA

## Visual truth and implementation evidence

- Source visual truth: `../tarosyn-home-reference-1440b.png`
- Normalized implementation comparison: `../investor-page-reference-size.png`
- Desktop implementation: `../investor-page-desktop-iteration-1.png`
- Mobile implementation: `../investor-page-mobile-iteration-1.png`
- Mobile menu state: `../investor-page-mobile-menu.png`
- Mobile FAQ state: `../investor-page-mobile-faq.png`
- Business-model region: `../investor-page-business-iteration-3.png`
- Use-of-capital region: `../investor-page-capital-iteration-4.png`

The source and normalized implementation were compared together at 1280 x 720 CSS pixels and 1x density. The full desktop page was also reviewed at 1440 x 900, with mobile states reviewed at 390 x 844.

## State under test

- Route: `/investors.html`
- Desktop state: page loaded at the hero with navigation visible
- Mobile state: page loaded at the hero with the sticky investor CTA visible
- Interaction states: mobile navigation open/closed, FAQ open, and anchored navigation positions
- Browser state: JavaScript enabled, local static server, no authenticated session required

## Full-view comparison

The 1280 x 720 source homepage and investor hero were viewed side by side in one comparison input. The implementation preserves the source's dark cosmic composition, centered serif display type, warm cream and gold palette, compact navigation, pill CTAs, atmospheric imagery, and restrained spacing rhythm. The investor ask is more prominent by design while remaining within the established Tarosyn visual language.

## Focused-region comparison

- Business model: reviewed at 1440 x 900. The pricing progression, typography, card hierarchy, and spacing are legible and visually consistent with the product page.
- Use of capital: reviewed at 1440 x 900. The three allocation cards and milestone copy maintain clear hierarchy without creating unsupported financial precision.
- Mobile hero: reviewed at 390 x 844. Headline wrapping, image crop, CTA stacking, and sticky CTA remain usable without horizontal overflow.
- Mobile menu and FAQ: reviewed at 390 x 844. Both states are readable, keyboard-dismissable where applicable, and preserve adequate tap targets.

## Fidelity surfaces

- Fonts: DM Sans and Playfair Display match the existing Tarosyn page.
- Spacing: section rhythm, card padding, hero proportions, and navigation offsets align with the existing design system.
- Colors: the implementation reuses Tarosyn's dark plum, cream, muted lavender, and gold accent palette.
- Imagery: existing first-party Tarosyn assets are used at appropriate crops and resolution; no placeholders or fabricated art are present.
- Copy: investor language is concise, specific, and evidence-led. The page does not invent revenue, user, valuation, return, security, or closing claims.

## Interaction and responsive verification

- All nine investor CTAs resolve to an intentional destination.
- Desktop anchor navigation lands below the fixed header.
- Mobile menu opens, reports `aria-expanded="true"`, and closes with Escape.
- FAQ disclosure opens correctly and exposes the financing-terms answer.
- Desktop document width equals viewport width at 1440 pixels.
- Mobile document width equals viewport width at 390 pixels.
- Six images loaded with no broken sources.
- Browser console: no warnings or errors.
- JavaScript syntax: passed `node --check`.
- HTML parse check: passed; only expected HTML5-element warnings from `xmllint` are emitted.

## Findings

- P0: none
- P1: none
- P2: none
- P3: none requiring action

## Comparison history

- Iteration 1: hero, business-model section, use-of-capital section, mobile layout, menu, and FAQ all passed visual and interaction review. No corrective iteration was required.

## Final result

passed
