<!--
Posting notes (PROJECT.md Section 11):
- Companion piece to linkedin_article.md (the DNO/grid-operator version).
  Same underlying model, extended by notebooks/05, reframed for a different
  reader: BESS/VPP vendors and installers, and the housing-association asset
  managers who buy from them.
- Attach figures/battery_utilisation_by_envelope_state.png directly to the
  post -- it carries the headline finding on its own.
- Deliberately England-grounded throughout (English Housing Survey, RdSAP
  conventions, Warm Homes: Social Housing Fund). Do not imply this transfers
  to other UK nations without re-deriving against their own data -- see the
  Scope section below. If a Scotland-specific version is ever built, it's a
  separate piece with separate sourcing, not this one relabelled.
- Publish this first; any outreach to a specific vendor (e.g. offering a
  bespoke version for their stock) happens after, and separately from,
  this public piece.
- MIT LICENSE added at the repo root (2026) covering the code only, not the
  third-party data cited in citations.md -- the "MIT-licensed notebooks"
  claim in the intro below is now accurate; keep the LICENSE file in sync
  if that claim is ever removed or the license changes.
- The bill-saving/VPP split in "The revenue is real" section below is a
  REASONED mechanism, not a modelled result -- notebooks/05 applies the
  GBP 1,075/year revenue figure as a flat archetype-level estimate,
  identical across all three fabric states (see the notebook's own
  "retrofit does not change whether a battery CAN cover peak demand, only
  how much of its capacity that costs" comment). Keep this caveat attached
  to the claim, not just buried in Scope, if this section is edited further.
-->

# Your battery in leaky housing stock is a bill-savings product. In insulated housing stock it's a flexibility asset — the grid pays for the headroom the fabric frees.

*Same hardware, same warranty — the walls decide which market you're in.*

If you sell, install, or fund LFP batteries into social housing in England, one question is worth quantifying before the next rollout: how much of that battery's usable capacity does a leaky home eat before you ever get to dispatch it for anything else?

I built a physics-based digital twin of a pre-1919 solid-wall terrace archetype — a meaningful share of English social housing — and extended it to a battery+solar+VPP comparator, using the same envelope physics and the real December 2022 cold snap as the rest of the model. English Housing Survey data throughout; the underlying model has been through two rounds of external technical review with the corrections published alongside the findings, every input is tagged by evidence status (grounded, provisional, or deliberately omitted) in the linked MIT-licensed notebooks, and every headline figure is hand-reproducible from the config files.

## The constraint isn't power. It's energy.

A domestic battery's power rating is never the bottleneck. Real UK products range 3.6–11.5 kW continuous, and even an unretrofitted home's peak electrical demand tops out at 2.46 kW — comfortably within reach at any fabric state.

Energy is a different story. To fully cover one home's 16:00–20:00 evening peak with the battery alone: an unretrofitted home asks a standard 10 kWh battery for 9.84 kWh — **98% of its usable capacity, every single evening.** Partial fabric work only leaves 8.24 kWh, **82%.** Only a full EPC-C retrofit changes the picture: 2.64 kWh, **26%.**

**[Insert chart: battery_utilisation_by_envelope_state.png]**

Same battery, same install, same warranty. The difference is what's left over. In an unretrofitted home, there's essentially nothing beyond holding comfort through one peak — no slack for a colder-than-usual evening, and a real risk that a slightly worse night drains the battery before the peak window ends, at exactly the moment a tenant overrides the system and the flexibility asset is lost for that day. In an EPC-C home, three-quarters of the battery is still there to work with.

## The market gap is large

Fabric retrofit adoption on this estate sits at **27%** (English Housing Survey, tenure-weighted); BESS/solar adoption is roughly **5.8%** — a back-derived, order-of-magnitude estimate from installer and tenure data, not a directly published rate. Fabric is retrofitted on this stock at roughly **4.6×** the rate battery storage is installed. The Warm Homes Fund change from February 2026 is too recent to show up in adoption data yet; worth watching, not yet worth assuming.

## The revenue is real — which makes wasted headroom a real cost

A battery genuinely is metered, dispatchable, and contractible today (unlike fabric's own flexibility value, which structurally can't be sold into a metered tender). On this archetype: roughly **£120–300/year** in VPP dispatch plus **£800–950/year** in time-of-use arbitrage — two distinct, stackable streams, combining to roughly **£1,075/year**, against a bundled installed cost of about **£13,500** (4 kWp solar + 10 kWh battery), for a **~12.6-year** payback.

That payback math assumes the battery is actually available to dispatch and arbitrage beyond the comfort-holding peak. Here's the mechanism — reasoned from the physics above, not separately modelled: this project's own comparator applies the £1,075 figure as a flat, archetype-level estimate, the same for all three fabric states, not something tested state-by-state or against a real dispatch log. Plausibly, though, the two revenue streams don't fail the same way in leaky stock. The bill-saving half needs no spare capacity, just a load to serve, so it likely survives: the battery still charges cheap and discharges into the evening load regardless of how insulated the walls are. The VPP half needs headroom beyond that load — and in an unretrofitted home there's almost none left to sell. The grid and the wholesale market between them pay for that headroom; the commercial case and the fabric case point the same direction, for the same underlying physical reason. Worth testing against real dispatch data before anyone underwrites it (see Scope).

## What this means if you sell, install, or finance these assets

1. **Your best-performing market is the insulated 27%.** A battery behind an EPC-C meter keeps roughly three-quarters of its capacity free every evening — dispatches land, arbitrage margins are real, tenants stay warm without overriding the system. That segment converts to low-churn, reference-able customers.

2. **Follow the fabric pipeline, not just the battery pipeline.** The Warm Homes: Social Housing Fund now lets landlords add batteries under the same grant as solar, and SHDF and council programmes are turning unretrofitted streets into EPC-C streets. A rollout co-located with a fabric programme inherits the 26% utilisation profile instead of the 98% one — 7.2 kWh of every 10 kWh battery freed, every peak evening. That's a different product economics.

3. **Don't underwrite VPP revenue against a 98%-utilised battery.** In unretrofitted stock, position the product for what it can actually deliver — bill savings, resilience, comfort — or be honest that partial fabric work won't rescue a dispatch business case; only a full package changes the picture, and that's landlord spend, not yours. The plain-English read: sell it as bill savings where the walls are leaky; underwrite it as flexibility where they're not.

## Scope, briefly

This is straightforward arithmetic — peak electrical demand × 4-hour window, against nominal battery capacity — not a full dynamic dispatch simulation with state-of-charge tracking or modelled tenant-override thresholds; that's a natural next step, not something this model has done yet. That includes the bill-saving/VPP split argued above: it's reasoned from the same static peak-window arithmetic as everything else here, not a separately modelled or field-verified result — treat it as a hypothesis worth testing against real dispatch logs, not a finding on the same footing as the utilisation percentages. Single archetype, English Housing Survey and RdSAP-derived assumptions throughout, English funding mechanisms only. If your stock, funding routes, or geography differ materially — Scotland's stock, funding, and tenure history in particular look quite different — the physical mechanism (fabric determines how hard a battery has to work) very likely still holds, but the specific numbers don't transfer without re-deriving against the right data first.

## If this is useful

I'd like to hear from anyone installing or specifying batteries into social housing where this headroom question is live — particularly if you hold dispatch logs or stock-condition data by EPC band. I'd genuinely like to compare the archetype against field data, and it would sharpen the next stage of the work.

Full model, every notebook, every citation: link in the comments.
