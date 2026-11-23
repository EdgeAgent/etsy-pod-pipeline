# Stage 3 — Research (the "Competitor Replication Lab", done legally)

The reel that inspired this pipeline showed a "Competitor Replication
Lab" that copies competitors' best-selling products. Here is the
honest version of that idea — and the line it must never cross:

> **You may replicate a validated NICHE, a product category, and a
> design CONCEPT (a funny phrase style, a layout idea, a theme).
> You may never replicate someone's artwork, wording, or branding.**

Copying a design is copyright infringement; copying branding is
trademark infringement; Etsy bans shops for it, and "the AI made it"
is not a defence. Research tells you **what buyers want**. Stage 4
makes something **original** that serves that want.

## The research method

1. **Pick the niche before the design.** A niche is an audience +
   occasion + style ("gym humour for nurses", "fishing dads,
   Father's Day"). Broad niches ("funny shirts") are where beginners
   drown.
2. **Find proven demand.** On Etsy, search the niche's phrases and
   look for:
   - Listings with **hundreds+ reviews** and recent review dates
     (proof of ongoing sales, not a 2021 spike).
   - Shops with a **coherent catalogue** in the niche (they survive
     because the niche pays).
   - "Bestseller" / "Star Seller" badges on niche listings.
   - Review text: buyers tell you the exact words, occasions, and
     complaints ("wish it came in black", "bought for my brother").
3. **Record patterns, not products.** For each strong listing note:
   the *concept* (e.g. "retro sunset + bold varsity text"), the
   *phrase pattern* (short, punchy, identity-based), the *product*
   (tee vs. sweatshirt), the *price band*, and the *occasions* in its
   tags. Ten listings minimum before you conclude anything.
4. **Check the gap.** What do reviews ask for that listings don't
   offer? A phrase angle nobody's using, an underserved sub-audience,
   a colour/size gap. The gap is where an original design wins.
5. **Write the brief.** One page: niche, audience, occasion, concept
   direction, phrase ideas (YOUR words), price band, and the pattern
   notes. That brief feeds Stage 4 and Stage 6 — never a screenshot
   of someone's design.

## The due-diligence system — research as a repeatable method

The method above is per-niche. This section makes it a **system**:
the same sources, the same signals, the same scoring, re-run on a
cadence — so "what's selling and what isn't" is a maintained answer,
not a vibe from the day you opened the shop. The current findings
live in `docs/research-findings-2026-11-23.md` (dated, sourced);
this is the method that produced them.

### Sources to check (in order)

1. **Etsy itself** — search the niche's phrases; pattern-note 10+
   listings (reviews count + recency, badges, price band, shop
   coherence). This is the primary source; everything else is a
   cross-check.
2. **Review text** — buyers state unmet wants in plain words; that
   is your gap list.
3. **Seller-tool blogs** (InsightAgent, eRank/Marmalead-class tools)
   — search-volume and competition estimates. Directional only:
   they sell tools, and Etsy publishes no category sales data.
4. **eBay sold listings** — for categories Etsy data can't verify
   (notably 3D prints/files), eBay's *sold* prices are real
   transactions. Label them as eBay data, never as Etsy data.
5. **Etsy's own policy pages** — fees and the Creativity Standards
   change (the June 2025 original-design rule redrew the 3D-print
   market; the June 2026 fee revisions moved margins). Re-read them
   every re-run; `docs/fees-verified-2026-11-23.md` is the pattern
   for how to record what you find.

### Signals to score — the candidate rubric

Every candidate product gets scored 0–5 on four signals, with
`pipeline/scoring.py` doing the arithmetic:

| Signal | Weight | 5 looks like | 0 looks like |
|---|---|---|---|
| **Demand** | 35% | Comparables with hundreds of recent reviews, bestseller badges, rising searches | No reviewed sellers; a 2021 spike and silence since |
| **Competition** (room to enter) | 25% | Few, weak listings own the niche; no dominant shop | A saturated wall of strong shops (generic tees, franchise SVG bundles) |
| **Margin** | 25% | Calculator leaves healthy profit mid-band, Offsite Ads case survivable | Profit only at the band's top price, or negative with ads |
| **IP safety** | 15% + **hard gate** | Your words, your art, clean by construction | Leans on a brand, character, or someone's coined phrase |

Verdicts: weighted ≥3.5 **strong** · ≥2.5 **test** (one listing,
watch it) · below **pass**. **IP safety below 3 is a kill, whatever
the total** — the scorer enforces it, because the checklist below
is a gate, not a suggestion.

```bash
python3 -m pipeline.scoring candidates.json   # {"candidates":[{...}]}
```

### Re-run cadence

- **Before any new product line** — full method, new findings dated
  and appended to the findings doc (never edit old findings into
  "current" ones; date a new section).
- **Monthly** — refresh the price bands and saturation calls for
  your live niches; seasonal listings get planned 6–8 weeks ahead
  of their peak (Q4, Valentine's, Mother's Day, Halloween,
  back-to-school — see the findings doc §D).
- **On any Etsy policy email** — rules and fees are research inputs,
  not fine print.

### The same method, per shop type

- **POD apparel** (`pod-apparel` preset): demand = reviewed niche
  listings; the saturation check matters most — generic tees and
  generic motivational quotes fail the competition signal by
  default and must be micro-niched to score at all.
- **Digital downloads** (`digital-downloads` preset): score
  **bundles**, not singles (singles are review-builders). Check the
  format rules as a research input: ≤5 files/20 MB, no variations,
  SVG ships in a ZIP. A top search result full of franchise bundles
  is an IP-safety data point, not demand proof.
- **3D-print files** (`stl-files` preset): Etsy publishes no sales
  data and STL price bands are unverified — cross-check demand on
  eBay sold listings, and treat "is it downloadable free?" as a
  competition-signal cap: if the model (or a near-twin) is free on
  Printables/Thingiverse, the candidate cannot score above 2 on
  competition.
- **Pet accessories** (`pet-accessories` preset): score the
  *breed/occasion version*, never the generic product — the
  research (findings §E) shows competition exceeding demand for
  generic bandanas while personalised collars/tags keep a healthy
  demand:competition ratio. Treats and health claims are not
  research candidates at all — they're excluded by law and policy
  before scoring.
- **Digital templates** (`digital-templates` preset): score the
  niche version against the broad term's listing count (Marketplace
  Insights shows both). If your candidate is describable by the
  broad term alone ("planner template", ~934K listings), it fails
  competition by default; the trade/brain/business-type version is
  the candidate. PLR availability of a similar product is an
  IP-safety data point, not a shortcut.
