import pytest

from pipeline.scoring import (IP_GATE_MIN, score_candidate, score_many)


def test_strong_candidate():
    s = score_candidate("NICU nurse sweatshirt", demand=5, competition=4,
                        margin=4, ip_safety=5)
    assert s.verdict == "strong"
    assert s.weighted == pytest.approx(5 * 0.35 + 4 * 0.25 + 4 * 0.25 + 5 * 0.15)


def test_ip_gate_kills_even_a_sure_thing():
    s = score_candidate("Famous cartoon tee", demand=5, competition=5,
                        margin=5, ip_safety=IP_GATE_MIN - 1)
    assert s.verdict == "kill (IP gate)"


def test_ip_gate_boundary_is_not_killed():
    s = score_candidate("Borderline phrase", demand=3, competition=3,
                        margin=3, ip_safety=IP_GATE_MIN)
    assert s.verdict != "kill (IP gate)"


def test_weak_candidate_passes():
    s = score_candidate("Generic funny tee", demand=3, competition=1,
                        margin=2, ip_safety=5)
    assert s.verdict in ("test", "pass")


def test_out_of_range_scores_rejected():
    with pytest.raises(ValueError):
        score_candidate("X", demand=6, competition=3, margin=3, ip_safety=5)
    with pytest.raises(ValueError):
        score_candidate("X", demand=3, competition=3, margin=-1, ip_safety=5)


def test_blank_name_rejected():
    with pytest.raises(ValueError):
        score_candidate("  ", demand=3, competition=3, margin=3, ip_safety=5)


def test_score_many_ranks_and_sinks_ip_kills():
    ranked = score_many([
        {"name": "cartoon rip", "demand": 5, "competition": 5,
         "margin": 5, "ip_safety": 0},
        {"name": "solid niche", "demand": 4, "competition": 4,
         "margin": 4, "ip_safety": 5},
        {"name": "okay niche", "demand": 3, "competition": 3,
         "margin": 3, "ip_safety": 4},
    ])
    assert ranked[0].name == "solid niche"
    assert ranked[-1].name == "cartoon rip"
    assert ranked[-1].verdict == "kill (IP gate)"
