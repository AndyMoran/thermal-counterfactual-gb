<!--
Posting notes (PROJECT.md Section 11):
- Companion post to linkedin_article_bess_vendors.md. Same rules as the
  original post: link in the FIRST COMMENT, not the body; attach
  figures/battery_utilisation_by_envelope_state.png directly.
- Written for BESS/VPP vendors and installers, and HA asset managers buying
  from them -- distinct audience from linkedin_post.md (DNO/grid operator).
- England-grounded; see the article's Scope section before reusing any
  number here for a different UK nation's housing stock.
- UPDATED 17 Aug 2026: the "probably" / "likely" hedge on the VPP/bill-saving
  split has been resolved. src/check_headroom_revenue_scaling.py (Rung 2 of
  the VPP-funded-battery ladder, Insulation Biz Case/ADDENDUM.md) actually
  modelled the split instead of reasoning about it: ~GBP 210/yr dispatch
  (roughly flat by fabric state) + ~GBP 875/yr arbitrage (scales with
  spare capacity). Headroom-scaled annual revenue: baseline ~GBP 228,
  wall-insulation-only ~GBP 368, EPC-C ~GBP 858 -- replacing the flat
  GBP 1,075/yr figure used when this post was first drafted. Paybacks
  against the same GBP 13,500 bundled install recomputed and hand-verified
  17 Aug 2026 (13500/228=59.2, 13500/368=36.7, 13500/858=15.7 years).
  Still PROVISIONAL/REASONED for the arbitrage-scales-with-headroom
  mechanism itself (installer-market-guide tier, not a dispatch-log
  result) -- see ADDENDUM.md for the full evidence tier.
- Best window: Tuesday, 10am-5pm UK. Post 3 of 3 in a deliberately spaced
  series: negawatt piece led the preceding Tuesday, DNO piece followed
  that Thursday, this piece closes the series today -- each spaced out
  rather than consecutive, so none compete with the last for the same
  followers' attention.
- Title changed by Andy, 17 Aug 2026, from the original hook-first opening
  line to an explicit headline: "In Social Housing, the Battery Isn't the
  Flex Asset -- the Fabric Is." Stronger hook; the one thing worth watching
  if this gets pushback is the shorthand -- fabric doesn't trade on a
  flexibility market itself, it's what frees the headroom a battery needs
  to. The body text still makes that mechanism explicit, so the title reads
  as a fair, punchy compression rather than a separate claim.
-->

In Social Housing, the Battery Isn't the Flex Asset — the Fabric Is

In leaky social housing, that same battery is a bill-savings product. In insulated stock, it's a flexibility asset the grid will actually pay for.

Here's what that looks like on a real pre-1919 solid-wall terrace:

- Unretrofitted home: a standard 10 kWh battery uses 98% of its usable capacity just to hold one evening peak.
- EPC-C insulated home: the same battery uses 26%.

Same battery, same install. The difference is what's left over to dispatch, arbitrage, or survive a colder-than-usual night without the tenant overriding the system.

When I first posted this, the £1,075/year VPP-plus-arbitrage revenue figure was flat — the same number regardless of fabric state — and I flagged the split below as a hunch, not a result. I went back and modelled it.

Split properly: ~£210/year comes from short dispatch events, roughly flat by fabric state. ~£875/year comes from time-of-use arbitrage, which needs headroom to sell. Scaled by how much spare capacity each fabric state actually leaves free: an unretrofitted battery earns ~£228/year, wall-insulation-only ~£368/year, EPC-C ~£858/year.

Against the same ~£13,500 bundled install, that's not one ~12.6-year payback anymore. It's ~59 years unretrofitted, ~37 years with wall insulation only, ~16 years at EPC-C.

Same hardware. Same install cost. A ~3.8x payback spread, purely from how much headroom the walls leave.

So the question isn't hypothetical anymore: are we underwriting VPP revenue against batteries that structurally can't deliver it?

Full physics, notebooks, and the estate-level breakdown in the first comment.
