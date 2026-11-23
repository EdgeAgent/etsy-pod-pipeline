# Shop types — pick one, and the pipeline is pre-configured

This repo is a picker. Six shop types ship as **presets**
(`config/presets/*.json`): each one is a complete starter package —
niche brief, starter product list, price bands from the dated
research (`docs/research-findings-2026-11-23.md`), a pricing config
`pipeline/pricing.py` can run, a listing brief
`pipeline/listing.py` can run, a launch checklist mapped to the
eight stages — plus, since v0.3.0, each preset's **affiliate picks**
and **creation path** (below).

```bash
python3 -m pipeline.presets                    # see the shop types
python3 -m pipeline.presets pet-accessories     # see one, in full
python3 -m pipeline.presets pet-accessories --emit # write its configs
python3 -m pipeline.pricing config/presets/out/pet-accessories.pricing.json
python3 -m pipeline.listing  config/presets/out/pet-accessories.brief.json
```

Picking a preset does not skip judgement: Stage 3's research method
still validates the niche, the publish gate still belongs to the
human, and every preset's example costs are placeholders until real
numbers replace them (each preset file says so, in its `_comment`).

**Start position (Stage 1):** the pipeline assumes you already
have a shop and routes you with two intake questions — shop?
product? No product is a normal answer: every preset's
`creation_path` is the defined route from research to a created,
priced, SEO-packed product slotted into your shop.

## The mixed model — every preset, two lanes

Each preset mixes:

- **(a) Your own original products**, sold on Etsy through the
  eight stages — the preset's `products` list.
- **(b) Affiliate picks** — proven, already-selling third-party
  products in the same niche (the preset's `affiliate_picks`:
  categories + price bands, never invented ASINs), promoted **off
  Etsy** — blog, social posts, link-in-bio, opt-in email — for
  Amazon Associates (or Etsy Affiliates) commission.

**Affiliate links never go inside Etsy** — not in listings,
descriptions, announcements, or messages. Etsy's rules ban
directing buyers off-platform, functionally and completely. The
whole model, with the sourced rules (Amazon's disclosure line, the
real 24-hour/89-day cookie, the no-own-purchases rule), lives in
[`affiliate-model.md`](affiliate-model.md). Read it before
promoting anything.

## The six shop types

### 1. `pod-apparel` — Print-on-Demand Apparel (physical)

The pipeline's original path, Stages 1–8 exactly as written.
Printify prints and ships per order. Starter brand in this repo:
**RiseOrConquer** motivational apparel
(`docs/starter-plan-riseorconquer.md`). Research verdict: micro-niche
or don't bother — generic tees and generic motivational quotes are
the two most saturated shelves on Etsy.

### 2. `digital-downloads` — Digital Design & Pattern Downloads

SVG cut files, patterns, printables — sold as instant downloads.
What changes vs. apparel:

- **Stage 2 is skipped.** No Printify, no provider, no shipping.
- **Delivery is Etsy's**: up to 5 files per listing, 20 MB each,
  filenames ≤70 chars (buyers see them), **no variations** on
  digital listings.
- **`.svg` is not an accepted direct-upload format** — SVGs ship
  inside a ZIP with PNG/DXF. (`.stl` *is* accepted; see type 3.)
- **Fees are the same rates on a smaller base**: price only — no
  shipping charged, no production cost. The calculator runs with
  zero costs.
- **The product must be made/designed by you.** Resold bundles and
  AI prompt lists are prohibited; purely AI-generated functional
  instructions (patterns, recipes) are not allowed — human-authored,
  AI-assisted is the line, with the AI disclosure in the description.
- **Economics are bundle economics**: singles $2–8 build reviews;
  10-design bundles ($15–25) and mega bundles ($25–45) carry margin.

### 3. `stl-files` — 3D-Print Files (STL)

Your own original models (Blender — free, open source — is the
reference tool), sold as STL downloads. What changes vs. apparel:

- **Stage 2 is skipped** for the file lane; fulfilment is the
  buyer's own printer.
- **Stage 4 becomes modelling + test-printing**: you print every
  model yourself before listing it. A model buyers can't print is a
  defect, and its reviews will say so.
- **The June 2025 rule runs this whole shop type**: since
  2025-06-10, Etsy's Creativity Standards require items produced
  with computerised tools to be based on the **seller's original
  design**. Your own models satisfy it by construction — for the
  file *and* for the optional physical-print lane. Bought or free
  files printed as-is do not, even with a commercial licence.
- **Free competition is the pricing enemy**: anything downloadable
  free (flexi dragons, generic stands) has collapsed. Original,
  hobby-specific, problem-solving and personalised models hold
  price.
- **STL price bands are labelled estimates** in the preset — no
  credible public source publishes them (see the findings doc's
  "could not be verified"). Validate with Stage 3 + eBay sold
  listings before betting modelling hours.

