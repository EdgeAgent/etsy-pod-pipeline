# Stage 6 — Listing SEO (Etsy's own rules, not folklore)

**Goal:** a complete listing pack for every product — built BEFORE
anything publishes, to the standard Etsy itself publishes in the
Seller Handbook. This stage was rewritten in v0.3.0 from Etsy's
official guidance, read 2026-11-23. Where Etsy and seller-blog
folklore disagree, **Etsy wins** — and the disagreements are called
out, because two of them (tag length, title front-loading) were
wrong in this repo's earlier versions.

**Primary sources** (all Etsy, read 2026-11-23): *The Ultimate
Guide to Etsy Search* (Seller Handbook, Aug 2025); *How Etsy Search
Works* (Aug 2025); *Keywords 101* (Aug 2025); *New Guidance for
Listing Titles* (2026); *How to Use Tags to Get Found in Search*
(Etsy Help); *Checklist: Optimize Your Shop for Etsy Search* (Aug
2025); *Creating Listings That Convert* (Aug 2025). Full citations
in the research log behind this stage.

## How Etsy search actually works (per Etsy)

Two phases, then personalisation:

1. **Query matching** — Etsy takes "a holistic view of your
   listing": **title, tags, attributes, description, categories,
   first photo, reviews**. If your keywords are an exact match for
   the query, the listing "may be ranked higher". No single field
   does the work — the 2026 guidance exists because sellers kept
   stuffing everything into titles.
2. **Ranking** — matched listings are ordered by likelihood to
   sell: **relevance, listing engagement rate** (views → clicks,
   favourites, purchases), **customer-service quality** (review
   average, message response rate, case rate, last 3 months),
   **listing quality** (multiple high-quality photos, policies),
   **recency** (new listings get a small boost for hours-to-days —
   renewing for the boost is, per Etsy, "not an effective
   strategy"), and **shipping price** (a factor; US domestic
   listings under $6 postage are prioritised).
3. **Context Specific Ranking** — results are personalised per
   shopper. Searching for your own listing tells you almost
   nothing; judge by Shop Stats, not by your own searches.

Etsy Plus and Star Seller do **not** directly change organic
placement (Etsy says so). There is no published weighting and no
stated keyword-stuffing *penalty* — Etsy frames stuffing as a
clarity/conversion problem. Write for the buyer; the matching is
holistic.

## Generate the pack

```bash
python3 -m pipeline.listing config/design-brief.example.json
```

Input: a design brief JSON (design phrase, product, audience,
keywords, materials, brand; `delivery_type: "digital"` for
downloads; `ai_assisted: true` adds Etsy's mandatory AI disclosure
line). Output: title, 13 tags, materials, description, FAQ, and
warnings — the IP tripwire **plus the SEO audit** below.

## Keyword research — the method (Etsy's own tools first)

1. **Etsy search-bar suggestions**: type what you sell; the
   suggestions are real popular search terms. Try synonyms the same
   way. (Seller Handbook method.)
2. **Marketplace Insights** (Shop Manager → Stats): real Etsy data
   — searches and listing counts per term for the last 30 days,
   related terms, trending searches. Look for *high buyer interest,
   lower listing count*. **15 searches/week free**; Etsy Plus is
   unlimited.
3. **Shop Stats**: the terms already bringing you buyers — reuse
   the ones you aren't targeting yet, refresh tags on low-traffic
   listings with them.
4. **The brainstorm dimensions** (Keywords 101): descriptive ·
   materials & techniques · who it's for · occasions ·
   solution-oriented · style · size. Work all seven before writing
   a single tag.
5. Third-party tools (eRank/Marmalead-class) are cross-checks only
   — Etsy does not endorse their volume numbers. Directional, like
   all seller-tool data in this repo.

## Title — the 2026 rules

- **Hard limit: 140 characters** (Etsy Help). The generator trims
  at a word boundary, never mid-word.
