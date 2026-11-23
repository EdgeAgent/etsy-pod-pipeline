"""Listing pack generator — title, tags, materials, description, FAQ.

Built to Etsy's actual limits and Etsy's current (2025–2026) Seller
Handbook guidance — see ``docs/06-listing-seo.md`` for the sourced
version of every rule below:

- **Title**: 140 characters max (Etsy Help). Etsy's 2026 title
  guidance: state the item clearly, most important traits upfront
  (front-loading helps *clicks* — Etsy says word order does not
  affect ranking), consider fewer than 15 words, don't repeat
  words, no subjective filler ("perfect", "beautiful"), no
  price/sale/shipping text, no gifting phrases ("gift for him").
- **Tags**: exactly 13 slots, **20 characters per tag** (Etsy Help —
  "How to Use Tags to Get Found in Search"). Multi-word phrases,
  all unique, long-tail over generic. An earlier version of this
  repo used a 55-character tag limit; that was wrong and is
  corrected in v0.3.0.
- **Description**: Etsy counts description keywords in query
  matching — relevant terms belong in the first sentences, written
  naturally, never a copy of the title.
- **Materials**: copied from the real product spec, never invented.
  (Etsy does not state that the free-text materials field affects
  search; honesty is the reason it exists.)

The generator also runs an IP-safety screen over the brief: known
trademark / franchise terms in the design text or keywords produce
warnings. The screen is a tripwire, not a legal opinion — Stage 3's
checklist (docs/03-research.md) is the real gate.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field

TITLE_LIMIT = 140
TITLE_WORD_TARGET = 15          # Etsy's 2026 guidance: consider <15 words
TITLE_FRONT_CHARS = 55          # what a shopper sees first in results
TAG_LIMIT = 13
TAG_CHAR_LIMIT = 20             # Etsy Help, verified 2026-11-23

# Words Etsy's 2026 title guidance says to keep out of titles:
# subjective filler and price/sale/shipping text. Gifting phrases
# are checked separately (they belong in tags, not the title).
TITLE_BANNED_WORDS = [
    "perfect", "beautiful", "wonderful", "amazing", "free shipping",
    "on sale", "sale!", "best seller", "bestseller", "cheap",
]
TITLE_GIFT_PHRASES = [
    "gift for him", "gift for her", "gift for men", "gift for women",
    "birthday present", "personalized gift", "personalised gift",
]

# Tripwire list — common trademark/franchise terms that must never ride
# into a design or a listing. Not exhaustive; absence of a flag is NOT
# clearance. See docs/03-research.md.
IP_BLOCKLIST = [
    "nike", "adidas", "disney", "marvel", "star wars", "pokemon",
    "harry potter", "nfl", "nba", "nhl", "mlb", "fifa", "barbie",
    "lego", "hello kitty", "supreme", "gucci", "louis vuitton",
    "chanel", "harley-davidson", "harley davidson", "ford", "chevy",
    "jeep", "tesla", "apple inc", "beatles", "metallica", "ac/dc",
    "grateful dead", "pink floyd", "naruto", "dragon ball", "zelda",
    "mario", "sonic the hedgehog", "batman", "superman", "spider-man",
    "spiderman", "avengers", "pixar", "netflix", "stranger things",
    "coco wyo", "bluey", "sanrio", "stanley cup",
]

AI_DISCLOSURE_LINE = (
    "Disclosure: this item was created with the use of AI tools, "
    "from my own original prompts and designs, as Etsy requires "
    "sellers to state."
)


@dataclass
class ListingPack:
    title: str
    tags: list = field(default_factory=list)
    materials: list = field(default_factory=list)
    description: str = ""
    faq: list = field(default_factory=list)  # list of (question, answer)
    warnings: list = field(default_factory=list)


def check_ip_safety(*texts: str) -> list[str]:
    """Flag blocklisted terms in any of the given texts."""
    haystack = " ".join(t.lower() for t in texts if t)
    return [f"IP tripwire: '{term}' appears in the brief — trademarked/franchise "
            f"terms never ship (docs/03-research.md)"
            for term in IP_BLOCKLIST if term in haystack]


def build_title(brief: dict) -> str:
    """Title formula (Etsy 2026 guidance): the item stated clearly
    first — design phrase + product — then the most important trait
    keywords. No gifting phrases, no repetition padding. Trimmed to
    Etsy's 140 characters at a word boundary, never mid-word."""
    phrase = brief["design_phrase"].strip()
    product = brief.get("product", "T-Shirt").strip()
    parts = [f"{phrase} {product}"]
    for extra in brief.get("title_keywords", []):
        parts.append(extra.strip())
    title = " | ".join(p for p in parts if p)
    if len(title) > TITLE_LIMIT:
        title = title[:TITLE_LIMIT].rsplit(" ", 1)[0].rstrip(" |,")
    return title


