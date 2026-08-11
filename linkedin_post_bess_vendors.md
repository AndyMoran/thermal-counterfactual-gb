<!--
Posting notes (PROJECT.md Section 11):
- Companion post to linkedin_article_bess_vendors.md. Same rules as the
  original post: link in the FIRST COMMENT, not the body; attach
  figures/battery_utilisation_by_envelope_state.png directly.
- Written for BESS/VPP vendors and installers, and HA asset managers buying
  from them -- distinct audience from linkedin_post.md (DNO/grid operator).
- England-grounded; see the article's Scope section before reusing any
  number here for a different UK nation's housing stock.
- Updated to match the article's new title/deck ("bill-savings product" vs
  "flexibility asset") and its hedged VPP/bill-saving revenue split -- keep
  the "plausibly" and "not yet modelled state-by-state" language if this
  post is edited further; notebooks/05 applies the GBP 1,075/year figure as
  a flat constant across all three fabric states, so the split is reasoned,
  not a modelled result. See linkedin_article_bess_vendors.md's own posting
  notes for the full explanation.
-->

Your battery's real ceiling isn't its power rating — it's the walls around it. In leaky social housing, that same battery is a bill-savings product. In insulated stock, it's a flexibility asset the grid will actually pay for.

On a real pre-1919 solid-wall terrace archetype: an unretrofitted home asks a standard 10 kWh battery for 98% of its usable capacity just to hold one evening peak. A fully insulated (EPC-C) home asks for 26%. Same battery, same install — the difference is what's left over to actually dispatch, arbitrage, or survive a colder-than-usual night without the tenant overriding the system.

The revenue is real too — roughly £1,075/year in VPP dispatch plus arbitrage, against a ~£13,500 bundled install. But plausibly (not yet tested state-by-state) it isn't evenly real: the bill-saving half likely survives in leaky stock — the battery still charges cheap and discharges into the evening load — but the VPP half likely doesn't, since dispatch needs headroom a comfort-holding battery doesn't have.

Full write-up, the physics, and the numbers — in the comments.
