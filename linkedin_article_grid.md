<!--
Posting notes (PROJECT.md Section 11):
- Companion long-form piece to linkedin_post.md. Publish as a LinkedIn Article,
  link it from the post's first comment.
- Attach both figures inline at the points marked below.
- Rewritten for a grid-operator reader (DNO network planning and flexibility
  procurement, kept general across both). The earlier version narrated the
  model-correction process; that process is now documented in FINDINGS.md /
  PROJECT.md instead. This version leads with what the numbers mean for
  someone planning or procuring around this stock, and closes with an
  explicit invitation to stress-test it against real data.
-->

# The hidden battery in Britain's social housing: what a grid operator can actually count on

If you plan network capacity or procure flexibility, here's the question this piece answers: when a pre-1919 solid-wall terrace gets insulated to EPC-C, how much genuine demand flexibility does that create, how confident can you be in it during a real cold snap, and can you actually buy it today?

I built a physics-based digital twin of a real, mixed-tenure UK terrace estate to get an answer with the assumptions visible rather than asserted — envelope physics checked two ways, English Housing Survey tenure and insulation data, a real December 2022 cold-snap event, and a street-level tenure-exposure stress test for when fabric quality and coldest weather coincide. It's been through a round of external technical review; every number below, and the full derivation, is in the linked notebooks. This piece is about what came out the other end and what you can do with it, not about how it got built. (Social landlords control the single largest share of this stock, but not the whole of it — the estate modelled here is about 35% ex-Right-to-Buy, sold into private ownership; the findings below are about that full mixed-tenure picture, not social housing alone.)

## The number that matters: 1.8 MW per 1,000 homes, if the fabric is right

A fully retrofitted (EPC-C) home cuts steady-state heat-pump electrical demand from 2.46 kW to 0.66 kW at a −3°C design outdoor temperature (COP 2.5 assumed throughout) — a 1.80 kW/home reduction, or **1.8 MW of avoided peak demand per 1,000 homes** retrofitted. That figure is stable: it depends only on heat-loss coefficient and heat-pump efficiency, not on any of the modelling refinements below. It also isn't a one-off saving from a single cold snap — it's a permanent reduction in the peak load the grid has to supply at the coldest hour of a design winter, for as long as the fabric stays retrofitted. And it's the potential: what a full retrofit programme unlocks, not what exists on the ground today — the next section gets to that gap.

Coasting time is the sharper question — how long a home holds a 19°C comfort floor with heating off, from a 22°C start (the preheat ceiling a VPP would target before curtailing — not the 21°C normal living setpoint referenced later for occupant behaviour), through the 16:00–20:00 evening peak. Checked properly, with a two-node (air/mass) thermal model rather than a single lumped mass: **EPC-C fabric coasts 11.4–14.3 hours and clears a 4-hour peak window every time.** Unretrofitted fabric coasts only **1.6–3.9 hours and never reliably clears it.** Wall-insulation-only sits in between at 2.0–4.4 hours, clearing only at the most generous end of that range.

**[Insert chart: coastdown_by_envelope_state.png]**

The operational read: don't rely on unretrofitted or partially-treated stock to coast through a peak window. The margin that holds up is EPC-C's, and only EPC-C's. (Scope note: this archetype is a mid-terrace, the most favourable solid-wall form physically — semis, detached homes, and bungalows in a real portfolio will show smaller margins than the ranges above.)

## Today, 27% of a real estate has it — and who controls it matters as much as how much there is

Weighting a real English Housing Survey tenure mix — council-retained, housing-association-retained, and the growing ex-Right-to-Buy share now privately rented or owner-occupied — **27% of this estate is solid-wall insulated today.** A single retrofitted home avoids a median 1.87 kW of peak demand (1.53–2.30 kW, P10–P90, propagating uncertainty in heat pump COP, thermal mass, and geometry) — that figure is per retrofitted home, not an estate-wide average. On a 1,000-home estate at today's 27% uptake, that's roughly **486 kW of avoided demand actually sitting on the ground now**, not the 1.8 MW potential above. An estate-wide planning number is the per-home figure times your uptake share — and the street-level variance below applies to that product too, not just to the uptake share on its own.

That capability figure also isn't the same as delivered flexibility. Every coastdown number here assumes a "charged battery" — a normal 21°C living temperature before any curtailment begins. Fuel poverty and prepayment self-rationing concentrate in exactly the lowest-insulation tenure segments modelled, so real occupancy is plausibly anti-correlated with fabric quality — the homes least likely to be insulated are also plausibly least likely to be heated to 21°C at all. Not modelled here, no occupant-behaviour data went into this; if true, usable capacity today is lower than both figures above, not higher.

