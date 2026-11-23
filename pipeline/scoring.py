"""Candidate scorer — Stage 3's due-diligence rubric as code.

Research judgement, made repeatable. A candidate product (from the
Stage 3 method in ``docs/03-research.md``) is scored 0–5 on four
signals:

- **demand** — proven buyers: review counts and recency on comparable
  listings, search volume, bestseller badges.
- **competition** — scored as *room to enter*: 5 means few, weak
  listings own the niche; 0 means a saturated wall of strong shops.
- **margin** — what the pricing calculator leaves at a realistic
  price in the niche's band (use ``pipeline/pricing.py`` first).
- **ip_risk** — scored as *safety*: 5 means the concept is clean by
  construction (your words, your art); 0 means it leans on someone
  else's brand, character, or phrase.

Weighted total (demand 35%, competition 25%, margin 25%, IP safety
15%) maps to a verdict. **IP safety is also a hard gate**: below 3,
the verdict is "kill" no matter how good the rest looks — that is
the pipeline's IP doctrine (Stage 3 checklist) expressed as code.

The scorer does not fetch anything and invents nothing: you bring
the evidence, it does the arithmetic and keeps you honest about the
gate.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass

WEIGHTS = {"demand": 0.35, "competition": 0.25, "margin": 0.25, "ip_safety": 0.15}
SIGNALS = tuple(WEIGHTS)
IP_GATE_MIN = 3.0       # below this IP-safety score the candidate dies
STRONG_MIN = 3.5        # weighted score at/above: strong candidate
TESTABLE_MIN = 2.5      # weighted score at/above: worth one test listing


@dataclass
class CandidateScore:
    name: str
    demand: float
    competition: float
    margin: float
    ip_safety: float
    weighted: float
    verdict: str  # "strong" | "test" | "pass" | "kill (IP gate)"


def _check(value: float, signal: str) -> float:
    if not 0.0 <= value <= 5.0:
        raise ValueError(f"{signal} score must be between 0 and 5, got {value}")
    return float(value)


def score_candidate(name: str, *, demand: float, competition: float,
                    margin: float, ip_safety: float) -> CandidateScore:
    """Score one candidate. All four signals are required — a
    candidate you cannot score is a candidate you have not researched.
    """
    if not name or not name.strip():
        raise ValueError("candidate needs a name")
    scores = {
        "demand": _check(demand, "demand"),
        "competition": _check(competition, "competition"),
        "margin": _check(margin, "margin"),
        "ip_safety": _check(ip_safety, "ip_safety"),
    }
    weighted = round(sum(scores[s] * WEIGHTS[s] for s in SIGNALS), 2)
    if scores["ip_safety"] < IP_GATE_MIN:
        verdict = "kill (IP gate)"
    elif weighted >= STRONG_MIN:
        verdict = "strong"
    elif weighted >= TESTABLE_MIN:
        verdict = "test"
    else:
        verdict = "pass"
    return CandidateScore(name=name.strip(), weighted=weighted, verdict=verdict, **scores)


def score_many(candidates: list[dict]) -> list[CandidateScore]:
    """Score a list of candidate dicts (keys: name, demand,
    competition, margin, ip_safety) and rank them, best first.
    IP-killed candidates sort last regardless of weighted score."""
    scored = [score_candidate(
        c["name"], demand=c["demand"], competition=c["competition"],
        margin=c["margin"], ip_safety=c["ip_safety"]) for c in candidates]
    return sorted(scored, key=lambda s: (s.verdict == "kill (IP gate)", -s.weighted))


def format_score(s: CandidateScore) -> str:
    return (f"{s.name}: demand {s.demand:.0f} · competition {s.competition:.0f} · "
            f"margin {s.margin:.0f} · IP safety {s.ip_safety:.0f} "
            f"→ weighted {s.weighted:.2f} → {s.verdict.upper()}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python3 -m pipeline.scoring <candidates.json>", file=sys.stderr)
        return 2
    with open(argv[1], encoding="utf-8") as fh:
        data = json.load(fh)
    candidates = data["candidates"] if isinstance(data, dict) else data
    for s in score_many(candidates):
        print(format_score(s))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
