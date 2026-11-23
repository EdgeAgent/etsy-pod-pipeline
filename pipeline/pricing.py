"""Pricing calculator — the full Etsy fee stack on one print-on-demand sale.

Every rate below was verified against Etsy's official pages on
2026-11-23 (see ``docs/fees-verified-2026-11-23.md`` for sources).
Etsy changes its fees; re-verify before you price a real shop.

Fee stack modelled (Canadian shop, the defaults):

- **Listing fee**: US$0.20 per listing, charged on publish and on every
  4-month renewal, whether or not the item sells. Modelled here as a
  per-sale cost (the listing one unit consumed); pass the amount in
  your shop currency.
- **Transaction fee**: 6.5% of (item price + shipping charged + gift
  wrap). For non-US sellers it also applies to any seller-responsible
  tax built into the price.
- **Regulatory operating fee**: 0.50% for Canada, same base as the
  transaction fee. Zero in the US and most other countries.
- **Payment processing**: Canada 3% + C$0.25 per order for buyers in
  Canada or the US; 4% + C$0.25 for other international buyers.
  Charged on the total the buyer pays (price + shipping + tax).
- **Offsite Ads fee** (optional, only on ad-attributed orders): 15%
  while the shop is under US$10,000 in trailing-365-day sales (those
  shops may opt out), 12% at/above that threshold, capped at US$100
  per order.

All money values are in ONE currency — the currency you pass in. Do
not mix CAD costs with USD prices and expect sense out.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass

# Verified 2026-11-23 — docs/fees-verified-2026-11-23.md
LISTING_FEE_USD = 0.20
TRANSACTION_FEE_PCT = 6.5
REGULATORY_FEE_PCT_CANADA = 0.50
PROCESSING_PCT_DOMESTIC = 3.0        # Canada: buyers in Canada or the US
PROCESSING_PCT_INTERNATIONAL = 4.0   # Canada: all other buyers
PROCESSING_FIXED = 0.25              # per order, shop currency
OFFSITE_ADS_PCT_STANDARD = 15.0
OFFSITE_ADS_PCT_HIGH_VOLUME = 12.0
OFFSITE_ADS_CAP = 100.0              # US$ per attributed order


@dataclass
class SaleBreakdown:
    price: float
    shipping_charged: float
    product_cost: float
    shipping_cost: float
    listing_fee: float
    transaction_fee: float
    regulatory_fee: float
    processing_fee: float
    offsite_ads_fee: float
    total_fees: float
    total_costs: float
    revenue: float
    profit: float
    margin_pct: float  # profit as % of revenue


def _pct(amount: float, pct: float) -> float:
    return round(amount * pct / 100.0, 2)


def compute_sale(price: float, shipping_charged: float, product_cost: float,
                 shipping_cost: float, *, listing_fee: float = LISTING_FEE_USD,
                 transaction_pct: float = TRANSACTION_FEE_PCT,
                 regulatory_pct: float = REGULATORY_FEE_PCT_CANADA,
                 international: bool = False,
                 offsite_ads: bool = False,
                 high_volume_shop: bool = False) -> SaleBreakdown:
    """Work one sale end to end: what the buyer pays, what Etsy takes,
    what Printify takes, and what is left.

    ``product_cost`` and ``shipping_cost`` are what the print provider
    charges YOU (the blank + print, and the fulfilment postage).
    ``shipping_charged`` is what the buyer pays you for shipping
    (0.00 if you offer "free" shipping and bake it into the price).
    """
    if price <= 0:
        raise ValueError("price must be positive")
    if min(shipping_charged, product_cost, shipping_cost, listing_fee) < 0:
        raise ValueError("costs and fees cannot be negative")

    fee_base = price + shipping_charged  # transaction + regulatory base
    transaction_fee = _pct(fee_base, transaction_pct)
    regulatory_fee = _pct(fee_base, regulatory_pct)
    processing_pct = PROCESSING_PCT_INTERNATIONAL if international else PROCESSING_PCT_DOMESTIC
    processing_fee = _pct(fee_base, processing_pct) + PROCESSING_FIXED
    offsite_fee = 0.0
    if offsite_ads:
        ads_pct = OFFSITE_ADS_PCT_HIGH_VOLUME if high_volume_shop else OFFSITE_ADS_PCT_STANDARD
        offsite_fee = min(_pct(fee_base, ads_pct), OFFSITE_ADS_CAP)

    total_fees = round(listing_fee + transaction_fee + regulatory_fee
                       + processing_fee + offsite_fee, 2)
    total_costs = round(product_cost + shipping_cost + total_fees, 2)
    revenue = round(price + shipping_charged, 2)
    profit = round(revenue - total_costs, 2)
    margin_pct = round(profit / revenue * 100.0, 1) if revenue else 0.0
    return SaleBreakdown(
        price=price, shipping_charged=shipping_charged,
        product_cost=product_cost, shipping_cost=shipping_cost,
        listing_fee=listing_fee, transaction_fee=transaction_fee,
        regulatory_fee=regulatory_fee, processing_fee=processing_fee,
        offsite_ads_fee=offsite_fee, total_fees=total_fees,
        total_costs=total_costs, revenue=revenue, profit=profit,
        margin_pct=margin_pct,
    )


def price_for_profit(product_cost: float, shipping_cost: float,
                     shipping_charged: float, target_profit: float, *,
                     listing_fee: float = LISTING_FEE_USD,
                     transaction_pct: float = TRANSACTION_FEE_PCT,
                     regulatory_pct: float = REGULATORY_FEE_PCT_CANADA,
                     international: bool = False,
                     offsite_ads: bool = False,
                     high_volume_shop: bool = False) -> float:
    """Solve for the list price that leaves ``target_profit`` on a sale.

    Percentage fees are charged on (price + shipping_charged), so:
        profit = (price + ship) * (1 - pct) - fixed_fees - costs
    Inverted directly. The Offsite Ads cap is ignored here (it only
    binds on very large orders); check big prices with compute_sale.
    """
    processing_pct = PROCESSING_PCT_INTERNATIONAL if international else PROCESSING_PCT_DOMESTIC
    pct_total = transaction_pct + regulatory_pct + processing_pct
    if offsite_ads:
        pct_total += OFFSITE_ADS_PCT_HIGH_VOLUME if high_volume_shop else OFFSITE_ADS_PCT_STANDARD
    keep = 1.0 - pct_total / 100.0
    if keep <= 0:
        raise ValueError("fee percentages total 100% or more — no price works")
    fixed = listing_fee + PROCESSING_FIXED + product_cost + shipping_cost
    price = (target_profit + fixed) / keep - shipping_charged
    return round(price, 2)


def format_breakdown(b: SaleBreakdown) -> str:
    lines = [
        f"Buyer pays:            {b.revenue:>8.2f}  (item {b.price:.2f} + shipping {b.shipping_charged:.2f})",
        f"Printify product cost: {-b.product_cost:>8.2f}",
        f"Printify shipping:     {-b.shipping_cost:>8.2f}",
        f"Etsy listing fee:      {-b.listing_fee:>8.2f}",
        f"Etsy transaction 6.5%: {-b.transaction_fee:>8.2f}",
        f"Etsy regulatory fee:   {-b.regulatory_fee:>8.2f}",
        f"Etsy processing fee:   {-b.processing_fee:>8.2f}",
    ]
    if b.offsite_ads_fee:
        lines.append(f"Etsy Offsite Ads fee:  {-b.offsite_ads_fee:>8.2f}")
    lines += [
        f"Total fees:            {b.total_fees:>8.2f}",
        f"PROFIT:                {b.profit:>8.2f}   ({b.margin_pct:.1f}% of revenue)",
    ]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python3 -m pipeline.pricing <pricing.json>", file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        cfg = json.load(fh)
    breakdown = compute_sale(
        price=cfg["price"], shipping_charged=cfg.get("shipping_charged", 0.0),
        product_cost=cfg["product_cost"], shipping_cost=cfg["shipping_cost"],
        listing_fee=cfg.get("listing_fee", LISTING_FEE_USD),
        international=cfg.get("international", False),
        offsite_ads=cfg.get("offsite_ads", False),
        high_volume_shop=cfg.get("high_volume_shop", False),
    )
    print(format_breakdown(breakdown))
    if "target_profit" in cfg:
        solved = price_for_profit(
            product_cost=cfg["product_cost"], shipping_cost=cfg["shipping_cost"],
            shipping_charged=cfg.get("shipping_charged", 0.0),
            target_profit=cfg["target_profit"],
            listing_fee=cfg.get("listing_fee", LISTING_FEE_USD),
            international=cfg.get("international", False),
            offsite_ads=cfg.get("offsite_ads", False),
            high_volume_shop=cfg.get("high_volume_shop", False),
        )
        print(f"\nList price for {cfg['target_profit']:.2f} profit per sale: {solved:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
