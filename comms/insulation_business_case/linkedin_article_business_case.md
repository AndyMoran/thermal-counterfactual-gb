<!--
Posting notes (PROJECT.md Section 11):
- Fourth companion article, and the first written for a decision-maker
  audience rather than a technical/policy one: CEOs and portfolio leaders,
  facilities/asset managers, and Housing Association leadership. Unlike
  the three earlier articles (linkedin_article.md / DNO-grid, _bess_vendors
  / commercial, _negawatt / policy), this one is deliberately structured
  as three short sections for three different readers, because that's
  literally its subject -- the same physics, three different "so what"s.
- This is the SOURCE article for a 3-part SHORT-POST mini-series (a
  follow-up to the original 3-part series, not a continuation of it --
  that series is already closed). linkedin_post_ceo.md,
  linkedin_post_facilities.md, and linkedin_post_ha_leader.md each lead
  with a different section of THIS one article and link to the same URL
  in the first comment. Space them across separate weeks (e.g. Tuesday /
  Thursday / Tuesday, same cadence convention as the original series),
  not consecutive days, so each gets its own engagement window.
- Built from STAKEHOLDER_BRIEFS.md, lightly rewritten for external tone --
  the internal "Finding N" citations are kept as parenthetical source tags
  rather than removed, since the caveats they anchor (the EUV-SH inference,
  the dual-basis carbon reporting, the not-yet-modelled combined-CapEx
  idea) are exactly what makes this credible to a reader who will
  push back, not decoration to trim for brevity.
- UPDATE 14 Aug 2026: the closing section ("The idea I checked") originally
  flagged the reader's ~40% combined-CapEx claim as unproven. It has now
  actually been checked -- src/check_combined_capex_hypothesis.py -- rather
  than left as a flagged guess. Result: ~33% combined CapEx reduction
  (battery component ~41%, well-evidenced from real UK SKU pricing;
  heat pump component ~29%, real but much less precisely costed, bounded by
  a practical minimum-unit-size floor no thermal-load ratio alone captures).
  Real per-property grant caps now grounded too: BUS (flat £7,500/ASHP,
  gov.uk/Ofgem) and WHSHF Wave 3 cost caps (£7,500 base + £7,500 off-gas or
  £20,000-for-10%-quota on-gas, cross-checked against a specialist advisory
  source working directly on WHSHF Wave 3 compliance). New finding not in
  the original hypothesis: WHSHF Wave 3's core scope is EPC bands D-G, so
  heat pump and fabric should be bundled into one application, not
  sequenced -- a home already at EPC-C loses core eligibility. Keeping the
  full honest arc (flagged unproven -> actually checked -> partially
  confirmed, narrower and less certain than the original number) visible
  in this file is the same discipline the rest of this project holds
  itself to. Full detail lives in ADDENDUM.md, deliberately kept separate
  from PROJECT.md's core Assumptions Ledger (Section 8.6 there now just
  points here) -- this check runs at a visibly lower evidence standard
  than the reviewed core record and shouldn't be blended into it silently.
- Attach figures/lifetime_economics_by_year.png directly (built for this
  article specifically -- no chart previously existed for Finding 8's
  lifetime economics).
-->

# The retrofit business case nobody's making

*A CEO, a facilities manager, and a housing association leader each ask a different question about the same retrofit. Here's the honest answer to all three — and the one claim about it I couldn't stand behind.*

Fabric retrofit on a pre-1919 solid-wall terrace is real, physically grounded, and pays for itself — that's what the modelling behind this series has shown so far. What it hasn't done yet is answer the question that actually gets capital released: so what, specifically, for the person who has to sign off on it? Three different people ask that question differently. Here's what the same numbers mean for each of them.

## For the CEO: this is a cash-positive balance sheet play, not an ESG cost

