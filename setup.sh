#!/usr/bin/env bash
# One-command bootstrap: check the environment, print honest next steps.
# It installs nothing and changes nothing — it just tells you where you stand.
set -u
cd "$(dirname "$0")"

echo "Etsy POD Pipeline — environment check"
echo "======================================"

fail=0

if command -v python3 >/dev/null 2>&1; then
  echo "✓ Python: $(python3 --version 2>&1)"
else
  echo "✗ Python 3 not found — install Python 3.10+ first."
  fail=1
fi

if python3 -m pytest --version >/dev/null 2>&1; then
  echo "✓ pytest available (optional, for the test suite)"
else
  echo "· pytest not installed (optional) — run tests later with:  pip install pytest"
fi

echo
echo "Accounts this pipeline needs:"
echo "  · An Etsy shop — assumed to EXIST already; Stage 1 health-checks it (no shop yet? docs/appendix-shop-creation.md, your hands only)"
echo "  · A Printify account — physical shop types only (apparel, pet accessories); Stage 2 connects it (token goes in the connect flow, never in chat or git)"
echo
if [ "$fail" -eq 0 ]; then
  echo "You're ready. Next steps:"
else
  echo "Fix the ✗ items above, then run ./setup.sh again. Once clean:"
fi
echo "  1. Answer the intake + pick a shop type:  python3 -m pipeline.presets   (see docs/shop-types.md)"
echo "  2. Read docs/01-shop-setup.md — the intake and the existing-shop health check (fees: docs/fees-verified-2026-11-23.md)"
echo "  3. Using Muse? Point your agent at SKILL.md and say your shop type and niche."
echo "  4. Running the RiseOrConquer plan? Start at docs/starter-plan-riseorconquer.md."
echo "  5. Run the tests any time with:  python3 -m pytest"
