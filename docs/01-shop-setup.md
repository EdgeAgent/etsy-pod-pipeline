# Stage 1 — Start From Your Existing Shop

**Goal:** a shop that's actually ready to sell from — verified,
configured, and matched to the shop type you picked.
**Assumption:** **you already have an Etsy shop.** That's the
default path. If you don't, this stage routes you to the appendix
walkthrough once, and then you come back here.

## The intake — two questions, answered first

Everything in this pipeline branches on these. Answer them before
touching a setting:

### Q1. Do you already have an Etsy shop?

- **Yes** → run the health check below. Most existing shops need
  two or three fixes, not a rebuild.
- **No** → do the one-time walkthrough in
  [`appendix-shop-creation.md`](appendix-shop-creation.md) (your
  hands only — identity, banking, tax), then return here and run
  the health check.

### Q2. Do you already have a product?

- **Yes — a product or a whole POD business elsewhere** → you're
  bringing it into Etsy. Skip ahead: Stage 2 connects Printify (or
  confirms your production partner), Stage 3 validates the niche
  against Etsy demand anyway (a product that sells on your own site
  still needs Etsy's evidence — and Etsy's original-design rule
  applies to it: it must be *your* design, or the buyer's own
  personalisation), and Stage 6 rebuilds its listing to Etsy's SEO
  standard. Don't copy a listing from another platform verbatim —
  Etsy's search is its own system (Stage 6).
- **No** → **the pipeline creates one with you.** Every preset
  carries a `creation_path` — the defined route for its shop type:

  1. **Stage 3 research** names the niche and the gap, and scores
     the candidate (`pipeline/scoring.py`; the IP gate is a kill).
  2. **Design brief** — your concept, your words, your art
     direction, written before anything is generated.
  3. **Original production** to the preset's spec (Stage 4): a
     300-DPI transparent PNG for apparel, a tested model file for
     STL, a buyer-tested template for digital templates, a
     print-tested PDF for coloring books.
  4. **Build + price** (Stage 5) with `pipeline/pricing.py` on real
     costs — the preset's example costs are placeholders until then.
  5. **Listing pack** (Stage 6) with `pipeline/listing.py` — the
     full SEO treatment — then the **publish gate** (Stage 7) slots
     it into your picked shop. Nothing publishes without your yes.

  Creating the product is a first-class branch of this pipeline,
  not an afterthought — most readers start here.

### Q3 (routing). Which shop type?

If you haven't picked, pick now: `python3 -m pipeline.presets`
lists the six. The preset pre-configures everything downstream
(products, price bands, configs, checklist) — see
[`shop-types.md`](shop-types.md).

## The existing-shop health check

Run it once per shop, and again whenever Etsy emails about policy
or payments. Every item is a setting or a fact, not a project:

- [ ] **Etsy Payments is active** and the **bank account is
      verified** (Shop Manager → Finances). Bank details must be
      added within 30 days of the first sale and verified within
      60, or Etsy can suspend the shop.
- [ ] **Identity verification is complete** — not "submitted",
      complete. (Human's hands only, always; the agent never sees
      an ID, a bank number, or a tax ID.)
- [ ] **Billing card on file** and current — it's what Etsy charges
      fees to when your balance doesn't cover them.
- [ ] **Tax information is current.** Canadian sellers include any
      seller-responsible taxes in listing prices — the pricing
      calculator (Stage 5) works tax-inclusive. (General
      information, not tax advice; your GST/HST situation is yours
      to confirm.)
- [ ] **Currency matches your payment account** — listing in a
      different currency costs a 2.5% conversion fee per sale.
      Canada-based, selling to Canada/US: CAD shop, CAD account.
- [ ] **Shop policies are set**: shipping/processing times that are
      honest for made-to-order, a returns policy that matches what
      the listing templates promise (defects always made right).
      Etsy counts shop policies and customer-service quality in
      search placement (Stage 6) — this is an SEO setting too.
- [ ] **Production partners are disclosed** (Settings → Production
      partners) for any POD/partner-made product — Etsy requires
      it, and the listing itself must disclose it too.
- [ ] **Shop name, icon and About tell one story** — the niche you
      picked, not three niches you used to sell. Buyers and Etsy's
      search both reward a coherent catalogue (see
      `shop-types.md` on keeping shop types in separate shops).

## What it costs to exist (verified 2026-11-23 — see fees doc)

| Item | Cost |
|---|---|
| Listing fee | **US$0.20 per listing**, per 4 months, charged whether or not it sells |
| One-time set-up fee | New shops only; varies by location; shown during setup (appendix) |
| Etsy Plus (optional) | US$10/month — skip it at the start |

Full fee stack: [`fees-verified-2026-11-23.md`](fees-verified-2026-11-23.md).

## Hard rules for this stage

- The agent **never** enters, receives, stores, or transmits:
  passwords, banking details, government ID numbers, or tax IDs.
  Health-check items that touch them are confirmed by the human
  ("done"), never shown to the agent.
- An existing shop with a **policy strike history** is a fact to
  know at intake, not a detail to discover at the publish gate —
  IP strikes compound, and repeat strikes close shops permanently.

## Stage checklist

- [ ] Intake answered: shop? product? shop type?
- [ ] No shop → appendix walkthrough completed by the human
- [ ] Health check passed, every box above
- [ ] Product branch chosen: **bringing one in** (→ Stage 2/3) or
      **creating one** (→ the preset's creation path, Stage 3 first)
- [ ] Zero listings published from this stage — publishing is
      Stage 7, behind the gate