### 4. `pet-accessories` — Pet Accessories (physical, partner-made)

Personalised bandanas, collar/tag sets, portraits and mats for a
breed or occasion micro-niche. What changes vs. apparel:

- **Stage 2 still applies** — Printify carries pet products
  (bandanas, beds, mats); engraved collars/tags usually come from a
  specialist partner. Either way the partner is **disclosed** in
  Shop Manager and on the listing, as Etsy requires.
- **The design must be yours** (or the buyer's own personalisation
  on your design). Personalising an unchanged commercial product
  does not make it yours under the Creativity Standards.
- **No pet food or treats. Ever.** Treats are regulated animal
  feed (FDA/AAFCO + state licensing) — a different business, not a
  listing. The preset sells accessories only.
- **No health claims**: Etsy's Prohibited Items Policy bans medical
  claims for any item — no "calming", "anxiety", or pain claims —
  and bans natural fur and cat/dog-derived materials outright.
- Research verdict (findings §E): pet gifting searches **doubled
  YoY** in Etsy's own trend report; personalised collars/tags and
  portraits are the proven sellers; generic bandanas are
  commoditised (more competing listings than searches).

### 5. `digital-templates` — Planners, Resumes, Business Templates

Finished editable **documents** — niche planners, trade-specific
resume systems, business document kits — as instant downloads.
What changes vs. apparel: Stage 2 skipped; delivery is a PDF
carrying the template (or a Canva template link — see below);
pricing at zero cost; bundles/kits carry the margin.

**How this differs from `digital-downloads` (type 2) — they are
not the same shop:**

| | `digital-downloads` | `digital-templates` |
|---|---|---|
| What the buyer gets | Design **assets**: SVG cut files, patterns, printables | Finished **documents**: planners, resumes, business kits |
| What the buyer does with it | Makes things FROM it (cuts, prints, sews) | Customises the words and USES the document itself |
| Core skill | Illustration / vector design | Document & system design |
| Delivery shape | ZIP of files | PDF with files or a Canva template link |
| Signature trap | Franchise bundles (IP) | PLR/MRR re-skins (originality) |

- **Canva's licence shapes delivery**: templates with Canva Pro
  content may only be sold as a **shareable Canva template link**
  (inside your delivery PDF), never as a file; template links need
  a paid Canva plan; Canva's own templates can't be resold as-is.
- **PLR/MRR is not a shortcut**: Etsy's rule asks who *created* it.
  A re-skinned PLR planner fails the original-design standard.
- Research verdict (findings §F): broad terms are a churn market
  (`canva template` ≈ 1.85M listings, median $5.34, tool data);
  the niche version — one brain, one trade, one business type —
  is the entry every 2026 guide converges on.

### 6. `coloring-books` — Coloring Books & Pages (digital)

Printable coloring books in one narrow theme at a time, sold as
PDF downloads. What changes vs. apparel: Stage 2 skipped; Stage 4
is page production + print-testing; the bundle is the product.

- **The AI rule, precisely** (Creativity Standards, 2025-06-10):
  seller-prompted AI creations from **your original prompts** are
  allowed **with disclosure in the listing description** and
  categorised "Designed by a seller". Banned: selling AI prompt
  bundles, and reselling PLR page packs as-is. Etsy publishes no
  hand-editing threshold — human cleanup of every page is this
  pipeline's QC standard because broken line art is what buyers
  refund, not because Etsy counts edits.
- The preset's brief sets `ai_assisted`, so the listing generator
  adds the disclosure line automatically.
- Research verdict (findings §G): a $3–5-median price war at the
  broad end (~541K listings) — narrow themes are the gap
  (`anxiety relief coloring book` ≈ 3,887 listings), bold-and-easy
  cozy is the dominant format, and seasonal packs listed 6–8 weeks
  early are the reliable spike. The same original pages can later
  become a KDP paperback (separate platform, its own AI disclosure
  at publish).

## One shop or several?

Nothing in the pipeline forces one shop per type — but keep the
types in **separate shops** if you run more than one: buyers (and
Etsy's search) reward a coherent catalogue, a shirt buyer is not an
STL buyer, and a takedown or a bad-review streak in one shop
shouldn't sink the others. Each shop still goes through Stage 1's
health check.

## Adding a seventh shop type

Copy the closest preset JSON, keep every required key (the loader
validates: brief must feed `pipeline/listing.py`, pricing must feed
`pipeline/pricing.py`, every product needs a sane price band, and
v0.3.0 presets must carry `affiliate_picks` and a `creation_path`),
run the tests, and add its research to the findings doc — with
sources and dates, or labelled as estimates. A preset without
research is just a guess with good formatting.
