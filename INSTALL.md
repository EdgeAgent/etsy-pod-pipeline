# Install

Two ways in. Both end at the same place: Stage 1's intake — do you
have a shop (assumed yes; the pipeline health-checks it), do you
have a product (if not, your preset's creation path makes one) —
with a shop type picked (start with `python3 -m pipeline.presets`
— see `docs/shop-types.md`), a niche picked, and the checklists in
front of you.

**Requirements** (both paths): Python 3.10+. That's it — the toolkit
is standard library only. pytest is optional, for the tests. The
pipeline itself additionally needs an Etsy shop (assumed to exist;
creating one is a one-time human-hands appendix) and — for the
physical shop types only (apparel, pet accessories) — a Printify
account (free plan), created by the human at its stage, never by a
script. Digital shop types need no Printify account.

---

## Path A — "Give it to your Muse" (recommended)

This repo is a one-shot package for an AI agent (Meta Muse, or any
agent that reads skill files):

1. Clone or download this repo.
2. Open your agent in the repo folder and point it at **`SKILL.md`**
   (the skill is also registered in `skill.yaml`).
3. Answer the intake and name your shop type and niche —
   *"I have a shop, no product, pet accessories for Goldendoodle
   owners"* is enough. (Running Kevin's plan? Say **RiseOrConquer**
   and it starts from `docs/starter-plan-riseorconquer.md`.)
4. The agent runs `./setup.sh`, checks your environment, confirms
   your starting state (shop health, product branch), and walks
   you into Stage 1.
5. From there it runs the pipeline stage by stage: it prepares
   everything preparable, and stops — clearly — at every human-only
   step (identity, banking, tax, tokens, and the publish approval).

## Path B — Plain CLI

```bash
git clone <this-repo-url> etsy-pod-pipeline
cd etsy-pod-pipeline
./setup.sh                      # environment check + next steps

# run the tests to see the machinery work
python3 -m pytest

# price a product: copy the example, replace the EXAMPLE costs with
# real numbers from your Printify catalog (Stage 5)
cp config/pricing.example.json config/my-product.json   # then edit it
python3 -m pipeline.pricing config/my-product.json

# build a listing pack from a design brief (Stage 6)
cp config/design-brief.example.json config/my-brief.json  # then edit it
python3 -m pipeline.listing config/my-brief.json

# or start from a shop-type preset (picker): emit its pricing and
# brief configs and run both tools on them
python3 -m pipeline.presets coloring-books --emit
python3 -m pipeline.pricing config/presets/out/coloring-books.pricing.json
python3 -m pipeline.listing config/presets/out/coloring-books.brief.json

# score product candidates from Stage 3 research
python3 -m pipeline.scoring candidates.json
```

Then use the modules directly from Python:

```python
from pipeline.pricing import compute_sale, price_for_profit
from pipeline.listing import build_pack

sale = compute_sale(price=39.95, shipping_charged=0.0,
                    product_cost=16.40, shipping_cost=5.60,
                    listing_fee=0.28)
print(sale.profit, sale.margin_pct)

pack = build_pack({"design_phrase": "Rise or Conquer",
                   "product": "Unisex T-Shirt",
                   "keywords": ["motivational shirt"]})
print(pack.title, pack.tags, pack.warnings)
```

## What is NOT installed

Nothing here creates an Etsy shop, logs into Etsy or Printify, holds
a token, or publishes a listing. Shop creation (appendix), identity
verification, and the Printify token are deliberate human steps,
and publishing sits behind a human approval gate (Stage 7). That
is a design choice, not a missing feature: the pipeline's job is
that everything reaching those steps is already researched,
designed, priced, and packed.
