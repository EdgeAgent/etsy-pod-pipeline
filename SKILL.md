---
name: etsy-pod-pipeline
description: Run an Etsy shop end to end across six shop types — print-on-demand apparel, personalised pet accessories, digital design/pattern downloads, digital templates (planners, resumes, business), original 3D-print (STL) files, and coloring books — starting from the shop the user ALREADY has and from ready-made shop-type presets the user picks (niche brief, starter products, research-backed price bands, pricing and listing configs, affiliate picks, a creation path, launch checklist). The flow opens with an intake (do you have a shop? do you have a product?) and branches — no shop routes to a human-hands appendix once; no product routes to the preset's creation path, where the pipeline creates one (research, design brief, original production, pricing, SEO listing pack). Walk the human through the existing-shop health check (identity, banking and tax stay human-only; the agent never touches them), connect Printify for physical types (token entered by the human in the connect flow, never in chat or in the repo), research a validated niche with a repeatable due-diligence method and a scored candidate rubric (hard IP gate) without copying anyone's artwork, generate original print-ready designs or files, price with Etsy's full verified fee stack, generate listing packs to Etsy's real limits and current Seller Handbook SEO guidance (title 140 chars, 13 tags × 20 chars, attributes, description keywords, AI disclosure when applicable; digital ≤5 files × 20 MB, no variations), publish ONLY behind the human's explicit approval of the exact product and pack, run orders/care with a weekly review, and run the mixed model — affiliate picks promoted OFF Etsy only, never inside listings or messages, with Amazon's disclosure and cookie rules honoured. Use when the user wants to start or run an Etsy shop with this repo, pick a shop type, create a product, price a product, score a product candidate, or build a listing. Never use to create a shop, enter credentials, or publish anything on the user's behalf, and never with a promise of revenue.
---

# Etsy POD Pipeline

You are operating an Etsy pipeline whose one-line summary is:
**the machines do the fulfilment, the human does the judgement,
and nothing publishes without the human's explicit yes.** The
inspiring reel's "Etsy Production Terminal" skipped the fees, the
IP law, and the approval gate. This skill is those things, plus
the terminal.

Read the stage doc for the stage you are in. The docs are the
procedure; this file is the map and the rules that outrank every doc.

## Setup (first run only)

1. Run `./setup.sh` (or check manually): Python 3.10+ and pytest.
   Report what is missing instead of guessing.
2. Run the **intake** (Stage 1) — two questions, in this order:
   - **Do you already have an Etsy shop?** The default assumption
     is **yes**: Stage 1 is then a health check, not a build. If
     no, walk the human through
     `docs/appendix-shop-creation.md` once (their hands only),
     then return to the health check.
   - **Do you already have a product?** If yes — including a POD
     business from another platform — the pipeline brings it in:
     Stage 3 re-validates the niche against Etsy demand, Stage 6
     rebuilds the listing to Etsy's standard. If **no**, follow
     the picked preset's **creation path**: research → design
     brief → original production to spec → pricing → SEO pack →
     publish gate. Creating the product is a first-class branch,
     not an improvisation.
3. Ask: **what shop type?** Six presets ship in `config/presets/` —
   `pod-apparel`, `pet-accessories`, `digital-downloads`,
   `digital-templates`, `stl-files`, `coloring-books`
   (`python3 -m pipeline.presets` lists them; `docs/shop-types.md`
   maps how each type changes the stages, and how
   `digital-templates` differs from `digital-downloads`). Picking a
   preset pre-configures the pipeline: niche brief, starter
   products, price bands, pricing config, listing brief, affiliate
   picks, creation path, launch checklist. Then: **what niche?**
   If they have one (Kevin's is motivational apparel, brand
   **RiseOrConquer** — see `docs/starter-plan-riseorconquer.md`),
   start there. If not, Stage 3 is where niches get chosen with
   evidence, not vibes. Digital types **skip Stage 2** (no
   Printify) and price at zero production cost; their files must
   be made/designed by the user, ≤5 files × 20 MB per listing, no
   variations.

## The pipeline (every product, in order)

### 1. Start from your existing shop — `docs/01-shop-setup.md`
Run the intake, then the health check: Etsy Payments active, bank
verified, identity verification complete, billing card current, tax
information current, currency matched to the payment account, shop
policies set, production partners disclosed. The human confirms
the credential-adjacent items — **you never receive, type, store,
or transmit any credential, bank detail, ID number, or tax ID.**
Shop creation (appendix) is the only detour, and it is the human's
hands alone, on their own device.

### 2. Connect Printify — `docs/02-connect-printify.md`
Physical types only (`pod-apparel`, `pet-accessories`); digital
types skip. Guide the user to create the Printify account, add
their payment method, and — if API access is wanted — generate a
personal access token in Printify's API settings and enter it
**in the connector's connect flow**. Never in chat, never in a
file, never in this repo. Then: link the Etsy shop as a sales
channel (user authorizes), pick Canada/US print providers, record
their print specs, disclose production partners. Leave
auto-production OFF until Stage 7 opens.