def build_tags(brief: dict) -> list[str]:
    """Fill all 13 tag slots with unique multi-word phrases of at
    most 20 characters (Etsy's real limit). Order: the brief's
    keyword seeds, then combinations built from the brief itself
    (phrase+product, phrase+gift, audience angles, product+gift) —
    never off-category filler borrowed from another shop type."""
    seeds = [s.strip().lower() for s in brief.get("keywords", []) if s.strip()]
    phrase = brief["design_phrase"].strip().lower()
    product = brief.get("product", "t-shirt").strip().lower()
    audience = brief.get("audience", "").strip().lower()
    candidates = list(seeds)
    candidates += [f"{phrase} {product}", f"{phrase} gift"]
    if audience:
        candidates += [f"gift for {audience}", f"{audience} gift"]
    candidates += [f"{product} gift"]
    for seed in seeds:  # last resort: seed + angle combos
        candidates += [f"{seed} gift", f"{seed} idea"]
    tags: list[str] = []
    seen: set[str] = set()
    for cand in candidates:
        if cand and cand not in seen and len(cand) <= TAG_CHAR_LIMIT:
            seen.add(cand)
            tags.append(cand)
        if len(tags) == TAG_LIMIT:
            break
    return tags


def _physical_description(brief: dict) -> str:
    phrase = brief["design_phrase"].strip()
    product = brief.get("product", "T-shirt")
    brand = brief.get("brand", "our shop")
    materials = ", ".join(brief.get("materials", [])) or "see product options"
    audience = brief.get("audience", "")
    hook = f"{phrase} — a {product.lower()} made for {audience}." if audience \
        else f"{phrase} — printed on a {product.lower()} you'll actually want to wear."
    lines = [
        hook,
        "",
        "Made to order, one at a time, when you buy it. No warehouse stock, "
        "no mass-produced pile — your item gets printed for you and shipped "
        "from our print partner's facility closest to you.",
        "",
        "DETAILS",
        f"- Product: {product}",
        f"- Materials: {materials}",
        "- Print: high-quality print, front",
        "- Fit: true to size — check the size chart in the photos before ordering",
        "",
        "SHIPPING",
        "Print-on-demand means production time before shipping (usually "
        "2-5 business days), then carrier transit. Order early for gifts "
        "and hard deadlines.",
        "",
        "RETURNS",
        "Because each item is made to order, we replace or refund any item "
        "that arrives damaged, misprinted, or wrong — message us with a "
        "photo and we make it right.",
        "",
        f"Designed by {brand}. Original artwork — designed in-house, "
        "printed on demand.",
    ]
    return "\n".join(lines)


