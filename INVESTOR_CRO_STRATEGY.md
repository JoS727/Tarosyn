# Tarosyn investor-page CRO strategy

## Conversion brief

- **Audience:** early-stage investors and operators who understand consumer AI, subscription apps, creative identity, spiritual wellness, or community-led products.
- **Objective:** turn qualified curiosity into a direct founder conversation about Tarosyn's planned `$777,000` raise.
- **Primary conversion:** click `Request the investor brief` and start a pre-addressed email to the founder.
- **Secondary conversions:** experience the live product, inspect the public project record, and review the business model or use of capital.
- **Positioning:** Tarosyn is building the memory layer for modern ritual: a tarot and astrology practice designed to become more useful as permissioned context compounds.
- **Proof policy:** use live product artifacts, current pricing, the public project record, and explicit operating goals. Do not invent traction, testimonials, returns, customers, growth, or financing terms.

## Investor journey

| Section | Why it exists | Psychological trigger | Conversion role |
| --- | --- | --- | --- |
| Hero + raise card | Makes the product thesis, target amount, and capital purpose legible in one viewport. | Specificity, processing fluency, selective attention. | Lets the right investor self-qualify immediately and offers a direct founder-contact path. |
| Evidence strip | Shows that Tarosyn is live and has a concrete offer architecture without implying revenue. | Tangibility, numerical specificity, credibility. | Replaces vague startup adjectives with verifiable product and pricing facts. |
| Thesis comparison | Reframes generic spiritual apps as disposable and memory as the compounding advantage. | Contrast effect, loss aversion, category reframing. | Gives investors a memorable reason the product can matter beyond a single reading. |
| Product engine | Shows the wedge, return loop, and expansion surface using real product imagery. | Demonstration, mental simulation, narrative transportation. | Connects the thesis to product mechanics instead of asking investors to believe a slogan. |
| Business model | Makes the free-to-paid-to-expansion path concrete. | Anchoring, commitment progression, monetization clarity. | Shows how the product can earn conversion without claiming unverified performance. |
| Use of capital | Explains why `$777,000` exists and what the sprint is intended to unlock. | Goal gradient, focus, resource-to-outcome mapping. | Converts the raise from a funding request into a focused operating plan. |
| Evidence before adjectives | Confronts the early-stage proof gap directly. | Transparency, skepticism reduction, authority. | Protects trust while sending evaluators to the live product and public record. |
| Investor fit | Describes the pattern recognition and support Tarosyn values. | Identity, affinity, self-selection. | Improves conversation quality by attracting investors who can contribute beyond capital. |
| FAQ | Handles stage, amount, monetization, proof, terms, and next-step objections. | Ambiguity reduction, inoculation. | Removes friction without publishing unsupported or legally sensitive offering details. |
| Final CTA | Restates the ask as a conversation and makes the next step small. | Goal gradient, reciprocity, reduced commitment. | Creates a final conversion point after diligence-oriented visitors finish evaluating the page. |

## CTA strategy

- **Primary:** `Request the investor brief`
- **Product proof:** `Experience the product`
- **Trust proof:** `Read the project record`
- **Objection path:** `Ask the founder`

All primary investor CTAs open a pre-addressed email with prompts for name, firm, and relevant focus. The page does not collect investment commitments, payment, accreditation data, or confidential diligence information.

Every investor CTA includes `data-investor-cta`. `investors.js` emits:

```js
window.dispatchEvent(new CustomEvent('tarosyn:investor-cta', {
  detail: { position, destination }
}));
```

and, when a `dataLayer` exists:

```js
dataLayer.push({ event: 'investor_cta_click', cta_position: position });
```

The primary KPI is **qualified investor conversations per unique page visitor**. Raw email-link CTR is diagnostic; diligence progression is the meaningful signal.

## Claim guardrails

- Do not publish user, revenue, conversion, retention, cohort, market-share, valuation, or growth claims until they are documented and approved.
- Describe milestones as intended operating goals, never guarantees.
- Keep actual financing instrument, valuation, investor qualification, closing mechanics, and return language in counsel-reviewed definitive materials.
- Keep the public product-principle language grounded: reflective, not absolute; personal, not invasive.
- Verify pricing, trial terms, and product availability against the live product before release.

## Public-release gate

The page ships with `noindex,nofollow` and should remain in a draft pull request until Tarosyn confirms its securities-law pathway with qualified counsel. The SEC explains that communications intended to arouse public interest in a capital raise may be viewed as an offer, and unrestricted public websites are a form of general solicitation. Rule 506(b) generally prohibits general solicitation, while Rule 506(c) permits it only when its conditions are met. Regulation Crowdfunding offerings must be conducted through a registered broker-dealer or funding portal.

Before merging publicly, confirm:

1. the intended offering exemption or registration pathway;
2. whether publishing the `$777,000` target is permitted for that pathway;
3. any required accredited-investor verification, legends, filings, state notices, or portal routing;
4. that every public factual claim matches current diligence materials;
5. whether the page should remain `noindex` or become discoverable.

Authoritative references: [SEC general solicitation overview](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/general-solicitation), [SEC Rule 506(c) overview](https://www.sec.gov/resources-small-businesses/exempt-offerings/general-solicitation-rule-506c), [SEC offering pathways](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/offering-pathways), and [SEC Regulation Crowdfunding issuer guidance](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/regulation-crowdfunding-guidance-issuers).

## Recommended experiment backlog

Run only after a lawful public distribution plan is confirmed.

1. Thesis headline: `Fund the memory layer for modern ritual` vs. `Back the ritual app that remembers`.
2. CTA: `Request the investor brief` vs. `Start a founder conversation`.
3. Evidence order: product engine before thesis comparison vs. the current thesis-first journey.
4. Raise framing: `$777K focused sprint` vs. `Founder + AI team runway`.
5. Proof module: public project record only vs. approved cohort and retention evidence when available.
