# Market research findings — 2026-11-23

A dated snapshot behind Stage 3 (`docs/03-research.md`). Every claim
below carries its source and the date it was read. Seller-tool blogs
(InsightAgent, StableCommerce, Trendlytic, ZIK) sell research tools —
their numbers are **directional, not audited**, and are labelled as
such. Etsy does not publish per-category sales data; anyone quoting
exact category revenue is estimating. Re-run the Stage 3 method
before acting on any of this — demand moves in weeks, not years.

**Researched:** 2026-11-23. **Sources read:** Etsy's Fees & Payments
Policy and Help Centre (via `docs/fees-verified-2026-11-23.md`),
plus the third-party guides cited per section.

---

## A. POD apparel (physical, via Printify)

**What's selling (directional, seller-tool data):**

- Generic tees are the saturated end of the market. Categories
  reported as moving in 2026: personalised home décor (blankets,
  wall art, doormats), sweatshirts/hoodies with niche slogans, mugs,
  ceramic ornaments, journals, and pet products. (Unilink POD guide,
  updated 2026, read 2026-11-23: https://unil.ink/blog/print-on-demand-etsy-2026)
- InsightAgent's listing-data guides (read 2026-11-23) report custom
  t-shirts as the highest-search, highest-competition POD product
  (~300K monthly searches, "very high" competition), hoodies and
  sweatshirts next (~110K searches, high competition), with
  personalised home décor carrying better margins at medium
  competition. Treat the search counts as the tool's own estimates.
  (https://www.insightagent.app/guides/best-selling-print-on-demand-products-etsy/)
- The niches those guides flag as profitable share one shape:
  **identity + occasion** — hobby-specific apparel (pickleball, disc
  golf), pet-breed personalisation, occupation pride below the
  umbrella term (NICU nurse, not "nurse"). Reported price bands:
  hobby apparel $28–45, pet personalisation $24–38, occupation
  $26–42 (USD, tool-reported).
  (https://www.insightagent.app/guides/most-profitable-print-on-demand-niches-etsy/)
- The same source's saturation table is the warning label: generic
  "funny t-shirts", generic pet products, motivational quotes, and
  coffee mugs are the categories with the most active shops and the
  worst price compression (motivational tees reportedly racing to
  $12–15). **This directly affects the RiseOrConquer starter plan:**
  motivational apparel only works micro-niched (a specific audience
  + occasion), never as generic quote tees. The starter plan already
  aims at gym/mindset audiences; keep it that specific.

**Rules that bite in 2026:**

- Etsy requires **AI involvement to be disclosed**, and listings that
  are pure prompt output with no human design work are being
  suppressed, per the Unilink guide (read 2026-11-23). Stage 4's
  human-design + QC-by-eye rules already comply; the disclosure line
  belongs in every listing description.

**Seasonality:** apparel gifting peaks in Q4; sweatshirts/hoodies
skew cold-month. See §D for the shared calendar.

## B. Digital design & pattern downloads

**What's selling (directional):**

- Highest-volume digital categories in 2026, per StableCommerce's
  analysis of live listings (read 2026-11-23): digital planners and
  journals **$8–25**, Canva/social templates **$5–49**, SVG cut files
  **$2–8 singles / $15–40 bundles**, printable wall art **$3–15**,
  wedding/event templates **$8–40**, colouring pages **$2–10**,
  resume templates **$5–18**. The same source is explicit that Etsy
  publishes no granular category sales data — these are price bands
  from live listings, not sales counts.
  (https://stablecommerce.ai/blog/best-selling-digital-products-etsy-2026)
- SVG economics are volume economics: singles are the cheapest
  digital product on the platform, so top sellers bundle. Best-
  selling SVG niches reported by InsightAgent's SVG guide (read
  2026-11-23): profession/occupation, pet/animal, seasonal/holiday,
  quotes/typography, floral. Bundle ladder from the same guide:
  5-design $8–15, 10-design $15–25, 20+ mega bundle $25–45.
  (https://www.insightagent.app/guides/selling-svg-files-on-etsy)
- A live look at Etsy's own SVG search results (2026-11-23) shows the
  category's open secret: a large share of top results are
  franchise/IP bundles (cartoon and game characters) sold at 50–75%
  "discounts" for CA$1.50–3.00. That is infringement stock, not a
  market to join — it is also why original, niche SVG work has room:
  the legitimate shelf is thinner than the raw listing count
  suggests. (https://www.etsy.com/ca/market/svg_files)

**Rules & fees — how digital differs from physical POD:**

- **Same headline fees**: US$0.20 listing (4 months), 6.5%
  transaction, payment processing, Canada's 0.50% regulatory fee —
  but charged on the **price alone**: there is no shipping charged,
  no production cost, no fulfilment. The pricing calculator handles
  this today by passing `product_cost: 0, shipping_cost: 0,
  shipping_charged: 0`. (Etsy Fees & Payments Policy, verified
  2026-11-23 — `docs/fees-verified-2026-11-23.md`.)
- **Delivery limits**: up to **5 files per listing, 20 MB each**;
  filenames ≤70 characters and shown to the buyer; **no variations**
  on digital listings (bundle variants as files, or list
  separately). (Etsy Help rules as summarised by MerchTitans, rules
  checked 2026-11-05, read 2026-11-23:
  https://www.merchtitans.app/blog/best-digital-products-to-sell-on-etsy)
- **Format trap**: `.svg` is **not** on Etsy's accepted direct-upload
  format list (`.stl` is; see §C). SVG sellers deliver a **ZIP**
  containing the SVG/PNG/DXF files. (Same MerchTitans rules summary,
  citing Etsy's accepted-format list.)
- **Originality rule**: digital items must be made or designed by
  the seller. Reselling bought bundles without rights is prohibited,
  and Etsy's Services policy bans curated-list products and
  generative-AI prompt lists outright. (MerchTitans summary and
  Marketsy guide, read 2026-11-23:
  https://marketsy.io/how-to-sell-pdf-file-on-etsy/)
- **AI rule**: AI-assisted work needs the seller's own creative input
  plus a disclosure in the description; per the MerchTitans summary
  of Etsy's rules, purely AI-generated *functional instructions*
  (craft patterns, recipes) are not allowed. Human-authored patterns
  are the product; AI can assist, not author.

## C. 3D-print files (STL) — and physical 3D prints

**The rule that defines this market (verified across three sources,
read 2026-11-23):** on **2025-06-10** Etsy changed its Creativity
Standards: items produced with computerised tools (3D printer, CNC,
laser, Cricut) **must be produced based on the seller's original
design**. Before, a templated/bought design was allowed. Now:

- Your own design, printed by you (or a disclosed production
  partner): **allowed**.
- A bought file with a commercial licence, printed as-is: **not
  allowed on Etsy** — the licence gives the designer's permission;
  Etsy's rule is about whose design it is.
- Free files from Printables/Thingiverse/MakerWorld, printed as-is:
  **not allowed**, even when the licence permits selling elsewhere.
  (Makers/Audja 2026 guide: https://makers.audja.com/blog/what-sells-on-etsy-3d-printed-2026;
  Trendlytic, updated Nov 2026: https://www.trendlytic.io/blog/3d-printed-items-to-sell-on-etsy;
  ZIK Analytics, updated Nov 2026: https://www.zikanalytics.com/blog/top-selling-3d-printed-items-on-etsy/)

**What this means for the STL-file shop type:** selling the *file*
is a digital listing (§B rules: made/designed by you, instant
download). `.stl` **is** an accepted Etsy upload format, 20 MB per
file, up to 5 files per listing — big models ship as ZIP. The
original-design rule is satisfied by construction **if the models
are yours** (e.g. modelled in Blender, which is free and open
source). It also means the physical-print version of this shop only
works with your own models — which is exactly what a file shop
already produces. One modelling hour can feed both listings.

**What's selling (directional):**

- Physical prints that hold price: personalised items (name signs,
  keychains $5–12, pet tags/gear $8–60), problem-solving parts
  (replacement parts/clips, board-game inserts/organisers),
  personalised photo lithophane lamps, hobby-specific tools.
  (Makers/Audja price table, 2026; Trendlytic's 12-item analysis,
  Nov 2026.)
- What's collapsed: articulated flexi animals and generic phone
  stands — anything a stranger can download free and print in an
  hour is a price race to a few dollars. (Trendlytic, Nov 2026.)
- Decorative niches with reported strength: articulated animals
  (saturated for prints, see above), fantasy figurines, garden
  gnomes, desk accessories, themed collectibles (ducks, gnomes).
  (3DCentral print-farm playbook, updated Nov 2026, read 2026-11-23:
  https://3dcentral.ca/growing-etsy-shop-3d-printed-products/)
- Cross-check trick from ZIK: Etsy publishes no sales counts, so
  they validate print categories against eBay sold data (30 days:
  41,120 3D-printed items sold across 2,556 sellers, median $15.61 —
  eBay figures, not Etsy). Use eBay's sold listings as a demand
  cross-check in the Stage 3 method; label it as eBay data.
- Physical-print economics (if you print): true unit cost is
  filament + power + printer wear + 5–15% failed prints + your
  time; sellers who last price at **3–5× total production cost**.
  (3DCentral, Nov 2026.)

**STL file pricing:** no trustworthy public source publishes STL-
specific Etsy price bands (searched 2026-11-23 — see "could not be
verified"). The presets therefore price STL packs inside the §B
digital bands (singles low, bundles carrying the margin) and label
them **estimates to validate with the Stage 3 method**, not findings.

## D. Seasonality (all shop types)

- Etsy is heavily seasonal: Q4 (Black Friday → Christmas) is the
  biggest window; Valentine's, Mother's Day, Halloween, and
  back-to-school are the secondary peaks; January and mid-summer are
  typically quietest. (EtsyOptima selling calendar, read 2026-11-23:
  https://www.etsyoptima.io/features/event-calendar)
- **Publish 6–8 weeks before the peak**, not during it: rankings
  take 3–6 weeks to build. Observed publish windows (InsightAgent
  crawl data, as of 2026-08-21): Christmas ornaments mostly
  published Sep–Nov (busiest October); Halloween décor Jun–Aug;
  fall printables Jun–Sep.
  (https://www.insightagent.app/guides/seasonal-selling-calendar)
- Seasonal search volume is extreme: measured US Google searches
  (DataForSEO via Craftific, fetched 2026-10-24) show Halloween
  printables peaking ~27,100 searches in October vs ~70–140 in
  spring — a seasonal listing is effectively a two-month product
  with a long tail. Digital goods dodge the shipping-cutoff cliff:
  instant delivery keeps selling into the last days before
  Christmas, when physical POD has already missed its deadlines.
  (https://craftific.com/tools/etsy-seller-calendar/)

---

# Addendum — v0.3.0 research (also 2026-11-23)

Three more shop types and the affiliate model, researched the same
way: primary sources where they exist, seller-tool data labelled
directional, gaps named. Plus one correction to the repo itself.

## Correction — Etsy tag character limit is 20, not 55

Versions 0.1–0.2 of this repo stated tags allow 55 characters.
**Wrong.** Etsy Help ("How to Use Tags to Get Found in Search",
read 2026-11-23) states each tag can contain **up to 20
characters** (letters, numbers, spaces; `'` and `-` only inside a
phrase). v0.3.0 corrects the generator (`TAG_CHAR_LIMIT = 20`),
every doc, and every preset brief. The full official SEO picture —
including Etsy's April 2026 title guidance — is in
`docs/06-listing-seo.md`.

## E. Pet accessories

**Demand, Etsy-official:** Etsy's Fall/Winter 2026 Seller Trend
Report (Seller Handbook, data as of 2026-09-14) reports pet
gifting-related searches **doubled year over year** and pet
ornaments **+22%**.
(https://www.etsy.com/seller-handbook/article/1521255894814)

**What's selling (directional, seller-tool/print-provider data):**

- Personalised collars, leashes and engraved ID tags are the
  anchor category — Printify's 2026 best-sellers guide cites a shop
  (AmyEngravedGifts) at **491,000 lifetime sales** on them; custom
  pet portraits cited at **136,000 orders** for one digital
  portrait shop (EditingStudio). Lifetime shop totals, not rates.
  (https://printify.com/blog/best-selling-items-on-etsy/)
- Demand-vs-competition (FitSmallBusiness/Alura, updated
  2026-01-27): personalised collar ~230,200 searches vs ~87,932
  competing listings; custom pet tag ~208,750 vs ~64,375; dog
  bandana ~88,458 searches vs **127,572 competing listings** —
  competition exceeds demand, which is the commoditisation signal.
  (https://fitsmallbusiness.com/best-selling-items-on-etsy/)
- Price bands (USD, directional): collars & tags **$12–40**
  (FitSmallBusiness) / $15–45 (InsightAgent); bandana median
  **$14.66**, 60% of sampled listings $10–25 (RankHero);
  portraits **$20–150+** (InsightAgent) / $30–80 (Unflagged);
  pet-parent sweatshirts **$35–70** (FitSmallBusiness); "new puppy"
  bundles (collar + tag + bandana) exemplified at **$45–65**
  (InsightAgent).
  (https://www.insightagent.app/guides/best-selling-pet-products-etsy)
- Saturation verdicts: generic bandanas commoditised (RankHero:
  "pet bandana" 126,193 competing listings, high competition);
  leashes alone are weak (~26,248 searches vs ~286,511 competition,
  Sale Samurai) next to collars (~513,291 searches). The repeated
  escape route: **breed-specific, occasion-specific, bundled**.
- Cat toys: demand verified only as listing volume on Etsy Canada
  (1,000+ results for felt catnip toys, prices in CAD) — **no
  verified sales ranking or USD band**; the preset does not lead
  with cat toys.

**Rules that bite:**

- Etsy's Prohibited Items Policy (updated 2026-08-11): medical
  claims are banned for *any* item (no "calming", "anxiety relief",
  pain or dental claims on pet products); items from cat/dog parts,
  natural animal fur (mink, fox, rabbit…), and endangered species
  are banned; recalled or hazardous items (choking/strangulation
  hazards — think collar parts and small toy parts) are banned.
  (https://www.etsy.com/legal/prohibited)
- **Pet treats are regulated animal feed, not a normal listing:**
  FDA rules (GRAS/AAFCO ingredients, labelling) plus most US states
  require a business licence and per-product registration, and
  shipping into a state can trigger that state's rules.
  (ShieldMyShop, 2026-06-15:
  https://www.shieldmyshop.com/blog/2026-06-15-selling-pet-treats-dog-food-etsy-fda-aafco-state-feed-license-rules)
  The pet preset therefore sells **no food at all**.
- POD/personalisation: allowed for your own design or the buyer's
  own text/image, made by a **disclosed production partner**;
  reselling unchanged commercial goods is banned, and personalising
  an unchanged commercial item doesn't cure it. (Etsy Creativity
  Standards via Printful/Printify summaries, read 2026-11-23.)

**Seasonality:** year-round base with holiday spikes — pet
stockings/ornaments/bandanas for Christmas, costumes for Halloween;
list seasonal lines 6–8 weeks ahead (the shared calendar, §D).

## F. Digital templates (planners, resumes, business)

**What's selling (directional):** the same four categories repeat
across 2026 guides — niche planners/journals, Canva social
templates (increasingly niche-by-trade), resume/CV systems, and
business documents (invoices, proposals, onboarding, media kits).
(StablesCommerce; Blogora Studio; Marks Insights; EarnWithDesign —
all read 2026-11-23.)

**Price bands (USD, live-listing compilations):** planners
**$8–25**; resumes **$5–18** (RankHero sample median ~$7.97, 73%
of listings under $10); Canva/social packs **$5–49** overall,
niche kits **$10–35**; business templates **$12–45**; branding
kits **$15–47**. (StableCommerce; InsightAgent;
https://www.insightagent.app/blog/best-selling-templates-etsy)

**Saturation, measured from live search (Optimsy, 1 Oct – 4 Nov
2026 — listings count is Etsy's own for the phrase, medians from
the top 100):** `canva template` **1,849,848 listings, median
$5.34**; `printable planner` 934,101 / $4.35; `digital planner`
848,685 / $6.46; `wedding template` 789,263 / $12.36. Broad terms
are a churn market; every guide's stated entry route is the
hyper-specific version (one trade, one brain, one business type).
(https://social.optimsy.com/en/blog/digital-products-to-sell)

**Rules that bite:**

- **Original design, again:** Etsy's Creativity Standards (updated
  2025-06-10) qualify digital downloads only as the seller's
  original content; "a bundle, collection, scan, or PDF of someone
  else's work" expressly does **not** qualify. PLR/MRR licences do
  not cure it — Etsy asks who *created* it, not who may resell it.
  (https://www.etsy.com/legal/creativity/ ; The PLR Store analysis,
  June 2025.)
- **Canva's licence shapes delivery:** Canva content can't be sold
  standalone; existing Canva templates can't be resold as-is; and
  templates containing Canva **Pro content must be sold as a
  shareable Canva template link** (delivered inside a PDF), never
  as a downloadable file. Creating template links requires a paid
  Canva plan. (https://www.canva.com/learn/content-licensing-agreement-explained-stock-images-copyright/)
- **No Etsy-standard buyer licence exists** — each seller states
  their own terms; the norm in live listings is personal/business
  *use* of the document, never resale of the template itself.
- Bundle economics: singles sit at $3–5 medians; kits and systems
  carry the business (EarnWithDesign's ladder, blog guidance:
  mini $7–15 → full kit $37–67; the $47–97 "premium niche" top end
  is single-source and treated as unverified here).

## G. Coloring books & pages

**What's selling:** bold-and-easy / cozy books dominate Etsy's own
best-seller market pages (cozy homes, cats, hygge, spooky-cute),
then adult niches (mandala, floral, swear-word humour, self-care),
kids' animal packs, and seasonal. The standard unit is a 40–100
page themed PDF pack. (Etsy market pages, crawled Nov 2026:
https://www.etsy.com/market/best_selling_coloring_books)

**Price reality (directional, seller-tool live samples):**
`coloring pages` median **$2.99**, `coloring book pdf` median
$3.99, `anxiety relief coloring book` median $4.15 (Optimsy,
Oct–Nov 2026); Kupkaike (2026-11-14): median $4.45, 59% of
listings under $5, rated "Crowded — low opportunity" at ~533K
listings. StableCommerce's guide band: $2–10.

**The narrow-theme gap:** `coloring pages` ≈ **540,659 listings**
vs `anxiety relief coloring book` ≈ **3,887** (Optimsy) — the same
pattern as §F: the theme is the strategy.

**The AI rule — primary source, Etsy Creativity Standards
(updated 2025-06-10, read 2026-11-23):**
(https://www.etsy.com/legal/creativity/)

- "Seller-prompted AI creations" — generated from **the seller's
  original prompts** — are a qualifying category, **with mandatory
  disclosure in the listing description**.
- Expressly NOT qualifying: "a bundle, collection, scan, or PDF of
  someone else's work" and **"AI prompt bundles"** (selling the
  prompts is banned; selling your prompted output, disclosed, is
  not).
- Etsy publishes **no minimum hand-editing threshold** for AI
  images — guides claiming one go beyond the policy text
  (unverified). Human cleanup remains this pipeline's QC standard
  for a different reason: broken line art is what buyers refund.
- Etsy itself names the legitimate print route: "a coloring book
  designed and illustrated by a seller and printed and bound by a
  production partner" qualifies. On **KDP** (separate platform):
  AI-generated images must be declared to KDP at publish even if
  substantially edited (secondary sources quoting KDP Content
  Guidelines, read 2026-11-23; KDP's own help page not opened —
  flagged).
- Debunked, do not cite: viral claims of "17,000+ listings removed
  for AI violations" have no Etsy source (Growtsy, 2026).

## H. The affiliate model — rules research

Full treatment in `docs/affiliate-model.md`. The verified load:

- **Amazon Associates:** disclosure sentence required (Operating
  Agreement §5); cookie = **24-hour session, 89-day cart rule**
  (Commission Income Statement, 2026-04-14) — the "180-day cookie"
  is a myth (180 days = account-review window and a ship-and-pay
  condition); own/family/staff purchases through your links banned
  (§6(u)); offline promotion banned (print, ebooks, mailings —
  §4), while **opt-in** email/SMS/DM links are allowed under the
  current policies; no cloaking/shorteners that obscure the Amazon
  destination (§6(v)/(w)); public, declared sites only (closed
  groups and personal profiles don't qualify). Rates are
  category-based, ~1–5% in these presets' categories, and differ
  between Amazon.com and Amazon.ca.
- **Etsy:** Seller Policy §2(a)(7) + Off-Platform Transactions
  Policy (2026-10-05) functionally ban affiliate links anywhere in
  listings/messages/announcements (directing a purchase to another
  marketplace; QR codes named). Etsy's own Affiliates Policy:
  authorized channels are your approved public socials/blog/site/
  subscriber email; **Etsy Convos and closed groups are expressly
  excluded**; cookie 7 days; earning on your own shop's sales is
  permitted with ownership declared.
- **FTC:** material connections must be disclosed clearly and
  conspicuously, in the content itself (16 CFR 255, rev. 2023).

## What could not be verified

- **STL-specific price bands on Etsy** — no credible public source
  (searched 2026-11-23). Preset prices for the STL shop are labelled
  estimates anchored to the general digital bands in §B.
- **Exact category sales volumes** — Etsy does not publish them.
  Every "X sells Y per month" figure in third-party guides is a
  tool estimate; this doc cites them as directional only.
- **Printify's live catalog prices** — still not reachable (see
  `docs/fees-verified-2026-11-23.md`); Stage 5 keeps using labelled
  example costs until the connector is connected.
- **Addendum gaps (v0.3.0):** cat-toy USD price bands and any
  Etsy-official pet subcategory sales ranking (none exists — all
  rankings are seller-tool directional except Etsy's own trend
  report); the top end of branding-kit prices ($47–97, one blog
  source); Corjl/Templett current subscription prices (their own
  pricing pages not opened); a "how much editing makes PLR/AI work
  original" threshold (Etsy has published none); the materials-field
  count and any search effect for the free-text materials field
  (not stated in the Etsy sources read — see Stage 6); seller
  revenue examples in template/coloring guides (marketing copy, no
  receipts).
