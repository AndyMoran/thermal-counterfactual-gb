<!--
Posting notes (PROJECT.md Section 11):
- Best window: Thursday, 10am-5pm UK (post 2 of 3 in a deliberately spaced
  series: negawatt piece led Tuesday, this DNO piece runs today, BESS-
  vendors piece closes the series the following Tuesday).
- Attach figures/street_exposure_stress_test.png -- this draft's climax is
  the 22/30 vs 27/30 coincident-spike finding, so that figure now carries
  more weight than the coastdown chart. figures/coastdown_by_envelope_state.png
  (the 2R2C sensitivity range) is the secondary option if you'd rather lead
  visually with the coasting-hours claim in paragraph 1 instead.
- Put the link to the full write-up / repo in the FIRST COMMENT, not the post
  body (LinkedIn suppresses reach on posts with outbound links).
- Tone: practitioner-to-practitioner, written for a DNO/flexibility reader.
  Lead with the number, not the process.
- Companion to linkedin_article.md -- both lead with what this is worth to
  a grid operator, not the model-correction story (that lives in
  FINDINGS.md / PROJECT.md for anyone who wants it).
- Rewritten from the author's own draft after a fact-check against
  FINDINGS.md / linkedin_article.md. Three fixes applied:
  1. "64.6 MW coincident spike" was a 1000x unit error -- the sourced
     figure (FINDINGS.md, linkedin_article.md) is 64.6 kW. A single street
     of 30 homes drawing 64.6 MW between them isn't physically plausible
     for domestic electric heating.
  2. The 22-of-30 reheat count was paired with the wrong street
     description ("low-insulation street"). Per source, 22/30 is the
     *diversified* street (64.6 kW); 27/30 is the street concentrated in
     the lowest-insulation tenure segment, ex-Right-to-Buy privately
     rented (79.2 kW). Both figures are now given together, correctly
     attributed, which also strengthens the paragraph.
  3. The title, "The 1.8 MW that's sitting on your network right now,"
     stated the full-retrofit potential (100% uptake) as if it already
     exists today. linkedin_article.md draws this distinction explicitly:
     at today's 27% uptake, what's actually on the ground is roughly
     486 kW per 1,000 homes, not 1.8 MW. Retitled to keep the "per 1,000
     homes retrofitted" rate framing the body text already uses correctly.
- Added a closing line at the author's request: "The asset with the
  biggest grid value has no revenue model. The one with a revenue model
  has a fifth of the adoption." Checked against source: the "fifth"
  figure matches linkedin_article.md's own "roughly a fifth of fabric's
  27%" for BESS/solar adoption (~5.8%, back-derived from MCS/EHS data --
  see FINDINGS.md Finding 6, PROJECT.md's 4.6x adoption-gap figure is the
  same ratio inverted). "Biggest grid value" is the one part of this line
  that's a rhetorical synthesis rather than a directly modelled £/kW
  comparison -- fabric's 1.8 MW/1,000 homes is real and large, but this
  project never quantifies fabric's avoided-reinforcement value against
  battery's dispatch/arbitrage value on the same £/kW basis to make
  "biggest" a strictly modelled claim. Consistent with the project's own
  established "inversion" framing (FINDINGS.md: "the asset with no
  working revenue mechanism today has been deployed far more than the
  asset that has one"), so left in as written.
-->

1.8 MW per 1,000 homes retrofitted — real, permanent, and completely undispatchable.

I modelled a real, mixed-tenure UK terrace estate — English Housing Survey data, a December 2022 cold snap, and a 2R2C thermal model — to answer one question for grid operators:

When a pre‑1919 solid‑wall terrace gets insulated to EPC‑C, how much genuine demand flexibility does that create?

The headline: 1.8 MW per 1,000 homes retrofitted. A permanent peak‑demand reduction at the coldest hour. Not a one‑off — a structural change to the load shape.

The coastdown number that matters: EPC‑C fabric holds 19°C for 11.4–14.3 hours with heating off. Unretrofitted fabric? 1.6–3.9 hours. It doesn't clear a 4‑hour evening peak. Don't bank on it.

The catch — and it's a big one: only 27% of a real estate has this fabric today. Right‑to‑Buy fragmentation means a third of the stock is outside a social landlord's reach entirely. Street‑level variance runs 0–37% — your most exposed feeder could look nothing like the estate average.

And the capacity that does exist? It shrinks fastest when the weather gets worst. At −9.4°C (8°C colder than Dec '22), 22 of 30 homes on a diversified street reheat simultaneously — a 64.6 kW coincident spike. On a street concentrated in the lowest-insulation tenure segment, it's 27 of 30 — 79.2 kW.

Worst of all: you can't buy this flexibility today. Passive fabric has no meter, no dispatch signal, no tender bid. It's real, measurable, structural — and invisible to your procurement system.

The asset with the biggest grid value has no revenue model. The one with a revenue model has a fifth of the adoption.

So here's the question I'm sitting with:

If fabric retrofit delivers 1.8 MW/1,000 homes of permanent peak reduction, and it's already 27% delivered on the ground... why isn't that on your constraint map?

The full model, and notebooks, are available to stress‑test if you want to run this against your own feeder data. Link in first comment.
