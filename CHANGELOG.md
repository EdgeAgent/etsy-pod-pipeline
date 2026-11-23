# Changelog

## v0.3.0 — 2026-11-23

The picker grows up: six shop types, a mixed model, an intake,
and SEO rebuilt on Etsy's own guidance — including one correction
of this repo's own earlier error.

- **Three new presets** (six total): `pet-accessories`
  (personalised pet products; no food — treats are regulated
  animal feed), `digital-templates` (planners, resumes, business
  documents — finished documents, positioned distinctly from
  `digital-downloads`' design assets), and `coloring-books`
  (narrow-theme printable books under Etsy's actual AI rule:
  your prompts + disclosure + "Designed by a seller"). Each ships
  with fresh sourced research (findings addendum §E–§G), starter
  products with price bands, and a stage-mapped checklist.
- **The mixed model, every preset**: own products on Etsy plus
  **affiliate picks** (proven third-party categories, never
  invented ASINs) promoted **off Etsy only**. New doc
  `docs/affiliate-model.md` carries the sourced rules: Etsy's
  functional ban on affiliate links in listings/messages/
  announcements, Amazon's disclosure sentence, the real cookie
  (**24 hours / 89-day cart** — the "180-day cookie" is a myth),
  the own-purchases ban, and where promotion legitimately lives.
- **Startup intake + existing-shop reframe**: the flow opens with
  two questions (shop? product?) and branches. Stage 1 is now the
  existing-shop health check; the shop-creation walkthrough moved,
  intact, to `docs/appendix-shop-creation.md`. **No product → the
  pipeline creates one**: every preset carries a `creation_path`
  (research → brief → original production → pricing → SEO pack →
  publish gate), validated by the loader and the tests.
- **SEO rebuilt from Etsy's Seller Handbook (Stage 6 rewritten)**:
  holistic two-phase search, Marketplace Insights / Shop Stats
  keyword method, attributes-as-tags, description keywords,
  first-photo click mechanics, and hashtags honestly placed (they
  don't rank Etsy listings; they live on social).
  - **CORRECTION — tag limit is 20 characters, not 55.** Etsy Help
    is explicit; v0.1–0.2 of this repo (and the generator) were
    wrong. `TAG_CHAR_LIMIT` is now 20, tag generation is
    brief-driven (no more off-category filler tags), and titles
    follow Etsy's 2026 guidance (item stated once, <15 words, no
    repeated words, no gifting phrases or sale text — the title
    formula dropped its "Gift for {Audience}" segment).
  - **SEO audit in `pipeline/listing.py`**: warns on wordy or
    repetitive titles, banned filler, gifting phrases, over-long
    keyword seeds, single-word tags, missing primary phrase in the
    description opening, and a missing AI disclosure. Digital
    briefs now generate a true digital description (instant
    download, files, licence) instead of the apparel text.
- **README to the house standard**: new banner (intake + six shop
  types), true badges, intake section, six-preset table, workflow
  map with the intake node and the mixed-model lane.
- 47 tests, all passing (was 37).

## v0.2.0 — 2026-11-23

The picker release: research becomes a system, and the repo covers
three shop types.

- **Shop-type presets** (`config/presets/`, `pipeline/presets.py`):
  pick a shop — `pod-apparel`, `digital-downloads`, `stl-files` —
  and the pipeline is pre-configured: niche brief, starter products,
  price bands, a pricing config and a listing brief the existing
  tools consume, and a per-stage launch checklist. Presets are
  validated on load; tests prove every preset drives both tools at
  a profit.
- **Due-diligence system in Stage 3**: a repeatable research method
  (sources in order, a re-run cadence) and a candidate scoring
  rubric — demand 35%, competition 25%, margin 25%, IP safety 15%
  with a hard IP gate — implemented as `pipeline/scoring.py`.
- **Dated market findings** (`docs/research-findings-2026-11-23.md`):
  per shop type, sourced and date-stamped — POD saturation map and
  micro-niche bands, digital category price bands and the digital
  rules that differ (≤5 files × 20 MB, no variations, SVG ships in
  a ZIP, made-by-you requirement), the 2025-06-10 Creativity
  Standards original-design rule that defines the 3D-print market,
  and the shared seasonality calendar. STL price bands are recorded
  as **could not be verified**; the preset's bands are labelled
  estimates.
- **Shop-type adaptation notes** added to Stages 2, 4, 5, 6, 7, 8
  and the RiseOrConquer starter plan (which now carries the
  2026-11-23 saturation warning for generic motivational designs).
- 37 tests, all passing (was 23).

## v0.1.0 — 2026-11-23

First release. The whole pipeline, mapped:

- Eight stage docs with checklists: shop setup (human's-hands
  walkthrough), Printify connection, research with the IP/trademark
  gate, design rules + by-eye QC, product building + pricing, listing
  SEO, the publish gate, orders & care with a weekly review loop.
- `pipeline/pricing.py` — the full Etsy fee stack on one sale, plus a
  target-profit price solver. Rates verified 2026-11-23 against
  Etsy's official Fees & Payments Policy and Help Centre
  (`docs/fees-verified-2026-11-23.md`).
- `pipeline/listing.py` — listing-pack generator (title ≤140 chars,
  13 tags × ≤55, materials, description, FAQ) with an IP tripwire.
- Worked starter plan: motivational apparel under RiseOrConquer
  (`docs/starter-plan-riseorconquer.md`).
- 23 tests, all passing.
- Honest limits in the README: no revenue guarantees, the inspiring
  reel's numbers were unverified, fees are real money, shop creation
  is human-only, no trademarked/copycat designs ever.