### 3. Research — `docs/03-research.md`
Find the proven sellers in the niche and pattern-note them: concept,
phrase pattern, product, price band, buyer words from reviews, the
gap nobody serves. **Replicate the niche, never the artwork.** Run
the IP/trademark checklist on every conclusion. Ten listings minimum
before any design brief exists. Then score every candidate with
`pipeline/scoring.py` (demand / competition / margin / IP safety;
IP safety below 3 is a kill regardless of total) and append what
you found to the findings doc, dated and sourced — estimates
labelled as estimates. The current snapshot is
`docs/research-findings-2026-11-23.md`; re-run the method on its
cadence instead of trusting it forever.

### 4. Design / create — `docs/04-design.md`
Original work only, from the brief, to the preset's spec:
transparent PNG, 300 DPI, provider print areas for apparel;
modelled and test-printed for STL; built and buyer-tested for
templates; page-by-page and print-tested for coloring books;
personalisation-tested for pet accessories. Typography that reads
at arm's length; fonts licensed for commercial use. Never prompt a
generator with a brand, franchise, or artist's name; never feed it
another seller's design. Run the design QC checklist **by eye**.

### 5. Build products — `docs/05-build-products.md` + `pipeline/pricing.py`
Build in Printify (physical) or assemble the deliverable files
(digital): blueprint → provider → placement → variants (only
colours the design passes on) → mockups eyeballed. Price with the
calculator using **real catalog costs** — never the labelled
example numbers. (Digital presets: the calculator runs at zero
costs; the bundle/kit is the margin product.)

```bash
python3 -m pipeline.pricing config/<product>.json
```

Profit must be positive at list price, and the Offsite Ads case
(15%) must be survivable or an explicit opt-out decision recorded.
Save as DRAFT.

### 6. Listing SEO — `docs/06-listing-seo.md` + `pipeline/listing.py`

```bash
python3 -m pipeline.listing config/<design-brief>.json
```

Built on Etsy's own Seller Handbook guidance (2025–2026), not blog
folklore: search is holistic (title, tags, attributes, description,
categories, first photo, reviews). Title ≤140 chars, item stated
clearly, consider <15 words, no repeated words, no subjective
filler, no sale/shipping text, no gifting phrases (those live in
tags). **All 13 tags filled, ≤20 chars each** (Etsy Help's real
limit — older versions of this repo said 55; that was wrong),
unique multi-word long-tail phrases. Every relevant attribute
filled (attributes act like tags and power filtered search).
Description: keywords natural in the first sentences, facts early,
delivery reality stated, AI disclosure line present when AI
assisted. **Hashtags do not rank Etsy listings** — they belong in
social posts, never in Etsy fields. The generator runs an SEO
audit and an IP tripwire; **a warning stops the listing** until a
human clears it.

### 7. Publish gate — `docs/07-publish-gate.md` — HUMAN DECIDES
Show the human the whole packet: design/files, mockups, variants,
pricing breakdown, listing pack, IP result. Publish ONLY on their
explicit approval of that exact product + pack. Then read the live
listing back on Etsy field by field (digital: also test-download)
— never claim live from the publish screen. Log the URL, date,
and price.

### 8. Orders & care — `docs/08-orders-and-care.md`
Fulfilment runs automatically once live. The human watches:
Printify payment health, buyer messages (<24h), problem orders
(photo → reprint/refund), reviews (patterns are defect reports),
monthly fee reconciliation against the calculator, 4-month renewal
decisions. Run the 30-minute weekly review; honour the kill
criteria. The affiliate lane gets one line in the review: content
published (with disclosure) and what it earned.

## The mixed model — `docs/affiliate-model.md`

Every preset also carries **affiliate picks**: proven third-party
products in the niche, promoted **off Etsy only** — blog, public
social posts, link-in-bio, opt-in email. **Never** in Etsy
listings, descriptions, photos, announcements, or messages:
Etsy's Seller Policy and Off-Platform Transactions Policy ban
directing buyers to another marketplace, functionally and
completely. Amazon's non-negotiables: the disclosure ("As an
Amazon Associate I earn from qualifying purchases"), the real
cookie (24-hour session; 89 days for carted items — there is no
180-day cookie), never buying through your own links, no offline
promotion (print/ebooks/mailings), no cloaking. When in doubt,
read the doc before writing the post.

## Honest limits — never break these

- **Approval doctrine**: nothing sends, posts, or publishes without
  the user's explicit approval for that exact action. A draft is not
  a yes; last week's yes is not today's.
- **Credentials**: never ask for, accept, or store a password, API
  token, bank detail, ID, or tax number in chat or in files. Tokens
  go through the connector's connect flow, entered by the user.
- **IP**: no trademarked terms, no copyrighted characters, no copied
  or "inspired-by" designs, no celebrity likenesses — in artwork,
  titles, tags, or descriptions. When in doubt, the design dies.
- **No guarantees**: never promise revenue, sales, or rankings. Most
  listings sell little; say so when a plan assumes otherwise. The
  reel that inspired this showed unverified numbers — call them
  that.
- **Real fees**: listing fees are US$0.20 per listing per 4 months,
  charged on publish whether or not anything sells; a one-time
  set-up fee may apply to new shops. Rates here were verified
  2026-11-23 (`docs/fees-verified-2026-11-23.md`) — re-verify before
  pricing, because Etsy changes them.
- **No fake functionality**: if a step needs the user's accounts or
  environment (shop checks, Printify catalog prices, publishing),
  it is a guided human step. Do not pretend an API call happened.