def _digital_description(brief: dict) -> str:
    phrase = brief["design_phrase"].strip()
    product = brief.get("product", "Digital Download")
    brand = brief.get("brand", "our shop")
    materials = ", ".join(brief.get("materials", [])) or "digital files"
    audience = brief.get("audience", "")
    hook = f"{phrase} — a {product.lower()} made for {audience}." if audience \
        else f"{phrase} — a {product.lower()}, ready to download."
    lines = [
        hook,
        "",
        "INSTANT DOWNLOAD — this is a digital product. No physical item "
        "will be shipped. Your files are available the moment checkout "
        "completes, from your Etsy purchases page.",
        "",
        "WHAT YOU GET",
        f"- Product: {product}",
        f"- Files: {materials}",
        "- Sized and formatted as described in the listing photos — check "
        "them before ordering, digital items can't be un-downloaded.",
        "",
        "LICENCE",
        "Personal use unless this listing explicitly grants commercial "
        "use. The files themselves may not be resold, shared, or given "
        "away — that's the licence every original-design shop runs on.",
        "",
        "PROBLEMS?",
        "A file that won't open or downloads corrupted is a defect: "
        "message us and we replace it or refund you. Change-of-mind "
        "returns on downloaded files aren't accepted.",
        "",
        f"Designed by {brand}. Original work — designed in-house.",
    ]
    return "\n".join(lines)


def build_description(brief: dict) -> str:
    if brief.get("delivery_type") == "digital":
        text = _digital_description(brief)
    else:
        text = _physical_description(brief)
    if brief.get("ai_assisted"):
        text += "\n\n" + AI_DISCLOSURE_LINE
    return text


def build_faq(brief: dict) -> list[tuple[str, str]]:
    if brief.get("delivery_type") == "digital":
        return [
            ("Is anything shipped to me?",
             "No — nothing is shipped; this is an instant download. Files "
             "appear in your Etsy purchases as soon as checkout completes."),
            ("What software do I need?",
             "The listing states the file formats and what opens them. "
             "Check the listing photos before ordering if you're unsure."),
            ("Can I return a download?",
             "Downloaded files can't be returned, but a file that won't "
             "open or arrives corrupted is always replaced or refunded."),
        ]
    return [
        ("How does sizing run?",
         "True to size. Compare the size chart in the listing photos with a "
         "shirt you own before ordering."),
        ("When will my order ship?",
         "Each item is printed to order (usually 2-5 business days of "
         "production), then shipped with tracking."),
        ("Can I return it if I change my mind?",
         "Made-to-order items can't be restocked, so change-of-mind returns "
         "aren't accepted — but damaged, misprinted, or wrong items are "
         "always replaced or refunded."),
    ]


