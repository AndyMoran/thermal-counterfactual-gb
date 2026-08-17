<!--
Posting notes (PROJECT.md Section 11):
- Third companion piece to linkedin_article.md (DNO/grid-operator) and
  linkedin_article_bess_vendors.md (BESS/VPP vendors). This one is written
  for a general UK energy-policy audience -- DESNZ/MHCLG officials, CCC-
  adjacent researchers, think tanks, and retrofit-programme designers --
  not a specific commercial buyer.
- Reuses Finding 1 (peak demand), Finding 2 (27% prevalence), Finding 3
  (street-level variance), Finding 5 (retrofit cost, category-error
  economics), Finding 6 (delivery-model asymmetry, battery headroom), and
  Finding 7 (annual displaced energy/bill/carbon) directly. Finding 8 is
  the one genuinely new piece of analysis this article introduces --
  lifetime economics over a sourced 36-year fabric life -- and it now has
  a documented, executed, hand-checked home in notebooks/06 Section 8,
  configs/tenure_insulation_assumptions.yml (annual_impact.lifetime_
  economics), citations.md, PROJECT.md Section 8.6/8.9, and FINDINGS.md,
  exactly like every other headline number in this project.
- CHANGE LOG vs the author's first draft (both fixes applied, not just
  flagged, per the author's explicit request):
  1. The "40-year fabric life" was an unsourced round number. Replaced
     throughout with the sourced 36-year Ofgem ECO/Green Deal "Appropriate
     Guarantees" convention for solid wall insulation (citations.md).
  2. The lifetime cost-per-tonne figure was GROSS (capital cost only) even
     though the same draft separately established a 5.4-year bill-saving
     payback -- internally inconsistent, since a measure that pays for
     itself in 5.4 years cannot honestly be priced as if the other ~31
     years of savings didn't happen. Replaced with the properly NETTED
     figure (capital cost minus lifetime bill savings, divided by lifetime
     carbon abated) as the headline, with the gross figure kept alongside
     for readers who want the unnetted number. The net figure is negative
     -- "no-regrets" abatement, not merely cheap abatement -- which is a
     STRONGER and better-supported claim than the original draft's.
  3. "Britain's cheapest decarbonisation" (title) was an unqualified
     superlative with no cross-technology comparator cited. Retitled around
     the now-well-supported "pays for itself" / negative-cost claim instead
     of a "cheapest" claim this project can't fully back.
  4. "Unlike a battery, nothing to degrade, replace, or recycle" directly
     contradicted the fabric-life assumption used two paragraphs later.
     Replaced with an accurate, still-favourable comparison (fabric's
     36-year working life vs a battery's roughly decade-scale replacement
     cycle).
  5. "Private rented stock is the lowest-insulation segment" overstated
     what this project modelled -- only this stock's ex-Right-to-Buy
     privately rented segment (10%), not the national PRS generally.
     Scoped accordingly.
  6. Added one clause noting Finding 3's own caveat that the 17-37%
     street-variance range is likely an undercount of real-world spatial
     clustering -- strengthens the "guarantees patchwork outcomes" point
     rather than weakening it.
  7. Added one clause in Scope flagging the lifetime economics as simple,
     undiscounted arithmetic, not a discounted-cash-flow appraisal --
     matching the equivalent caveat now in README.md's Limitations section.
-->

# The negawatt has no salesforce — decarbonisation that pays for itself is real, measured, and undelivered

*We can now measure it: ~7.6 GWh of displaced energy, ~£2m of bills, and ~1,000 tonnes of CO2e per 1,000 homes a year. What we don't have is anyone whose job it is to sell it.*

The negawatt — the unit of energy you never have to generate, transmit, or pay for — is the oldest idea in energy policy and still the most under-delivered. I've spent recent months building a physics-based digital twin of a real, mixed-tenure English terrace estate to find out whether the negawatt is real, what it's worth, and why so little of it exists. The short version: it's real, it pays for itself, it's durable — and it has no salesforce.

## The negawatt, measured

A pre-1919 solid-wall terrace retrofitted to EPC-C displaces 7,600 kWh of heating energy a year — worth about £1,984/yr at the current price cap, and about 1.0 tCO2e/yr on the official average-grid basis, or 2.7–3.0 t on a marginal, CCGT-proxy basis. Which basis is "correct" for an abatement claim is a genuinely contested question, so this project reports both rather than picking a convenient one. At the coldest hour of a design winter the same retrofit removes 1.8 kW of peak demand per home — 1.8 MW per 1,000 homes, permanently, for as long as the fabric holds.