Two more things worth building into any estate-wide planning number:

**Right to Buy fragmentation shrinks who you can actually reach.** Roughly a third of this stock has been sold out of council or housing-association ownership. A retrofit programme routed through a social landlord structurally cannot touch that share directly, whatever the estate-wide average implies.

**A single street can look nothing like the estate average.** A specific 30-home street, drawn from the same tenure mix, ranges from 17% to 37% insulated across the middle 80% of outcomes, with a real chance of landing at 0%. Real tenure is also spatially clustered — whole streets were sold under Right to Buy together, not scattered randomly — so this range is likely an *undercount* of real street-to-street variance, not an overcount.

## The capacity you can count on shrinks exactly when you need it most

Running the real December 2022 cold snap progressively colder finds the point where unretrofitted fabric starts failing to hold its comfort floor during the peak window at all: **8°C colder than the event actually delivered** (a peak-window outdoor minimum of −9.4°C). At that point, **22 of 30 homes on a diversified street are forced to resume heating simultaneously — a coincident spike of about 64.6 kW.** On a street concentrated in the lowest-insulation tenure segment (ex-Right-to-Buy privately rented), it's **27 of 30, about 79.2 kW.**

**[Insert chart: street_exposure_stress_test.png]**

Worth being precise about direction here: this dynamic stress test runs the simpler single-node thermal model, which coasts longer than the more careful two-node model above — so if anything, it *understates* how early real exposure starts, not the reverse. What it does not show, and shouldn't be assumed, is that these low-insulation streets sit on your most constrained feeders. That's a plausible, checkable hypothesis against your own network data, not something this model has established. It's also worth noting a coincident reheating spike isn't the end of the story: curtailed demand that ends in resumed heating is displaced into the recovery period, not deleted, which matters if cold snaps run several days.

## What you can actually buy today is smaller than the headline number implies

The 1.8 MW/1,000-homes figure is real demand reduction. It is **not** a metered, dispatchable, verifiable resource you can procure through a standard flexibility tender — passive fabric has no meter, no controllable asset, and no dispatch signal, so it structurally cannot bid into a service like Piclo Flex as currently structured. Pricing it against an illustrative flexibility-service rate (~£127/home/year) is a category error, not a revenue estimate — worth knowing before that number lands in a business case.

The two channels where fabric retrofit's value to a grid operator is real — avoided network reinforcement capex, and direct bill savings — aren't quantified in this model. That's deliberately where the actual financial case lives, and where I'd want real network and billing data to go next.

For comparison: a battery+solar+VPP fit-out on the same archetype *is* genuinely contractible today, on a bundled installed cost of ~£13,500. Its ~£1,075/home/year is two stackable revenue streams on the same battery, not one blended figure — ~£120–300/year in VPP dispatch payments plus ~£800–950/year in time-of-use arbitrage — for a ~12.6-year payback. I'm breaking that out deliberately: bundling distinct revenue channels into a single number is exactly the category error the fabric economics above just corrected, and I'd rather not repeat it here even though both channels here are genuinely real and contractible.

Adoption on this same stock is much lower than fabric's, on a back-derived, order-of-magnitude estimate (~5.8%, built from MCS installer tenure shares and EHS population counts, not a directly published per-tenure rate) — roughly a fifth of fabric's 27%. One plausible read: the asset with a working revenue mechanism has so far been an individual owner-occupier purchase, not a landlord-funded programme, while fabric retrofit has been the reverse. That's a read, not a proven causal claim — adoption differences reflect who buys and what's fundable, not only which asset has a revenue mechanism. Fabric and battery answer different questions regardless; one ROI number across both would be its own category error.

## Scope, briefly

Single archetype, external wall insulation assumed (internal wall insulation would likely strand more thermal mass and isn't modelled separately), and a calibrated synthetic weather profile rather than raw station data. None of that changes the direction of the findings, but it bounds how far to extrapolate this specific set of numbers.

## If this is live for you

I'd like to stress-test this against a real feeder or estate — your tenure mix, your network topology, your cold-snap event. If you're in DNO network planning or flexibility procurement and either of these is a live question for you — the reinforcement-avoidance number, or what a metering layer would need to look like to make fabric-driven flexibility actually procurable — I'd like to talk.

Full model, every notebook, every citation: link in the comments.
