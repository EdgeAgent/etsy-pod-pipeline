"""Pricing calculator tests — the fee math must match Etsy's policy
(docs/fees-verified-2026-11-23.md) exactly, because pricing on wrong
fees is how POD shops quietly lose money on every sale."""

import pytest

from pipeline.pricing import (OFFSITE_ADS_CAP, compute_sale,
                              price_for_profit)


def test_transaction_fee_is_6_5_pct_of_price_plus_shipping():
    b = compute_sale(price=40.00, shipping_charged=5.00, product_cost=10.00,
                     shipping_cost=4.00, listing_fee=0.0, regulatory_pct=0.0)
    # processing uses defaults too; isolate the transaction fee field
    assert b.transaction_fee == pytest.approx(0.065 * 45.00, abs=0.01)


def test_regulatory_fee_canada_half_percent():
    b = compute_sale(price=40.00, shipping_charged=0.00, product_cost=10.00,
                     shipping_cost=4.00, listing_fee=0.0)
    assert b.regulatory_fee == pytest.approx(0.005 * 40.00, abs=0.01)


def test_processing_domestic_3pct_plus_quarter():
    b = compute_sale(price=50.00, shipping_charged=0.00, product_cost=10.00,
                     shipping_cost=4.00, listing_fee=0.0)
    assert b.processing_fee == pytest.approx(0.03 * 50.00 + 0.25, abs=0.01)


def test_processing_international_4pct():
    b = compute_sale(price=50.00, shipping_charged=0.00, product_cost=10.00,
                     shipping_cost=4.00, listing_fee=0.0, international=True)
    assert b.processing_fee == pytest.approx(0.04 * 50.00 + 0.25, abs=0.01)


def test_profit_is_revenue_minus_all_costs_and_fees():
    b = compute_sale(price=39.95, shipping_charged=0.00, product_cost=16.40,
                     shipping_cost=5.60, listing_fee=0.28)
    assert b.revenue == pytest.approx(39.95)
    assert b.total_costs == pytest.approx(16.40 + 5.60 + b.total_fees)
    assert b.profit == pytest.approx(b.revenue - b.total_costs)
    assert b.profit > 0  # the worked example must actually make money


def test_free_shipping_bakes_cost_into_margin():
    paid = compute_sale(price=34.95, shipping_charged=5.00, product_cost=16.40,
                        shipping_cost=5.60, listing_fee=0.28)
    free = compute_sale(price=39.95, shipping_charged=0.00, product_cost=16.40,
                        shipping_cost=5.60, listing_fee=0.28)
    # Same buyer total, same provider costs — fee base identical, so
    # profit must be (nearly) identical. "Free shipping" is pricing, not magic.
    assert free.profit == pytest.approx(paid.profit, abs=0.02)


def test_offsite_ads_fee_only_when_attributed():
    plain = compute_sale(price=40.00, shipping_charged=0.00, product_cost=10.00,
                         shipping_cost=4.00, listing_fee=0.0)
    attributed = compute_sale(price=40.00, shipping_charged=0.00, product_cost=10.00,
                              shipping_cost=4.00, listing_fee=0.0, offsite_ads=True)
    assert plain.offsite_ads_fee == 0.0
    assert attributed.offsite_ads_fee == pytest.approx(0.15 * 40.00, abs=0.01)
    assert attributed.profit < plain.profit


def test_offsite_ads_high_volume_rate_and_cap():
    b = compute_sale(price=40.00, shipping_charged=0.00, product_cost=10.00,
                     shipping_cost=4.00, listing_fee=0.0, offsite_ads=True,
                     high_volume_shop=True)
    assert b.offsite_ads_fee == pytest.approx(0.12 * 40.00, abs=0.01)
    huge = compute_sale(price=5000.00, shipping_charged=0.00, product_cost=10.00,
                        shipping_cost=4.00, listing_fee=0.0, offsite_ads=True)
    assert huge.offsite_ads_fee == OFFSITE_ADS_CAP


def test_price_for_profit_round_trips():
    price = price_for_profit(product_cost=16.40, shipping_cost=5.60,
                             shipping_charged=0.00, target_profit=8.00,
                             listing_fee=0.28)
    b = compute_sale(price=price, shipping_charged=0.00, product_cost=16.40,
                     shipping_cost=5.60, listing_fee=0.28)
    assert b.profit == pytest.approx(8.00, abs=0.05)


def test_negative_costs_rejected():
    with pytest.raises(ValueError):
        compute_sale(price=40.00, shipping_charged=0.00, product_cost=-1.00,
                     shipping_cost=4.00)


def test_zero_price_rejected():
    with pytest.raises(ValueError):
        compute_sale(price=0.00, shipping_charged=0.00, product_cost=10.00,
                     shipping_cost=4.00)
