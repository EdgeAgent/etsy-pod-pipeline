# Stage 2 — Connect Printify

**Goal:** Printify connected to the Etsy shop as its sales channel, so
products built in Printify can be published to Etsy and orders flow
back to Printify for fulfilment automatically.

## How the pieces fit

```
You ──design──▶ Printify product ──publish──▶ Etsy listing
                                                  │ buyer orders
Printify ◀──order auto-created── Etsy Payments ◀──┘
   │
   └──prints + ships──▶ buyer        You watch: messages, reviews,
                                       payouts (Stage 8)
```

You never print, pack, or ship anything. Printify charges your payment
method on file with Printify when an order is produced; Etsy deposits
the buyer's money to your bank on its deposit schedule. The spread
between the two is your margin — Stage 5's calculator exists because
that spread is thinner than it looks.

## Connect steps

### 1. Printify account (human creates it)

- [ ] Create a Printify account (free plan is enough to start).
- [ ] Add a payment method inside Printify (human — Printify charges
      production costs per order).

### 2. API token — for agent-assisted work (optional but recommended)

If you want your agent to browse the catalog, build products, or check
orders through Printify's API:

1. In Printify: **My Profile → Integrations → Generate Personal
   Access Token** (Printify's API settings).
2. The token is a credential. **The human enters it in the connector's
   connect flow** (e.g. Muse's Printify connector page) — never in
   chat, never in an email, never in this repo, never in a file the
   repo tracks.
3. Scopes: grant only what the work needs (catalog read, products,
   orders). Start read-heavy; widen when a stage actually needs it.

> This repo contains **no token, no placeholder token, and no config
> file expecting one**. If you ever see a token in a commit here,
> revoke it in Printify immediately and treat it as burned.

### 3. Link the Etsy shop as a sales channel

1. In Printify: **Add a new store → Etsy** → sign in to Etsy and
   authorize the connection (human — it's their account consent).
2. Confirm the shop shows as **Connected** in Printify.
3. In Etsy Shop Manager, confirm Printify appears under integrations.

### 4. Choose your print provider(s)

Provider choice decides your real product cost, shipping cost, and
delivery times. Rules of thumb for a Canadian shop selling to
Canada + US:

- [ ] **Prefer providers located in Canada or the US** — shorter
      shipping, no cross-border surprises for most buyers, returns
      stay sane.
- [ ] Compare the SAME blueprint across 2–3 providers: base cost,
      shipping to CA and to US, production time (business days),
      print quality reputation.
- [ ] Pick one **primary** provider per product. Switching providers
      later changes costs and mockups — re-run Stage 5 pricing when
      you switch.
- [ ] Note the provider's **print-area dimensions and file specs** —
      Stage 4 designs to them.

## Verify the connection before building anything

- [ ] A draft product in Printify can see the Etsy shop as its
      publish target (do NOT publish it — Stage 7 gate).
- [ ] Printify's order settings: orders set to be sent to production
      automatically once the shop is live (leave this OFF until the
      publish gate opens for your first real product).
- [ ] Timezone/currency inside Printify match how you price (Stage 5).

## Stage checklist

- [ ] Printify account created; payment method added (human)
- [ ] API token generated and entered via the connect flow only (human)
- [ ] Etsy shop linked in Printify and showing Connected
- [ ] Primary provider chosen per starter product (Canada/US preferred)
- [ ] Provider print specs recorded for Stage 4
- [ ] Auto-production still OFF until first publish approval

## Shop-type note

This stage exists for the **physical presets**: `pod-apparel`
(Printify is the provider) and `pet-accessories` (Printify carries
pet products; a specialist partner is fine too — whoever makes it,
the partner is disclosed in Shop Manager and on the listing, as
Etsy requires). The digital presets — `digital-downloads`,
`digital-templates`, `stl-files`, `coloring-books` — have no print
provider: skip this stage, note the skip, and go to Stage 3
(`docs/shop-types.md` has the per-type map).
