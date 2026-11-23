import json

import pytest

from pipeline.listing import build_pack
from pipeline.presets import (emit_configs, get_preset, list_presets,
                              validate_preset)
from pipeline.pricing import compute_sale

EXPECTED_IDS = {"pod-apparel", "digital-downloads", "stl-files",
                "pet-accessories", "digital-templates", "coloring-books"}


def test_all_six_shop_types_ship_as_presets():
    ids = {p["id"] for p in list_presets()}
    assert EXPECTED_IDS <= ids


def test_every_preset_carries_the_mixed_model():
    for preset in list_presets():
        assert preset["affiliate_picks"], preset["id"]
        for pick in preset["affiliate_picks"]:
            assert pick["category"] and pick["channel"]
            low, high = pick["price_band"]
            assert 0 < low <= high
        # Affiliate promotion is an off-Etsy lane, always.
        assert "affiliate-model" in json.dumps(preset) or \
            "off Etsy" in json.dumps(preset), preset["id"]


def test_every_preset_has_a_creation_path():
    for preset in list_presets():
        path = preset["creation_path"]
        assert len(path) >= 4, preset["id"]
        joined = " ".join(path).lower()
        assert "stage 3" in joined and "stage 7" in joined, preset["id"]


def test_templates_and_downloads_are_distinct_presets():
    templates = get_preset("digital-templates")
    downloads = get_preset("digital-downloads")
    assert templates["summary"] != downloads["summary"]
    assert "document" in templates["summary"].lower()
    assert "svg" in downloads["summary"].lower()


def test_every_preset_drives_the_pricing_tool():
    for preset in list_presets():
        cfg = preset["pricing"]
        sale = compute_sale(price=cfg["price"],
                            shipping_charged=cfg.get("shipping_charged", 0.0),
                            product_cost=cfg["product_cost"],
                            shipping_cost=cfg["shipping_cost"])
        assert sale.profit > 0, preset["id"]


def test_every_preset_drives_the_listing_tool():
    for preset in list_presets():
        pack = build_pack(preset["brief"])
        assert pack.title
        assert not any("IP tripwire" in w for w in pack.warnings), preset["id"]


def test_digital_presets_have_zero_production_costs():
    for preset in list_presets():
        if preset["shop_type"] == "digital-download":
            assert preset["pricing"]["product_cost"] == 0.0
            assert preset["pricing"]["shipping_cost"] == 0.0


def test_get_unknown_preset_names_the_options():
    with pytest.raises(ValueError, match="pod-apparel"):
        get_preset("no-such-shop")


def test_validate_rejects_missing_and_broken_presets():
    with pytest.raises(ValueError):
        validate_preset({"id": "x"})
    good = get_preset("pod-apparel")
    broken = json.loads(json.dumps(good))
    broken["products"][0]["price_band"] = [50.0, 10.0]
    with pytest.raises(ValueError):
        validate_preset(broken)


def test_emit_configs_round_trips(tmp_path):
    preset = get_preset("digital-downloads")
    pricing_path, brief_path = emit_configs(preset, tmp_path)
    assert json.loads(pricing_path.read_text())["price"] == preset["pricing"]["price"]
    assert json.loads(brief_path.read_text())["design_phrase"] == \
        preset["brief"]["design_phrase"]
