"""
build_lifetime_economics_chart.py

Builds the one figure Finding 8 never got: a cumulative net-cash-position
chart over the fabric's 36-year working life. Every input below is read
from FINDINGS.md's own stated numbers (Finding 5, Finding 8), not
re-derived -- this script only draws the line between two already-grounded
endpoints (year 0: -£10,728 outlay; year 36: +£60,706 net) and marks the
already-grounded 5.4-year payback point.

Straight-line interpolation is a deliberate simplification, flagged in the
chart's own footnote: real bill savings would compound with future
electricity price changes, which this project does not model (flat
26.11p/kWh throughout, per FINDINGS.md Finding 7). The implied annual
saving from this straight line (£71,434 / 36 = £1,984.3/yr) matches
FINDINGS.md's own stated £1,984/yr almost exactly, so the simplification
does not silently introduce a new number.

Output: ../figures/lifetime_economics_by_year.png
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Same palette already used in notebooks/06 for this project's other charts
RUST = "#a65852"
GREEN = "#4c7c59"
GREY = "#555555"

# Grounded endpoints (FINDINGS.md Finding 5, Finding 8) -- not re-derived
CAPEX_GBP = 10_728
NET_LIFETIME_GBP = 60_706
GROSS_LIFETIME_SAVINGS_GBP = 71_434
FABRIC_LIFE_YEARS = 36
PAYBACK_YEARS = 5.4  # FINDINGS.md Finding 8, stated directly

years = [0, FABRIC_LIFE_YEARS]
cumulative = [-CAPEX_GBP, NET_LIFETIME_GBP]

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.edgecolor": GREY,
    "axes.linewidth": 0.6,
    "text.color": "#222222",
    "axes.labelcolor": "#222222",
    "xtick.color": GREY,
    "ytick.color": GREY,
})

fig, ax = plt.subplots(figsize=(9, 5.2), dpi=150)

x = [0, PAYBACK_YEARS, FABRIC_LIFE_YEARS]
y = [-CAPEX_GBP, 0, NET_LIFETIME_GBP]

ax.plot(x, y, color="#222222", linewidth=2.2, zorder=4)
ax.fill_between([0, PAYBACK_YEARS], [-CAPEX_GBP, 0], 0, color=RUST, alpha=0.18, zorder=1)
ax.fill_between([PAYBACK_YEARS, FABRIC_LIFE_YEARS], [0, NET_LIFETIME_GBP], 0, color=GREEN, alpha=0.18, zorder=1)

ax.axhline(0, color=GREY, linewidth=0.8, zorder=2)
ax.axvline(PAYBACK_YEARS, color=GREY, linewidth=0.8, linestyle=":", zorder=2)

ax.plot([0], [-CAPEX_GBP], marker="o", markersize=7, color=RUST, zorder=5)
ax.plot([PAYBACK_YEARS], [0], marker="o", markersize=7, color="#222222", zorder=5)
ax.plot([FABRIC_LIFE_YEARS], [NET_LIFETIME_GBP], marker="o", markersize=7, color=GREEN, zorder=5)

ax.annotate(f"£{CAPEX_GBP:,.0f} outlay\n(year 0)", xy=(0, -CAPEX_GBP), xytext=(2.2, -CAPEX_GBP - 2200),
            fontsize=9.5, color=RUST, fontweight="bold", ha="left")
ax.annotate(f"Payback: {PAYBACK_YEARS} years", xy=(PAYBACK_YEARS, 0), xytext=(PAYBACK_YEARS + 1.3, 9500),
            fontsize=9.5, color="#222222", fontweight="bold", ha="left",
            arrowprops=dict(arrowstyle="-", color="#222222", linewidth=0.8))
ax.annotate(f"£{NET_LIFETIME_GBP:,.0f} net saved\n(year {FABRIC_LIFE_YEARS})", xy=(FABRIC_LIFE_YEARS, NET_LIFETIME_GBP),
            xytext=(FABRIC_LIFE_YEARS - 15.5, NET_LIFETIME_GBP + 3500),
            fontsize=9.5, color=GREEN, fontweight="bold", ha="left")

ax.set_xlim(0, FABRIC_LIFE_YEARS)
ax.set_ylim(-CAPEX_GBP - 5000, NET_LIFETIME_GBP + 8000)
ax.set_xlabel("Years since retrofit")
ax.set_ylabel("Cumulative net position (£/home)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"£{v:,.0f}"))
ax.set_title("Fabric retrofit crosses from cost to net saving in 5.4 years,\nthen keeps paying for 30 more",
             fontsize=13.5, fontweight="bold", loc="left", pad=14)

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

fig.text(0.02, -0.02,
          "Straight-line illustration between two grounded endpoints (FINDINGS.md Finding 5, Finding 8): £10,728 capital cost,\n"
          f"£{GROSS_LIFETIME_SAVINGS_GBP:,.0f} gross lifetime bill savings, 36-year fabric life (Ofgem ECO/Green Deal convention). Assumes flat\n"
          "26.11p/kWh electricity price throughout, not modelled to escalate -- a conservative, not favourable, simplification.",
          fontsize=7.8, color=GREY, va="top")

plt.tight_layout(rect=[0, 0.06, 1, 1])
out = os.path.join(os.path.dirname(__file__), "..", "figures", "lifetime_economics_by_year.png")
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Wrote {out}")