def seo_audit(brief: dict, pack: "ListingPack") -> list[str]:
    """Check a built pack against Etsy's current SEO guidance
    (docs/06-listing-seo.md, sourced from the Seller Handbook).
    Returns warnings; silence means the pack passes every check the
    generator can run. The checks a script *can't* run — attributes
    filled, first photo quality, keyword research done — live in
    Stage 6's checklist."""
    warnings: list[str] = []
    title = pack.title
    phrase = brief.get("design_phrase", "").strip().lower()

    words = re.findall(r"[a-z0-9']+", title.lower())
    if len(words) > TITLE_WORD_TARGET:
        warnings.append(
            f"SEO: title is {len(words)} words — Etsy's 2026 guidance "
            f"says consider fewer than {TITLE_WORD_TARGET}; every word "
            "must earn its place")
    counts: dict[str, int] = {}
    for w in words:
        if len(w) >= 4:
            counts[w] = counts.get(w, 0) + 1
    repeated = [w for w, n in counts.items() if n >= 3]
    if repeated:
        warnings.append(
            "SEO: title repeats word(s) "
            + ", ".join(f"'{w}'" for w in repeated)
            + " 3+ times — Etsy advises against repeated words in titles")
    low = title.lower()
    for banned in TITLE_BANNED_WORDS:
        if banned in low:
            warnings.append(
                f"SEO: title contains '{banned}' — Etsy's guidance keeps "
                "subjective filler and price/sale/shipping text out of titles")
    for gift in TITLE_GIFT_PHRASES:
        if gift in low:
            warnings.append(
                f"SEO: title contains the gifting phrase '{gift}' — Etsy "
                "says gifting phrases belong in tags, not the title")
    if phrase and phrase not in title[:TITLE_FRONT_CHARS].lower():
        warnings.append(
            "SEO: the primary keyword phrase is not in the first "
            f"{TITLE_FRONT_CHARS} characters of the title — that is what "
            "shoppers see in results (a click problem, per Etsy, not a "
            "ranking one)")

    seeds = [s.strip().lower() for s in brief.get("keywords", []) if s.strip()]
    dropped = [s for s in seeds if len(s) > TAG_CHAR_LIMIT]
    if dropped:
        warnings.append(
            f"SEO: {len(dropped)} keyword seed(s) exceed Etsy's "
            f"{TAG_CHAR_LIMIT}-character tag limit and cannot be tags: "
            + ", ".join(f"'{d}'" for d in dropped)
            + " — split them into shorter phrases")
    single = [t for t in pack.tags if " " not in t]
    if single:
        warnings.append(
            "SEO: single-word tag(s) present ("
            + ", ".join(f"'{t}'" for t in single)
            + ") — Etsy: multi-word phrases are stronger tags")
    if len(pack.tags) < TAG_LIMIT:
        warnings.append(f"Only {len(pack.tags)} of {TAG_LIMIT} tag slots "
                        "filled — add more keyword seeds to the brief")

    first_lines = "\n".join(pack.description.split("\n")[:3]).lower()
    if phrase and phrase not in first_lines:
        warnings.append(
            "SEO: the primary keyword phrase is not in the description's "
            "opening lines — Etsy counts description keywords in query "
            "matching; work it into the first sentences naturally")
    if brief.get("delivery_type") == "digital" and \
            "instant download" not in pack.description.lower():
        warnings.append(
            "SEO/digital: description does not state INSTANT DOWNLOAD — "
            "digital listings must say no physical item ships")
    if brief.get("ai_assisted") and "use of ai" not in pack.description.lower():
        warnings.append(
            "Etsy requires AI use to be disclosed in the listing "
            "description — the disclosure line is missing")
    if not pack.materials:
        warnings.append(
            "Materials list is empty — copy the real spec; invented "
            "materials are a returns problem, and honest attributes/"
            "materials are part of a complete listing")
    return warnings


def build_pack(brief: dict) -> ListingPack:
    """Build the full listing pack from a design brief dict.

    Required brief keys: ``design_phrase``. Optional: ``product``,
    ``audience``, ``keywords``, ``title_keywords``, ``materials``,
    ``brand``, ``delivery_type`` ("digital" for downloads),
    ``ai_assisted`` (adds Etsy's required AI disclosure line).
    A pack built on defaults is a draft, not a listing.
    """
    if not brief.get("design_phrase", "").strip():
        raise ValueError("brief needs a non-empty 'design_phrase'")
    pack = ListingPack(
        title=build_title(brief),
        tags=build_tags(brief),
        materials=list(brief.get("materials", [])),
        description=build_description(brief),
        faq=build_faq(brief),
    )
    pack.warnings = check_ip_safety(
        brief.get("design_phrase", ""), brief.get("product", ""),
        " ".join(brief.get("keywords", [])), " ".join(brief.get("title_keywords", [])),
    ) + seo_audit(brief, pack)
    return pack


def format_pack(pack: ListingPack) -> str:
    out = [f"TITLE ({len(pack.title)}/{TITLE_LIMIT}):", pack.title, "",
           f"TAGS ({len(pack.tags)}/{TAG_LIMIT}, ≤{TAG_CHAR_LIMIT} chars each):"]
    out += [f"  - {t} ({len(t)}/{TAG_CHAR_LIMIT})" for t in pack.tags]
    out += ["", "MATERIALS:", "  " + (", ".join(pack.materials) or "(none in brief)"),
            "", "DESCRIPTION:", pack.description, "", "FAQ:"]
    out += [f"  Q: {q}\n  A: {a}" for q, a in pack.faq]
    if pack.warnings:
        out += ["", "WARNINGS:"]
        out += [f"  ! {w}" for w in pack.warnings]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python3 -m pipeline.listing <design-brief.json>", file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        brief = json.load(fh)
    print(format_pack(build_pack(brief)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
