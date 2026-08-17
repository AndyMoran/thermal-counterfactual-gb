<!--
Posting notes (PROJECT.md Section 11):
- Companion piece to linkedin_article_bess_vendors.md, same audience (BESS/VPP
  vendors, installers, aggregators, and the HA asset managers who buy from
  them), picking up where that piece's point 2 ("follow the fabric pipeline")
  left off. That article established fabric determines battery utilisation
  (98% vs 26%); this one asks whether a VPP could go further and fund the
  battery itself in exchange for dispatch rights, and prices out whether
  that's actually a fundable deal rather than just a plausible idea.
- Built from ADDENDUM.md's "VPP-funded-battery ladder: Rung 2" section and
  src/check_headroom_revenue_scaling.py -- every figure traces to that
  script's output, hand-verified.
- Keeps the wide GBP880-GBP10,252 lifetime-margin range deliberately, same
  reasoning as the companion HA-audience piece -- a vendor reading this
  should see the real range they'd be underwriting, not a single flattering
  number.
- Does not name specific battery vendors or chemistries (Kight, sodium-ion,
  etc.) -- that's a separate, differently-framed piece.
-->

# We priced out funding the battery yourselves. Here's the honest number.

*Not "should you fund batteries into social housing" — the arithmetic for whether it actually pays back, using this project's own physics and real UK revenue data.*

The last piece in this series established that fabric retrofit determines how hard a battery has to work — 98% of a 10kWh battery's usable capacity in an unretrofitted home, versus 26% in an EPC-C one. The obvious next question from readers wasn't whether to follow the fabric pipeline. It was sharper: if that spare capacity is worth real money to a VPP, why should the landlord be the one funding the battery at all?

So we priced it. Not as a pitch — as a check, using the same evidence discipline as the rest of this project.

## The revenue figure needed fixing before the arithmetic meant anything

This project's own VPP-plus-arbitrage revenue estimate — roughly £1,075/year — has always been a flat figure, applied the same regardless of how much spare capacity a battery actually has free. That was defensible for the question it was first built to answer. It's the wrong number for underwriting a battery-financing decision.

Split properly, using real UK VPP payment structures: roughly £210/year comes from short dispatch and frequency-response events (Axle Energy's published ~£1/kWh rate is a useful anchor), and roughly £875/year from time-of-use arbitrage — the classic cheap-overnight-charge, expensive-evening-discharge cycle. That arbitrage window sits inside the same 4pm–8pm peak a home's own comfort-holding draw competes for, so it scales with spare capacity by fabric state. The dispatch component doesn't obviously scale the same way — short grid-service events aren't tied to that specific window — so we left it flat, on the conservative assumption that we shouldn't invent precision we don't have. (Worth flagging: real frequency-response events plausibly cluster during winter system stress, which is exactly when a leaky home's own draw is highest too — if anything this makes the flat treatment optimistic for unretrofitted stock, not conservative.)

Headroom-scaled, not flat: **£228/year in an unretrofitted home, £368/year with wall insulation only, £858/year in a fully retrofitted EPC-C home.** The flat figure this project used before overstated leaky-stock revenue by roughly 4.7x.

## The payback, priced properly

Funding a 10kWh battery (£5,500, real UK product-tier pricing) in exchange for dispatch rights, using the headroom-scaled revenue: **6.4 years in an EPC-C home.** In wall-insulation-only stock, **15 years** — marginal at best. In unretrofitted stock, **24.2 years** — not a fundable deal on these numbers, full stop.

That last figure matters commercially, not just physically: it's the honest reason to decline funding a battery ahead of a fabric programme, stated as a number rather than a hunch. If you're being asked to fund batteries into stock that hasn't been retrofitted yet, this is the arithmetic that says no — and the one that says yes changes entirely once fabric's gone in first.

## The range you'd actually be underwriting

Payback isn't the whole story — what matters commercially is the margin over the rest of the battery's working life, and that depends on how long the battery actually lasts. The real, peer-reviewed literature on residential Li-ion life (Beltran, Ayuso & Pérez, *Energies*, 2020) gives a wide range: 7.44 to 18.37 years to a 60%-capacity threshold, reflecting genuine climate and usage variation, not sloppy sourcing.

At the pessimistic end of that range, the margin after payback in an EPC-C home is **£880** — thin. At the central, industry-standard-warranty estimate (15 years), **£7,362**. At the optimistic end, **£10,252**. Any real underwriting decision should be priced against that whole range, not the middle of it — the pessimistic case is the one that tells you what you're actually risking, not the one that makes the deck look good.

## What this means if you're structuring one of these deals

1. **Fund the full-size battery, not the right-sized one.** A comfort-only EPC-C battery is a 5kWh-class unit — cheaper, but it removes the spare capacity you're funding it to capture. The deal only works funding the 10kWh-class unit even in a retrofitted home, deliberately oversized relative to what the household needs.

2. **Underwrite against the pessimistic case, not the central one.** A 24.2-year payback in unretrofitted stock and a 6.4-year one in retrofitted stock aren't close calls — but £880 versus £10,252 in EPC-C stock is a genuinely wide spread depending on real-world battery degradation. Price the deal so it still works at the bottom of that range, not just the middle.

3. **A DNO's local flexibility value is a separate revenue line, not a bonus on top of arbitrage.** National arbitrage dispatch and a DNO's own constrained-feeder timing aren't guaranteed to coincide — a DNO co-funding structure needs its own metered local-flexibility mechanism (a Piclo Flex-style tender), priced and contracted separately, not assumed to be baked into the arbitrage number above.

4. **This is still a two-point comparison, not a full dispatch model.** The headroom-scaled revenue treats degradation as a cliff edge rather than a gradual curve, and the dispatch-component-unscaled assumption is a named simplification, not a verified one. Treat these numbers as a serious first pass worth underwriting against, not a finished actuarial model.

## Scope, briefly

This is arithmetic built on real, cited UK revenue and cost data — Habo Energy's VPP/arbitrage market summary, Axle Energy's published dispatch rate, and this project's own already-grounded battery-utilisation physics — not a field-tested dispatch simulation. Single archetype (pre-1919 solid-wall terrace), English Housing Survey assumptions throughout. If your stock or funding routes differ materially, the mechanism almost certainly holds — fabric state determines spare capacity, spare capacity determines revenue — but the specific numbers need re-deriving against your own data before they go in front of a credit committee.

## If this is useful

If you're already structuring or considering deals like this — battery capex funded by an aggregator or installer in exchange for dispatch rights, into social housing specifically — I'd like to compare this arithmetic against real numbers. Particularly interested in hearing from anyone with actual dispatch logs by fabric/EPC band, or real degradation data on batteries running this kind of daily-arbitrage duty cycle for more than a few years. That's exactly the data that would narrow the £880–£10,252 range into something closer to a single, trustworthy number.

Full model, every notebook, every citation: link in the comments.
