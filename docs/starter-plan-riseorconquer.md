# Starter plan — RiseOrConquer (motivational apparel)

Kevin's actual starting point, chosen **October 2026**: print-on-
demand motivational apparel, no inventory, brand **@riseorconquer /
RiseOrConquer**. The channel/brand name already exists; this plan is
the shop that was decided then and never built. It runs this repo's
eight stages in order, with the specific choices filled in.

## The position

- **Brand:** RiseOrConquer
- **Niche:** motivational / gym-mindset apparel — identity phrases for
  people who train and people building something. (Stage 3 narrows
  this before design #2: gym-first is the launch wedge; "builder/
  hustle mindset" is the adjacent second lane, not a launch mix.)
- **Products at launch:** one unisex tee blueprint + one sweatshirt.
  Two products, done properly, beat twelve done thin.
- **Shop currency:** CAD (Canadian shop), selling to Canada + US.

> **Research check (2026-11-23):** seller-tool data flags *generic*
> motivational quotes as one of Etsy's most saturated, price-raced
> categories — see `docs/research-findings-2026-11-23.md` §A. This
> plan survives that finding only in its narrow form: gym-first,
> identity-specific phrases for a defined audience. If Stage 3's
> scoring (`pipeline/scoring.py`) can't get a design's competition
> score up in the narrow niche, the design doesn't ship — broaden
> the catalogue, never the genericness.

## Launch sequence

| Week | Stage | The work |
|---|---|---|
| 1 | 1. Existing shop | This plan is the appendix case: the **RiseOrConquer** shop doesn't exist yet, so the human creates it once via `docs/appendix-shop-creation.md` (name + fallbacks ready; Etsy Payments + ID verification submitted; set-up fee decision is Kevin's, in-flow), then passes Stage 1's health check. |
| 1 | 2. Printify | Account + payment method; Etsy linked; 2–3 CA/US providers compared on the chosen tee blueprint; primary picked, specs recorded. |
| 1–2 | 3. Research | 10+ proven motivational/gym listings pattern-noted; review mining for buyer words and gaps; first 5 design briefs written (original phrases only). |
| 2 | 4. Design | 5 original designs, full QC. Launch set leans on typography — the brand IS the phrase. |
| 2 | 5. Build | Products built in Printify with REAL catalog costs; calculator run per product, incl. the Offsite Ads case; Kevin decides: price with headroom or opt out of Offsite Ads while under the threshold. |
| 2 | 6. SEO | Listing pack per product (`pipeline/listing.py`), human-reviewed. |
| 2–3 | 7. Publish gate | Kevin approves each product + pack; publish one at a time; read back live; log URLs. **Starter budget: 5 listings × US$0.20 = US$1.00 in listing fees** (plus the set-up fee if Etsy shows one). |
| 3+ | 8. Orders & care | Auto-fulfilment on after first verified listing; weekly review loop starts the first Monday after launch. |

## The first five design briefs (starting points — Stage 3 may swap)

1. **Rise or Conquer** — the brand mark as a phrase design. Varsity/
   bold display type. This is the flagship.
2. **Built Before Sunrise** — early-morning training identity.
3. **Quiet Grind, Loud Results** — two-line contrast type.
4. **Nobody Cares. Work Harder.** — blunt gym humour lane. *(Check
   Stage 3: this sentiment exists in the niche — the WORDING here is
   the brief's own; if research shows this exact phrase is a specific
   seller's coined design, it gets rewritten. The checklist decides,
   not optimism.)*
5. **Day One or One Day** — classic motivational structure, original
   lettering treatment.

Each brief becomes a `config/`-style JSON like
`config/design-brief.example.json` (brief #1 is already there as the
worked example).

## Pricing posture

- Price from the calculator, not from competitors' stickers: their
  fee stack is not your fee stack, and half of them are losing money
  politely.
- Launch target: **≥ C$8 profit per sale** after ALL fees at list
  price (see the Stage 5 worked example: a C$39.95 tee on example
  costs clears C$13.42; the solver price for exactly C$8.00 is
  C$33.92 — real catalog numbers replace the examples at Stage 5).
- Decide Offsite Ads BEFORE the first sale, in writing, in the shop
  log.

## What success honestly looks like

First 90 days is a **proof gate**, not a payday: listings live, SEO
iterating, reviews accumulating, weekly reviews running. The win
condition for the quarter is a **repeatable design pattern** — one
design family that sells weekly — not a revenue number. If the gate
fails, Stage 8's kill criteria say what happens, and the total
exposure was listing fees, the set-up fee if any, and time — no
inventory, ever. That asymmetry is the entire reason this pipeline
exists.