Full fabric retrofit pays for itself in 5.4 years, then nets **£60,706 per home, not spent, over the remaining 30 years** of its working life — against a £10,728 outlay, using nothing but bill savings that already happen today (Finding 8). Scaled to a 1,000-home portfolio at full uptake, that's £1.98m/year in avoided bills; at today's actual 27% uptake, it's already running at roughly £536,000/year (Finding 7).

Once lifetime bill savings are properly netted against the capital cost — the standard treatment in any real marginal abatement cost curve — the cost per tonne of carbon abated is **negative**: roughly –£1,694/tCO2e on an average-grid basis, or –£555 to –£635/tCO2e on a marginal-emissions basis (Finding 8). That's cash-positive decarbonisation before any carbon value is even counted. For anyone who has to report the volume too: that's ~1.0 tCO2e/home/year on the average-grid basis, or 2.7–3.0 tCO2e/home/year on a marginal basis — roughly 996 tCO2e/year at full 1,000-home uptake (Finding 7).

Underneath the upside sits a real, dated exposure: Minimum Energy Efficiency Standards are being extended to social housing for the first time (one EPC metric by 2030, a second by 2039), and the reformed Decent Homes Standard folds the same requirement into Criterion D, compliant by 2035 (Finding 6). A home that misses either deadline is a landlord-specific financial exposure, not just tenant discomfort — and usefully, the regulation itself caps the downside: a time-limited £10,000-per-property spend cap is a known ceiling on required capital, not an open-ended one.

## For the facilities team: sequence it, don't silo it

The single most actionable fact in this whole series: **a post-retrofit home needs only 26% of a standard battery's capacity to cover the evening peak, versus 98% for an unretrofitted one** (Finding 6). If fabric and battery rollouts are planned as separate workstreams, doing fabric first changes what "adequate battery provision" means for everything that comes after it.

The same physics shows up as avoided peak demand: 2.46 kW/home drops to 0.66 kW/home at a heat pump COP of 2.5 — **1.80 kW/home, or 1.8 MW per 1,000 homes retrofitted** (Finding 1). That's a real number for a DNO conversation about local network headroom or EV charging capacity.

Two spec-level considerations, both real mechanisms but neither quantified for this specific archetype: external wall insulation plausibly outperforms internal wall insulation on summer comfort (CIBSE TM59); and rooftop solar added at scale on one street pushes power back onto the LV network at exactly the times statutory voltage limits are most likely to bind (Finding 7) — worth a conversation with the DNO before phasing solar street-by-street rather than after.

And a delivery-model fact worth knowing before fielding "why haven't we done more battery/solar": fabric already reaches 27% of this estate, while battery/solar sits at roughly 5.8% — not because it's less valuable, but because fabric has been landlord-funded and programme-driven, while battery/solar has historically been an individual purchase, with its revenue accruing to whoever holds the electricity account (usually the tenant, not the landlord funding the install). Since February 2026, the Warm Homes Social Housing Fund lets landlords fund battery storage under the same mechanism as solar — the first real route that could close this gap.

## For the housing association: this is compliance and balance-sheet protection with a fixed price tag

Two regulatory deadlines make this a "when," not an "if" (Finding 6). Housing association stock is carried on the balance sheet at Existing Use Value-Social Housing (EUV-SH) — a rental-income-based valuation lenders assess covenants against. A home that misses MEES or Decent Homes Criterion D is a live exposure against that valuation. Fabric retrofit is what a landlord spends against it: it moves the EPC band and satisfies Criterion D directly. A battery does neither — it isn't a scored EPC input, and it protects no balance-sheet figure, whatever its own real financial upside.

On cost: £10,728/home for this specific archetype (not the cheaper £6,335 blended national figure, which understates it), paid back from bills alone in 5.4 years, with a £10,000/property spend cap as a known ceiling on required compliance cost. On funding: the Warm Homes Social Housing Fund (£1.29bn total programme) already underpins delivery, and its February 2026 extension to battery storage is the first mechanism letting landlords fund both fabric and battery under one grant route.