- **Say what the item is, once.** "State the item clearly — mug,
  dress — just once." Then the **top traits** (colour, material,
  size, the descriptors that decide the click).
- **Consider fewer than 15 words.** Etsy's own contrast:
  *"Dad T-Shirt | Father Shirt | Personalised Father's Day Gift |
  …"* (stuffed) vs *"Personalised 100% Cotton Dad T-Shirt: Custom
  Kids' Names S-XL"* (clear).
- **Don't repeat words.** Etsy's example of waste: "unisex adult
  poncho, unisex cotton poncho".
- **Keep out:** subjective words ("perfect", "beautiful",
  "wonderful" → description), price/sale/shipping text ("on sale",
  "free shipping" → Etsy badges those itself), and **gifting
  phrases** ("gift for him", "birthday present" → those belong in
  tags).
- **Front-load for clicks, not ranking.** Etsy, verbatim in
  substance: *where a phrase sits in your title does not affect
  ranking* — but shoppers see only the first words in results, so
  the item + key trait goes first anyway. (Older Handbook advice
  said front-loading maximised search importance; the Aug 2025 /
  2026 guidance supersedes it.)
- The generator's audit warns on: >15 words, any word repeated 3+
  times, banned filler/sales words, gifting phrases, and the
  primary phrase missing from the first ~55 characters.

## Tags — 13 slots × 20 characters (yes, twenty)

> **Correction:** this repo's v0.1–0.2 said 55 characters. Etsy
> Help says **each tag can contain up to 20 characters** — letters,
> numbers, spaces (`'` and `-` only inside a phrase). The generator
> now enforces 20.

- **Use all 13.** "Each tag you add is an opportunity to be matched
  with a shopper's search."
- **Multi-word phrases in natural language.** "Custom bracelet"
  beats "custom" + "bracelet". Etsy's test: *if you can't imagine
  someone typing it into Google, it shouldn't be a tag.*
- **Long-tail over generic** — specific phrases "tend to convert
  better". A phrase over 20 characters gets split into phrasal
  chunks ("minimalist diamond engagement rings" → "minimalist
  jewellery" + "diamond ring" + "engagement ring").
- **All 13 unique, and diverse** — different angles (the seven
  brainstorm dimensions), not thirteen rewordings of one phrase.
- **Don't repeat your category/attribute phrases as standalone
  tags** — categories and attributes "act like tags" already. A
  word from an attribute can still live inside a multi-word tag.
  (Note what Etsy does *not* say: there is no official rule against
  a title word appearing in a tag. Blog claims otherwise are
  folklore.)
- **Don't** use deliberate misspellings (Etsy redirects common
  typos itself), don't tag in multiple languages (Etsy translates),
  don't sweat plurals (Etsy matches root words).
- **Gifting and aspirational phrases live here** ("gift for her")
  — tags are their home, since titles refuse them.
- The audit warns on: keyword seeds too long to ever be tags,
  single-word tags, and unfilled slots.

## Attributes & materials — the quiet ranking fields