- **Coloring books** (`coloring-books` preset): score one narrow
  theme at a time and read the median price before the demand
  signal — in a $2.99–4.45-median category, margin comes from the
  bundle and the theme's thin competition, not from volume hopes.
  Seasonal themes get researched 3+ months out so they can list
  6–8 weeks ahead of the peak.

## IP / trademark safety checklist — run before EVERY design

- [ ] No brand names or logos (sports leagues, car brands, bands,
      fashion houses, tech brands) — in the artwork, the title, the
      tags, anywhere.
- [ ] No copyrighted characters or franchises (movies, anime, games,
      cartoons, book series) — including "inspired by", silhouette,
      and parody versions. Parody is a courtroom argument, not a
      business plan.
- [ ] No celebrity names, faces, or catchphrases.
- [ ] No copied phrases from an existing listing. A generic idiom
      ("best dad ever") is different from a seller's distinctive
      coined phrase — when in doubt, write your own.
- [ ] No team/school/military insignia or seals.
- [ ] Fonts and any stock elements are licensed for **commercial use**
      (check the licence; "free download" ≠ commercial rights).
- [ ] The design would still make sense with the niche's biggest
      brand's name removed — because it is removed.
- [ ] `pipeline/listing.py`'s IP tripwire passes on the brief (it's a
      tripwire, not clearance — this checklist is the gate).

Etsy enforces IP hard: rights holders file takedowns, Etsy counts
them, and repeat strikes close shops permanently — including shops
that "didn't know". There is no stage in this pipeline where copying
is the fast path.

## What "validated" honestly means

A niche with active, reviewed sellers is evidence that **someone**
makes money in it. It is not evidence that **you** will — your design
still has to be good, your SEO still has to land, and most listings
in any niche sell little. Research raises your odds; it does not
issue guarantees (see the README's honest limits).

## Stage checklist

- [ ] Niche defined as audience + occasion + style
- [ ] 10+ proven listings pattern-noted (concept, phrase pattern,
      product, price band — no screenshots of artwork as "templates")
- [ ] Review mining done: buyer words + unmet wants recorded
- [ ] The gap identified in one sentence
- [ ] Every candidate scored with `pipeline/scoring.py` — IP gate
      honoured, kills actually killed
- [ ] One-page design brief written, in your own words
- [ ] IP checklist understood — it runs again at Stage 4 and Stage 6
- [ ] Findings appended to the findings doc, dated and sourced
      (estimates labelled as estimates)
