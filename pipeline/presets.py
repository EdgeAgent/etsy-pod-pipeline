"""Shop-type presets — the picker.

Open the repo, see the shop types, pick one, and the pipeline is
pre-configured for that shop: niche brief, starter product list,
price bands, a pricing config the calculator can run, a listing
brief the pack generator can run, and a launch checklist. Since
v0.3.0 each preset also carries the mixed model — affiliate picks
(proven third-party products promoted off Etsy,
``docs/affiliate-model.md``) alongside the shop's own products —
and a creation path for users who arrive with no product at all.

Presets live in ``config/presets/<id>.json``. A preset is a
*starting configuration*, not a promise: its price bands come from
``docs/research-findings-2026-11-23.md`` (dated, sourced, some
labelled estimates) and its example costs are placeholders until
real catalog numbers replace them — the same honesty rules as the
rest of the repo.

Usage:

    python3 -m pipeline.presets                 # list the shop types
    python3 -m pipeline.presets pod-apparel     # show one preset
    python3 -m pipeline.presets pod-apparel --emit
        # write config/presets/out/pod-apparel.pricing.json and
        # config/presets/out/pod-apparel.brief.json, ready for
        # pipeline.pricing / pipeline.listing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PRESET_DIR = Path(__file__).resolve().parent.parent / "config" / "presets"
REQUIRED_KEYS = ("id", "name", "shop_type", "summary", "delivery",
                 "products", "brief", "pricing", "launch_checklist")
# v0.3.0: every preset also carries the mixed model (affiliate picks
# alongside own products) and the no-product creation path. Optional
# in the loader for back-compat, required by the test suite for the
# presets that ship in this repo.
MIXED_KEYS = ("affiliate_picks", "creation_path")


def list_presets(preset_dir: Path = PRESET_DIR) -> list[dict]:
    """Load every preset in the directory, sorted by id."""
    presets = [load_preset(p) for p in sorted(preset_dir.glob("*.json"))]
    return sorted(presets, key=lambda p: p["id"])


def load_preset(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        preset = json.load(fh)
    validate_preset(preset, source=str(path))
    return preset


def get_preset(preset_id: str, preset_dir: Path = PRESET_DIR) -> dict:
    path = preset_dir / f"{preset_id}.json"
    if not path.exists():
        known = ", ".join(p["id"] for p in list_presets(preset_dir)) or "(none)"
        raise ValueError(f"unknown preset '{preset_id}' — available: {known}")
    return load_preset(path)


def validate_preset(preset: dict, source: str = "preset") -> None:
    """A preset that cannot drive the tools is not a preset."""
    missing = [k for k in REQUIRED_KEYS if k not in preset]
    if missing:
        raise ValueError(f"{source}: missing keys: {', '.join(missing)}")
    if not preset["products"]:
        raise ValueError(f"{source}: 'products' must not be empty")
    for product in preset["products"]:
        for key in ("name", "price_band"):
            if key not in product:
                raise ValueError(f"{source}: product missing '{key}': {product!r}")
        low, high = product["price_band"]
        if low <= 0 or high < low:
            raise ValueError(f"{source}: bad price_band {product['price_band']} "
                             f"for {product['name']!r}")
    if not preset["brief"].get("design_phrase", "").strip():
        raise ValueError(f"{source}: brief needs a non-empty 'design_phrase' "
                         "(pipeline.listing requires it)")
    for key in ("price", "product_cost", "shipping_cost"):
        if key not in preset["pricing"]:
            raise ValueError(f"{source}: pricing config missing '{key}' "
                             "(pipeline.pricing requires it)")
    if not preset["launch_checklist"]:
        raise ValueError(f"{source}: 'launch_checklist' must not be empty")
    for key in MIXED_KEYS:
        if key in preset and not preset[key]:
            raise ValueError(f"{source}: '{key}' must not be empty when present")
    for pick in preset.get("affiliate_picks", []):
        for key in ("category", "price_band", "channel"):
            if key not in pick:
                raise ValueError(f"{source}: affiliate pick missing '{key}': {pick!r}")
        low, high = pick["price_band"]
        if low <= 0 or high < low:
            raise ValueError(f"{source}: bad affiliate price_band "
                             f"{pick['price_band']} for {pick['category']!r}")
        if "amazon" not in pick["channel"].lower() and \
                "etsy" not in pick["channel"].lower():
            raise ValueError(f"{source}: affiliate pick channel must name "
                             f"the program: {pick!r}")
    for step in preset.get("creation_path", []):
        if not isinstance(step, str) or not step.strip():
            raise ValueError(f"{source}: creation_path steps must be text")


def emit_configs(preset: dict, out_dir: Path) -> tuple[Path, Path]:
    """Write the preset's pricing config and listing brief where the
    existing tools can consume them."""
    out_dir.mkdir(parents=True, exist_ok=True)
    pricing_path = out_dir / f"{preset['id']}.pricing.json"
    brief_path = out_dir / f"{preset['id']}.brief.json"
    pricing_path.write_text(json.dumps(preset["pricing"], indent=2) + "\n",
                            encoding="utf-8")
    brief_path.write_text(json.dumps(preset["brief"], indent=2) + "\n",
                          encoding="utf-8")
    return pricing_path, brief_path


def format_preset(preset: dict) -> str:
    lines = [f"{preset['name']}  [{preset['id']}]",
             f"Type: {preset['shop_type']} · Delivery: {preset['delivery']}",
             "", preset["summary"], "", "Starter products (price bands from "
             "docs/research-findings-2026-11-23.md):"]
    for p in preset["products"]:
        low, high = p["price_band"]
        note = f" — {p['notes']}" if p.get("notes") else ""
        lines.append(f"  - {p['name']}: ${low:.2f}–${high:.2f}{note}")
    if preset.get("affiliate_picks"):
        lines += ["", "Affiliate picks (proven sellers, promoted OFF Etsy — "
                  "docs/affiliate-model.md):"]
        for pick in preset["affiliate_picks"]:
            low, high = pick["price_band"]
            lines.append(f"  - {pick['category']}: ${low:.2f}–${high:.2f} "
                         f"via {pick['channel']}")
    if preset.get("creation_path"):
        lines += ["", "No product yet? The creation path:"]
        lines += [f"  {i}. {step}" for i, step in
                  enumerate(preset["creation_path"], 1)]
    lines += ["", "Launch checklist:"]
    lines += [f"  [ ] {item}" for item in preset["launch_checklist"]]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print("Pick a shop type — each preset pre-configures the pipeline:\n")
        for p in list_presets():
            print(f"  {p['id']:<18} {p['name']} ({p['shop_type']})")
        print("\nShow one:  python3 -m pipeline.presets <id>")
        print("Emit its pricing + brief configs:  "
              "python3 -m pipeline.presets <id> --emit")
        return 0
    preset = get_preset(args[0])
    print(format_preset(preset))
    if "--emit" in argv:
        pricing_path, brief_path = emit_configs(
            preset, PRESET_DIR / "out")
        print(f"\nWrote {pricing_path}\nWrote {brief_path}")
        print("Run them:\n"
              f"  python3 -m pipeline.pricing {pricing_path}\n"
              f"  python3 -m pipeline.listing {brief_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
