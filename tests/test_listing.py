"""Listing pack tests — a pack that violates Etsy's limits is a pack
Etsy rejects, so the limits are asserted, not assumed."""

import pytest

from pipeline.listing import (TAG_CHAR_LIMIT, TAG_LIMIT, TITLE_LIMIT,
                              build_pack, build_tags, build_title,
                              check_ip_safety)

BRIEF = {
    "design_phrase": "Rise or Conquer",
    "product": "Unisex T-Shirt",
    "audience": "gym lovers",
    "brand": "RiseOrConquer",
    "keywords": [
        "motivational shirt", "gym motivation tee", "rise or conquer",
        "workout shirt", "fitness gift", "gym lover gift",
        "inspirational tee", "no excuses shirt", "training shirt",
        "mindset shirt",
    ],
    "title_keywords": ["Motivational Gym Shirt", "Workout Gift"],
    "materials": ["100% Airlume combed and ring-spun cotton"],
}


def test_title_within_etsy_limit():
    title = build_title(BRIEF)
    assert 0 < len(title) <= TITLE_LIMIT
    assert title.startswith("Rise or Conquer")


def test_title_truncates_at_word_boundary():
    brief = dict(BRIEF, title_keywords=["word " * 40])
    title = build_title(brief)
    assert len(title) <= TITLE_LIMIT
    assert not title.endswith(" ")


def test_all_13_tag_slots_filled_from_a_full_brief():
    tags = build_tags(BRIEF)
    assert len(tags) == TAG_LIMIT


def test_tag_limit_is_etsys_real_20_chars():
    # Etsy Help: each tag can contain up to 20 characters.
    # (v0.1-0.2 of this repo wrongly used 55; corrected in v0.3.0.)
    assert TAG_CHAR_LIMIT == 20


def test_every_tag_within_limit():
    tags = build_tags(BRIEF)
    assert all(len(t) <= TAG_CHAR_LIMIT for t in tags)


def test_tags_deduped_case_insensitively():
    brief = dict(BRIEF, keywords=["Gym Shirt", "gym shirt", "GYM SHIRT"])
    tags = build_tags(brief)
    assert len(tags) == len(set(t.lower() for t in tags))


def test_overlong_seed_tags_are_skipped_not_truncated():
    brief = dict(BRIEF, keywords=["x" * 60, "valid tag"])
    tags = build_tags(brief)
    assert "valid tag" in tags
    assert all(len(t) <= TAG_CHAR_LIMIT for t in tags)


def test_pack_carries_materials_and_faq():
    pack = build_pack(BRIEF)
    assert pack.materials == BRIEF["materials"]
    assert len(pack.faq) >= 3
    assert "made to order" in pack.description.lower()


def test_pack_warns_when_tag_slots_unfilled():
    pack = build_pack({"design_phrase": "Quiet Grind"})
    assert any("tag slots" in w for w in pack.warnings)


def test_missing_phrase_rejected():
    with pytest.raises(ValueError):
        build_pack({"product": "T-Shirt"})


def test_ip_tripwire_flags_trademarked_terms():
    warnings = check_ip_safety("Cool Disney parody shirt")
    assert warnings and "disney" in warnings[0]


def test_ip_tripwire_quiet_on_original_work():
    assert check_ip_safety("Rise or Conquer", "motivational shirt") == []


def test_pack_flags_ip_in_brief():
    brief = dict(BRIEF, design_phrase="Nike Style Hustle")
    pack = build_pack(brief)
    assert any("IP tripwire" in w for w in pack.warnings)


DIGITAL_BRIEF = {
    "design_phrase": "Cozy Bold and Easy",
    "product": "Coloring Book PDF",
    "audience": "adults who color",
    "brand": "our shop",
    "delivery_type": "digital",
    "keywords": ["coloring pages", "coloring book pdf", "bold and easy",
                 "cozy coloring", "adult coloring book"],
    "materials": ["Digital file: printable PDF — no physical item ships"],
}


def test_digital_pack_states_instant_download():
    pack = build_pack(DIGITAL_BRIEF)
    assert "instant download" in pack.description.lower()
    assert "wear" not in pack.description.lower()
    assert any("shipped" in a.lower() for _, a in pack.faq)


def test_ai_assisted_pack_carries_etsy_disclosure():
    brief = dict(DIGITAL_BRIEF, ai_assisted=True)
    pack = build_pack(brief)
    assert "use of ai" in pack.description.lower()
    assert not any("disclosure" in w.lower() and "missing" in w.lower()
                   for w in pack.warnings)


def test_seo_audit_flags_gifting_phrase_in_title():
    brief = dict(BRIEF, title_keywords=["Gift for Her"])
    pack = build_pack(brief)
    assert any("gifting phrase" in w for w in pack.warnings)


def test_seo_audit_flags_overlong_keyword_seeds():
    brief = dict(BRIEF, keywords=["a keyword seed far too long for a tag"])
    pack = build_pack(brief)
    assert any("tag limit" in w for w in pack.warnings)


def test_seo_audit_flags_wordy_titles():
    brief = dict(BRIEF, title_keywords=[
        "one two three four five six seven eight nine ten eleven twelve"])
    pack = build_pack(brief)
    assert any("fewer than" in w or "words" in w for w in pack.warnings)


def test_clean_brief_passes_seo_audit_quietly():
    pack = build_pack(BRIEF)
    assert not any(w.startswith("SEO") for w in pack.warnings), pack.warnings