- **Attributes act like tags** and power filtered search: *the
  only way to appear in a filtered result is to carry that
  attribute*. Fill **every relevant attribute**, choose the **most
  specific subcategory** (categories act like tags and unlock more
  attributes), and add the near-synonym option when it's also true
  (Etsy: if it's magenta *and* honestly pink, add pink). Skip
  irrelevant attributes — they describe what the item **is**, not
  what it could be gifted for.
- **Materials:** copy the real spec from the provider — honesty is
  the rule (buyers return lies; "not as described" counts against
  the shop). Be precise about one thing: Etsy does **not** state
  that the free-text materials field affects search matching (its
  matching list names titles, descriptions, tags, categories, and
  attributes). Fill materials for the buyer, not as a secret 14th
  tag.

## Description — it ranks, and it sells

- **Etsy counts description keywords in query matching** (Keywords
  101). Work the primary phrase and its natural variants into the
  **first few sentences**, in your own voice. **Never paste the
  title** or list keywords — Etsy says don't.
- **Structure that converts** (Etsy's pattern + this pipeline's):
  1. The hook: what it is, who it's for, the benefit — first lines.
  2. Essential facts early: sizes/dimensions, colours, materials,
     how to order/personalise.
  3. The honest reality block: made-to-order production time THEN
     transit for physical; **INSTANT DOWNLOAD, no physical item**
     for digital (the generator branches on `delivery_type`).
  4. Returns/defects policy in plain words.
  5. The original-work line — and, when AI assisted, **the
     disclosure line Etsy requires in the description** (the
     generator adds it when the brief sets `ai_assisted`).
- Short paragraphs and bullets beat a wall of text; the story goes
  at the end, the facts at the top.

## Photos — the click is a ranking input

Etsy doesn't rank photo quality directly; it ranks what photos
cause. The **first photo is the search thumbnail** → it drives
**clicks** → clicks/favourites/purchases feed the **engagement
rate** → engagement moves placement. Rules from Etsy: first photo
clearly shows the item, high-resolution (**2000px+ recommended**;
under 635px can show up lower), **no collage, no text overlay, no
collection shot** as the first image; use the full photo set
(current Help: up to 20 photos + 2 short videos — one Handbook
article still says 10; Help is current) with angles, close-ups,
scale and lifestyle shots.

## Hashtags — not an Etsy thing

**Hashtags do not rank Etsy listings.** Etsy never names them as a
search input; `#` isn't even an allowed tag character. Putting
hashtags in a title or description spends characters for nothing.
Hashtags belong to the **social/affiliate side** of this pipeline
(`docs/affiliate-model.md`): on Instagram/TikTok/Pinterest posts
promoting your products, where they work — Etsy's own social team
says it pulls features from **#etsy**. Rule of thumb: *Etsy fields
get keywords; social posts get hashtags.*

## FAQ — pre-answer the inbox

Sizing, ship time, returns for physical; formats, software, licence
for digital (the generator seeds the right set per delivery type).
Add listing-specific ones from Stage 3's review mining — "does it
come in black?" is a FAQ *and* a variant decision.

## The IP tripwire

`pipeline/listing.py` screens the brief for known
trademark/franchise terms and warns loudly. **A warning stops the
listing** until a human clears it against Stage 3's checklist. No
warning does NOT mean cleared — the blocklist is finite, the
checklist is the gate.

## Stage checklist

- [ ] Keyword research done with Etsy's tools (search suggestions,
      Marketplace Insights, Shop Stats) — seeds recorded in the brief
- [ ] Pack generated from a complete brief (no default-only fields)
- [ ] Title ≤140 chars, ≤15 words, no repeated words, no filler/
      sales/gifting phrases, item + key trait first
- [ ] 13/13 tags, each ≤20 chars, all unique multi-word phrases,
      long-tail, drawn from the research
- [ ] Every relevant attribute filled; most specific subcategory
- [ ] Materials copied from the real provider spec
- [ ] Description: keywords natural in the first sentences, facts
      early, delivery reality stated, AI disclosure present if AI
      assisted — reviewed by a human
- [ ] First photo: the item, clear, 2000px+, no collage/text overlay
- [ ] No hashtags anywhere in Etsy fields (they live on social)
- [ ] IP tripwire quiet AND Stage 3 checklist re-run on the final text
- [ ] Pack saved next to the product draft — it is what Stage 7 approves

## Shop-type note

The generator branches by `delivery_type`. **Digital downloads,
templates, STL and coloring books** state INSTANT DOWNLOAD and "no
physical item will be shipped", list the file formats and sizes,
and state licence terms (personal vs commercial use); STL adds the
printer settings your test print used. Digital listings have **no
variations**; bundle variants as files in one listing or list them
separately. **Pet accessories** lead with the personalisation
fields and honest size/safety facts. **Apparel** leads with fit and
the size chart. The AI-disclosure line is required wherever AI
assisted the work, on every shop type.
