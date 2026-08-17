<!--
Posting notes (PROJECT.md Section 11):
- Fifth companion article in the business-case thread, following on from
  linkedin_article_business_case.md and its ADDENDUM.md. That article closed
  with the combined-CapEx hypothesis check; this one picks up a question a
  reader asked after it went out: if fabric frees up spare battery capacity,
  could a VPP operator's own commercial interest in that capacity actually
  help pay for it? Written for the same three-audience frame as the original
  business-case piece (CEO/portfolio leader, facilities/asset manager, HA
  leadership) but as a single unified piece rather than three sections, since
  the "ladder" structure is itself the point, not something to fragment by
  reader.
- Built entirely from ADDENDUM.md's "VPP-funded-battery ladder: Rung 2" section
  and src/check_headroom_revenue_scaling.py -- every figure here traces to
  that script's output, hand-verified.
- Deliberately keeps the wide, honest profitability range (GBP880-GBP10,252)
  rather than collapsing it to a single "it works" number -- that range IS
  the finding, and softening it would repeat the exact mistake this project
  keeps catching itself almost making. Same treatment for the "default
  outcome" section added 17 Aug 2026 -- GBP18,362 is an order-of-magnitude
  negotiating figure, not a number to quote as precise.
- Does not name specific vendors (Kight, CATL, BYD) -- that's the subject of
  a separate, differently-framed piece (linkedin_article_verifying_battery_claims.md).
  This article stays at the level of the financing mechanism, not any one
  company's claims about it.
-->

# The battery doesn't need to be the landlord's problem

*Fabric retrofit pays for itself without a battery anywhere near it. But once it's done, a battery bigger than the landlord actually needs starts to look like someone else's investment — if the deal is structured right.*

Every number in the retrofit business case stands on its own, no battery required: 5.4-year payback, £60,706 net lifetime saving per home, cash-positive decarbonisation. If a battery never enters the conversation, none of that changes. What follows is about a separate question, asked after that case was already made: once fabric frees up spare battery capacity, is there a way to get someone other than the landlord to pay for it?

## The size a landlord needs isn't the size a VPP wants

A retrofitted, EPC-C home needs only 26% of a standard 10kWh battery's capacity to cover the evening peak, against 98% for an unretrofitted one. Sized purely for comfort, that argues for a smaller, cheaper battery — roughly 41% less than the full-size unit, based on real UK product tiers.

But that's optimising for one customer. The other 74% of that battery, sitting idle every evening in an insulated home, is exactly the spare capacity a Virtual Power Plant operator can dispatch for arbitrage and grid-service revenue. A landlord sizing for comfort alone throws that value away. A VPP funding the *bigger* battery, in exchange for the right to dispatch the spare capacity, doesn't.

That's the shape of the idea: right-size for comfort is the landlord's optimisation; right-size for revenue is a different party's, and there's no reason both have to be paid for by the same person.

## The number that was too convenient to trust

The obvious next question is whether the VPP side of that deal actually pays for itself — and the answer depends entirely on getting the revenue number right, which turned out to need more care than it first looked like.

This project's own existing VPP-and-arbitrage revenue figure — roughly £1,075 a year — had always been applied as a flat number, the same regardless of how much spare capacity a battery actually has. That was fine for the question it originally answered. It's the wrong number for this one.

Splitting it properly: about £210 a year comes from short, discrete dispatch events, and about £875 a year from daily time-of-use arbitrage — charge cheap overnight, discharge into the expensive evening peak. That arbitrage window is the *same* 4pm–8pm window a retrofitted home's comfort-holding draw already competes for, so it should scale with how much spare capacity a fabric state actually leaves free — not stay flat.

Done properly: an unretrofitted home's battery earns roughly **£228 a year** for a VPP; a wall-insulation-only home, **£368**; a fully retrofitted EPC-C home, **£858**. The flat figure this project used before overstated the leaky-home case by nearly 5x, and was roughly right — slightly conservative, if anything — for the retrofitted one.

## What that means for a VPP funding the battery itself

Re-running the numbers with the honest, headroom-scaled figure: a VPP funding a full 10kWh battery (£5,500) in an EPC-C home, in exchange for dispatch rights, pays back in **6.4 years**. In a wall-insulation-only home, **15 years** — marginal. In an unretrofitted home, **24.2 years** — no commercial case at all.

That last number is worth sitting with. It's not an assumption that fabric has to come first — it's the quantified reason a VPP has no reason to fund a battery ahead of it. The financing idea only works downstream of a retrofit that was already worth doing on its own terms.