One channel worth ruling out of any funding pitch: this project's own illustrative flexibility-service revenue figure (£127/home/year) would take roughly 84 years to repay the retrofit — never a realistic revenue case, since passive fabric has no meter and can't bid into flexibility markets (Finding 5). The real financial case is bill savings plus compliance-exposure avoidance, not flexibility-market income.

## The idea I checked

This article exists because a reader proposed a sharper claim than any of the above: that fabric-first sequencing cuts combined battery-plus-heat-pump CapEx by around 40%, letting Housing Association deals fit under grant caps. When this article first went out, that was flagged as an unproven hypothesis — no heat pump costing existed anywhere in this project, and the grant figures grounded here were a total programme size and a MEES compliance *spend* cap, not real per-property *grant* caps. Since then, it's been checked properly rather than left as a guess. Three separate results, at three different confidence levels — reported separately, not blended into one falsely precise number.

The battery side is solid: Finding 6 already showed a post-retrofit home needs only 26% of a 10kWh battery's energy versus 98% pre-retrofit. Mapped onto real UK product tiers — baseline needs a 10kWh-class battery, EPC-C fits comfortably inside a 5kWh-class one — that's roughly a **41% lower battery cost**, using multiple 2026 UK market surveys at the same evidentiary standard as this project's existing battery-cost figures.

The heat pump side is real but smaller, and less precisely costed. This project's own physics (unchanged code, just multiplied through by COP) gives a required thermal output of 6.15kW for baseline and 1.65kW for EPC-C — a 73% reduction in heating load. But no UK heat pump is sold at 1.65kW: the smallest practical domestic units cluster around 4–6kW, so an EPC-C home can't actually buy a unit sized to its true load — it buys the smallest tier available, same as a baseline home buying the 6–8kW tier its own larger load calls for. Triangulated from multiple 2026 UK installer surveys (no single official size-banded cost table exists, so this is the weakest-evidenced number in this whole series), that gap is worth roughly **29% off the heat pump's cost** — real, but far short of the 73% the raw thermal-load ratio would suggest, because of that practical minimum-size floor.

Combined, weighted by each component's own cost rather than averaged: **~33% lower combined CapEx** — in the same order of magnitude as the original 40% claim, not a precise match, and I'd treat this as a plausible range (roughly 25–40%) rather than a single number, given how much less solid the heat pump half is.

The grant-cap part of the hypothesis checks out, and turned up something sharper than "it fits": the Boiler Upgrade Scheme gives a **flat £7,500** toward an ASHP regardless of its size — which covers maybe 70% of a baseline-sized unit's cost, but close to the *entire* cost of a fabric-enabled, right-sized one. And Warm Homes: Social Housing Fund Wave 3 has real per-property cost caps — £7,500 per home for any measure (50:50 match funded), plus £7,500 more for off-gas-grid heating or up to £20,000 for a 10%-of-application quota on-gas-grid. One thing this turned up that the original hypothesis didn't anticipate: WHSHF Wave 3's core scope is EPC bands D–G — a home already moved to EPC-C is only eligible for further funding under a restricted 10%-quota route. That's a real sequencing implication: bundle the heat pump into the *same* application as the fabric retrofit, before the EPC band moves, rather than fund them in separate rounds.

So: directionally right, materially real, and not a guess anymore — just not exactly 40%, and the honest range is wider than one number implies.

## Scope, honestly

Single archetype — a mid-terrace, the physically favourable solid-wall form; other forms cost more to treat. Carbon is basis-dependent and reported as such throughout. The EPC-to-EUV-SH valuation link is this project's own reasoned inference from real compliance exposure, not an independently sourced valuation methodology — directionally sound, not independently verified. The lifetime economics are simple, undiscounted arithmetic over a sourced 36-year fabric life, assuming flat electricity prices throughout, not a discounted-cash-flow appraisal. None of that changes the direction of any figure above; it's what should travel with them into a board paper.

Full model, every notebook, every citation: link in the comments.