Per 1,000 homes that is 7.6 GWh/yr, ≈£2m/yr, ≈1,000 tCO2e/yr on the average basis. No new generation, no new network, no land use, no new supply chain — and unlike a battery's roughly decade-scale replacement cycle, fabric's working life is measured in decades, not years.

## It pays for itself — the barrier is capital, not economics

The retrofit costs £10,728/home and repays in about 5.4 years through bill savings alone. Compare the 84 years it would take flexibility-market revenue to repay it — a market that, as currently structured, cannot buy what fabric delivers at all, because passive retrofit has no meter, no dispatch signal, and no verifiable baseline. What fails is the front end: the households who would benefit most can't front the capital, and the landlords who could don't capture the benefit.

Over the fabric's own working life — 36 years, the Ofgem ECO/Green Deal standard measure life for solid wall insulation — that arithmetic goes further than "cheap." Even before counting a penny of bill savings, the gross cost is about £299/tonne on the average-grid basis, or £98–112/tonne on the marginal-proxy basis: already a modest figure by the standards of UK abatement measures generally. But that isn't the right number, because it ignores the bill savings the same spend also buys. Net those off — the standard treatment in a marginal abatement cost curve, where fuel-cost savings are an offsetting benefit, not an afterthought — and the true cost is negative: roughly –£1,694/tonne on the average basis, –£555 to –£635/tonne on the marginal basis. Negative means what it says: over its working life this measure saves money and abates carbon at the same time. It belongs in the "no-regrets" category of decarbonisation, not merely the affordable one. The economics are not the bottleneck. Delivery is.

## It multiplies everything else we have to build

Every negawatt shrinks the heat pump, the battery, and the network upgrade that electrification otherwise requires. In the same model, a battery in an unretrofitted home spends 98% of its capacity just holding comfort through one evening peak; in a retrofitted one, 26%. Insulation is not a competitor to electrification or storage. It is the multiplier that makes them affordable at system scale.

## But the negawatt has no salesforce

Megawatts have vendors, lenders, and procurement routes. Negawatts have to be delivered by capital that only flows where someone controls the asset. On a real mixed-tenure estate, 27% of homes have the retrofit today; the other 73% don't, and the missing share concentrates exactly where decades of Right to Buy sales have put it furthest out of reach of any landlord programme. A social landlord can't retrofit a street it no longer owns. A private landlord can't capture a tenant's bill savings. An owner-occupier in fuel poverty can't front £10,728.

The delivery-model evidence is already in the data: fabric retrofit, delivered as landlord-funded programmes, has reached this stock at roughly 4.6× the rate of battery-plus-solar, which has been an individual purchase. Area-based, funded programmes out-deliver market-led uptake — and current programme routes stop at the social-landlord boundary.

## What would a negawatt delivery policy actually do?

1. **Make delivery tenure-blind.** Area-based schemes must be able to treat every home on a street regardless of ownership — the fragmented ex-Right-to-Buy share included — because the street-level variance (17–37% insulated on streets drawn from the same tenure mix, and real spatial clustering, where whole streets were sold under Right to Buy together, likely makes the true range wider still) otherwise guarantees patchwork outcomes.

2. **Close the split incentive where capital exists but can't capture benefit.** Within this stock, the ex-Right-to-Buy privately rented segment is the lowest-insulation tier (10% insulated, against 34–37% for retained council/housing-association stock): the landlord pays, the tenant saves. Minimum standards or shared-cost mechanisms have to bridge that, or the capital stays on the sideline.

3. **Give the negawatt a buyer on the network side.** The 1.8 MW per 1,000 homes is real avoided reinforcement cost — but no route exists to pay for it. A reinforcement-avoidance funding mechanism, or a metering-and-verification layer that makes fabric-driven reduction contractible, would turn the negawatt from a free good into a procurable resource.

If you're designing Warm Homes delivery routes, PRS minimum standards, or reinforcement-avoidance mechanisms, I'd like to compare notes.

## Scope, honestly

Single archetype — a mid-terrace, the physically favourable solid-wall form; other forms coast faster and cost more to treat. Carbon is basis-dependent and reported as such. The negawatt buys bounded headroom, not a substitute for generation or network build. The lifetime economics are simple, undiscounted arithmetic over a sourced 36-year fabric life — not a discounted-cash-flow appraisal, and they don't account for future energy-price movements, grid decarbonisation, or real-world degradation of insulation performance. None of that changes the central finding: decarbonisation that pays for itself is sitting undelivered — not because it isn't real, but because nobody's revenue depends on selling it.

Full model, every notebook, every citation: link in the comments.