## The honest range, not the comfortable one

Here's where this gets more cautious than it first appeared. A VPP's profit over the battery's working life depends on how long that battery actually lasts — and the real, peer-reviewed literature on Li-ion residential storage life gives a genuinely wide range: 7.44 to 18.37 years, depending on climate and usage profile, to a 60%-capacity threshold (Beltran, Ayuso & Pérez, *Energies*, 2020).

At the pessimistic end of that range, the margin a VPP earns after paying back its £5,500 is only **£880** — barely profitable, not the comfortable case a single central estimate implies. At the optimistic end, **£10,252**. The honest statement is that this is solidly worthwhile at the central-to-optimistic end of a real range, and only marginally worthwhile at the pessimistic end — which is a materially more careful conclusion than picking one number and reporting it as *the* answer.

## Skin in the game does some of the work a landlord shouldn't have to

There's a genuinely useful side effect of structuring the deal this way. If a landlord funds the battery, the landlord is also the one exposed if the vendor's performance claims don't hold up over fifteen years. If a VPP funds it in exchange for dispatch rights, that exposure moves with the money — the VPP only profits if the battery performs close to what was promised, so their willingness to actually put capital behind a specific product is a far better signal of real confidence than a warranty document on its own. A landlord doesn't have to independently verify every vendor's cycle-life claim if the party financing the deal already has to get that right to make any money at all.

That's not a guarantee — a VPP with genuine capital at risk can still be honestly wrong about a number, same as anyone else. But it's a real, useful filter, and it's one a landlord gets for free simply by structuring who pays for what correctly.

## The default outcome, if nobody asks

There's a version of this that requires no negotiation at all, and it isn't in the landlord's favour. A battery installer that also runs its own VPP or aggregator arm doesn't need to offer anyone a revenue-share to capture the spare-capacity value — they can sell the battery purely on comfort, EPC compliance, and asset-protection grounds, all genuinely sufficient reasons to buy on their own, and then quietly enrol the same battery in their own flexibility programme afterwards. Nothing about that sale ever has to disclose what the ongoing dispatch and arbitrage revenue is worth, because the purchase was never contingent on it.

That's not a hypothetical edge case — it's the default outcome unless someone on the buying side raises the question. And it's a genuinely worse outcome than either alternative in this piece: paying full price for the battery *and* getting none of its flexibility value is strictly worse than a VPP funding the battery outright (where the landlord pays nothing at all for the same zero-revenue outcome), and it's worse again than simply negotiating to keep that revenue in the first place.

Put a number on it: in EPC-C stock, over a central 15-year battery life, not asking costs a landlord up to **£12,862** in forgone lifetime flexibility revenue, on top of the **£5,500** they'd have avoided paying entirely under the VPP-funded structure above. Combined, the gap between the uninformed default and the best available structure is roughly **£18,362** per battery — undiscounted, and dependent on the same wide battery-life range flagged throughout this piece, but a real order of magnitude to negotiate against, not a rounding error.

The practical takeaway is simple: treat who keeps the flexibility-market revenue as an explicit term of any battery procurement, not an afterthought. If an installer's pitch is built entirely on comfort and compliance — which, to be clear, is a completely legitimate basis for the purchase on its own — that's exactly the moment to ask what happens to the dispatch revenue afterwards, because the pitch working on its own merits is precisely why nobody is obliged to volunteer the answer.

## What's still open

The DNO side of this is a distinct, unmodelled question. A DNO benefits from a battery discharging to relieve a local network constraint, which doesn't necessarily happen on the same schedule a VPP's national arbitrage strategy would choose — so a DNO's contribution needs its own revenue mechanism (a local flexibility tender, not a share of arbitrage income), and nothing here has costed that out yet.

The lifetime-margin figures above also assume a battery earns the same revenue right up until a cliff-edge end of life. Real degradation is gradual — arbitrage revenue should taper as capacity fades, not hold flat and then stop. That refinement hasn't been done either.

None of this changes the underlying carbon and bill-saving case for the retrofit itself, which needs no battery to justify it. What it changes is a genuine, second-order question: who should pay for going beyond comfort-sizing, and how, and who ends up keeping the value if nobody thinks to ask. The honest answer, on the numbers so far, is: plausibly a VPP, plausibly worth structuring — but only if the deal is priced against a real range of outcomes, and negotiated explicitly, rather than left to a default that quietly favours whoever installed the hardware.

Full model, every notebook, every citation: link in the comments.
