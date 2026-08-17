<!--
Posting notes (PROJECT.md Section 11):
- Sixth companion piece in the fabric/battery series, following the VPP-
  funded-battery ladder article. That piece closed the financing question
  (who pays for the battery). This one picks up a separate question nobody
  in the series had asked yet: does the battery's own daily cycling, once
  installed, carry a carbon benefit distinct from the fabric retrofit's own
  heating-carbon saving (Finding 7)? Short answer: yes, and in a retrofitted
  home it's roughly as large as Finding 7's existing figure -- a genuine
  addition to the carbon case, not a restatement of it.
- Built entirely from src/check_headroom_revenue_scaling.py section 6 and
  ADDENDUM.md's "Carbon check, 17 Aug 2026" section -- every figure here
  traces to that script's output, hand-verified 17 Aug 2026.
- Two distinct claims, two distinct confidence levels, and this piece is
  deliberately built to keep them visibly separate rather than blend them
  into one clean number:
    1) Finding 7's existing 0.131 kgCO2e/kWh DESNZ average-grid figure --
       re-checked this session, majority-supported but flagged UNRESOLVED
       (one conflicting source at 0.207 kg/kWh, primary DESNZ spreadsheet
       not machine-readable via available tools).
    2) The new dispatch-carbon figures themselves (0.027 / 0.240 / 0.989
       tCO2e/yr) -- these inherit whatever uncertainty sits under (1), plus
       their own scaling assumptions (headroom-scaled like the revenue
       figures, marginal grid factor back-derived from Finding 7's own
       2.7-3.0 tCO2e/yr rather than independently sourced).
  Do not simplify this into "the battery saves X tonnes of CO2" without the
  UNRESOLVED caveat attached -- that's the exact overclaim discipline this
  whole project exists to avoid.
- Does not name vendors. Stays at the level of the mechanism and the
  project's own numbers, consistent with the ladder article's scope.
-->

# The battery was already justified. It turns out it's also doing more than we counted.

*Every carbon figure in this project so far came from the fabric — walls, loft, windows. Nobody had asked yet what the battery's own daily cycling is worth, separately, in carbon terms. It turns out the answer isn't a rounding error.*

This project's carbon case has always rested on Finding 7: retrofitting a pre-1919 solid-wall terrace to EPC-C saves roughly 1.0 tonne of CO2e a year on the average grid-carbon basis, because less gas gets burned for heat. That number has never depended on a battery being present at all. What hadn't been asked, until this month, is whether a battery sitting in that same retrofitted home — cycling daily for arbitrage and grid-service revenue, entirely for financial reasons — was quietly doing carbon work nobody had costed.

## The mechanism, stated plainly

A battery on a daily arbitrage cycle charges overnight, when the grid is cheaper and cleaner, and discharges into the early-evening peak, when it's more expensive and, on average, dirtier — generation at the margin during peak demand leans more on higher-carbon plant than the round-the-clock average. Every kWh the battery discharges at 6pm instead of drawing from the grid directly is a kWh of peak-time generation avoided. That's a real, physical carbon saving, distinct from — and additive to — the heating-carbon saving fabric retrofit already delivers.

It's also, notably, the same daily cycle this project's own VPP revenue figures already depend on (the £875/year arbitrage component from the funding-ladder piece). The money and the carbon saving come from the same physical action. Nobody had put a number on the carbon half of it before.

## What the numbers say

Using this project's existing carbon-intensity figures and the same headroom-scaling logic already applied to VPP revenue — a battery's usable cycling capacity depends on how much spare capacity a home's fabric state leaves free — the dispatch-carbon saving comes out at roughly **0.027 tonnes CO2e a year** for an unretrofitted home, **0.240 tonnes** for a wall-insulation-only home, and **0.989 tonnes** for a fully retrofitted EPC-C home.

That last figure is the one worth sitting with. It's almost exactly as large as Finding 7's own 1.0-tonne heating-carbon saving. Put together, a fully retrofitted home with a battery cycling for VPP revenue is plausibly saving close to **double** the carbon this project had counted before — roughly 2 tonnes a year rather than 1 — and the second tonne was never the point of installing the battery in the first place. It's a side effect of a financial decision, not something anyone engineered for.

The same pattern that shows up everywhere else in this project shows up here too: the carbon benefit scales with how much fabric work has already been done. An unretrofitted home's battery barely moves the needle (0.027 tonnes). A fully retrofitted one earns a saving almost as large as the fabric itself delivered. Fabric isn't just a precondition for the VPP financing case to make commercial sense — it's also what makes the battery's own carbon contribution worth having.

## Why this isn't reported as one clean number

Two separate pieces of uncertainty sit underneath these figures, and collapsing them into a single confident claim would repeat a mistake this project has already caught itself making elsewhere.

First, Finding 7's underlying grid-carbon figure — 0.131 kgCO2e/kWh on the DESNZ average-grid basis — was re-checked this session against DESNZ's June 2026 conversion-factor release, which cut the reported UK electricity factor by roughly 26% through a revised methodology. Three independent sources corroborate a figure in the 131–141 gCO2e/kWh range, consistent with what this project already uses. One other source states 0.207 kg/kWh instead, and the primary DESNZ spreadsheet couldn't be read directly to settle the discrepancy. Majority evidence supports the existing figure. It is not confirmed to primary-source certainty, and is flagged accordingly.

Second, the dispatch-carbon figures above use a marginal grid-carbon factor back-derived from Finding 7's own reported 2.7–3.0 tonne marginal-basis range, rather than an independently sourced marginal-intensity figure for evening peak hours specifically. That's a reasonable approximation, consistent with how this project has treated marginal-versus-average carbon accounting elsewhere — but it's an internally derived number, not a third-party-verified one, and should be read as an order of magnitude rather than a precise annual figure.

Neither of those caveats changes the direction or the rough scale of the finding. Both are reasons to say "roughly a tonne, worth taking seriously" rather than "0.989 tonnes, full stop" — which is the more honest claim, and the only one this project's own discipline permits.

## What this doesn't do

This isn't new money and it isn't new fabric savings — it's a separate accounting of a benefit that already existed physically the moment a battery started cycling for VPP revenue, just never quantified. It doesn't change the retrofit's own business case, which needs no battery to stand on. And it doesn't get added to any revenue figure elsewhere in this project — carbon and cash are counted separately here, deliberately, to avoid double-counting one physical action as two different kinds of benefit.

What it does is close a genuine gap. A battery installed for financial reasons, in a home retrofitted for financial and comfort reasons, turns out to be doing climate work nobody asked it to do and nobody had measured. That's a better story than the one this project was telling a month ago, and it's a more honest one — with the uncertainty attached, not smoothed over.

Full model, every notebook, every citation: link in the comments.
