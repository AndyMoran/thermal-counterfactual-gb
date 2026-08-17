<!--
Posting notes (PROJECT.md Section 11):
- Standalone piece, not a numbered companion to the fabric/battery series --
  broader audience, different register: a process/epistemics piece rather
  than a findings piece, though it grew directly out of sourcing the battery-
  life figure for the VPP-funded-battery ladder (ADDENDUM.md, 17 Aug 2026).
- Names Kight PowerHub directly, by explicit decision -- their own specific,
  checkable claims (25yr warranty, 20,000 cycles, NGA chemistry, insurer
  approval) were independently verified as real and accurately reported, not
  fabricated. Naming them here is fair precisely because the piece is
  illustrating good-faith verification, not a takedown -- the one claim that
  didn't hold up (a hybrid open-API/VPP-programme description) is
  attributed carefully to a third-party summary Andy found, NOT stated or
  implied to be something Kight themselves claimed. That distinction must be
  preserved in any future edit of this piece -- collapsing it would be unfair
  to a real, named company whose own public claims checked out.
- The specific unverifiable citations (rocketreach.co returning empty,
  tsa-voice.org.uk containing zero mentions of Kight) are described exactly
  as found on 17 Aug 2026 -- re-check before republishing if this piece is
  reused later, since both could change.
- UPDATED 17 Aug 2026: added a "One update, since I first checked this"
  postscript after direct correspondence with Kight confirmed third-party
  VPP/API access is real (see ADDENDUM.md's "Third-party VPP API access"
  section for the full PROVISIONAL/single-source evidence tier). Kept
  deliberately anonymised in the public text ("I later asked Kight
  directly") rather than naming the personal/family channel -- doesn't
  change the piece's core distinction between a citation problem and a
  company problem, and if anything sharpens it: the claim was substantively
  true, the citations that first carried it still weren't good enough to
  establish that.
- Sodium-ion/Chinese battery-manufacturing context (CATL TENER Sodium, BYD's
  sub-GBP0.04/Wh target) is used here only to establish why claim-verification
  volume is about to increase, not as a technical deep-dive -- that's a
  different piece if one gets written.
-->

# I fact-checked a battery claim. The citations were the problem, not the company.

*A live example from a project built on "check it, don't wave it through" — including the one time, this month, that discipline caught something I'd have otherwise repeated as fact.*

Every number in this project's own findings has been through the same test: state it, cite it, grade it — grounded, provisional, or flag it as omitted. That discipline is usually applied to the model's own numbers. This month it got applied to a vendor claim instead, and it's worth walking through exactly what happened, because the failure mode it caught is about to get a lot more common.

## The claim that checked out

Kight PowerHub is a new (2026) Scottish-manufactured domestic battery, developed over five years with Scottish housing associations, now heading into real-world trials before full production. Their public claims are specific: a 25-year warranty, a 20,000-cycle life, a chemistry with no graphite and no cobalt that they say eliminates fire risk and clears full insurance cover, including for social housing.

I checked these against the actual source pages rather than taking a summary's word for it. They held up. The 25-year warranty and 20,000-cycle figure are stated plainly on Kight's own site and in trade coverage. The "no graphite, no cobalt" chemistry description is real and specific enough to be a genuine technical claim, not marketing filler — specific enough, in fact, to plausibly point at a sodium-ion or sodium-ion-adjacent chemistry, though Kight doesn't use that term themselves and I haven't confirmed it.

That's the useful case: a claim that's specific, sourced, and checks out — worth taking seriously, while still remembering that a warranty on a brand-new product is a forward promise, not a demonstrated fifteen-year track record. Those are two different things, and both were true here at once.

## The claim that didn't

Separately, I was handed a detailed technical summary describing Kight's system as a "hybrid" architecture — a proprietary control layer for day-to-day optimisation, but with open API access letting third-party aggregators run their own Virtual Power Plant dispatch on top of it, plus a claim that Kight runs its own VPP and flexibility programmes directly. It was specific, well-organised, and cited: a company-directory page, an industry association's website, a couple of LinkedIn references.

I checked each citation directly rather than trusting the summary. The industry-association site had zero pages mentioning Kight, at all. The company-directory citation returned an empty page — and on inspection, that particular site is a contact-lookup tool, not the kind of source that would ever contain technical architecture details in the first place. Independent searching for Kight's actual API or third-party integration capability turned up nothing to confirm any of it.

To be precise about what this does and doesn't show: nothing here suggests Kight made these claims themselves. The summary I was checking wasn't Kight's own material — it read like a research write-up assembled from public sources, and on inspection its central claims simply weren't supported by the sources attached to them. That's a distinct problem from a company overselling its own product, and worth being exact about which one actually happened here.

## Why this is going to matter more, not less

Chinese battery manufacturers are moving fast enough that claim-volume is about to spike. CATL unveiled its TENER Sodium storage platform in June, with first deliveries in September. BYD is targeting a manufacturing cost around $0.04/Wh on its own sodium platform by 2027, backed by a dedicated 50GWh factory. New chemistries, new warranty numbers, new cycle-life claims, new market entrants — all arriving faster than any one person can independently verify by hand.

That's exactly the environment where a fluent, well-cited, entirely wrong summary is most dangerous — not because it's obviously false, but because it's specific enough to sound checked when it hasn't been. A vague marketing superlative ("longest lifespan on the market") is easy to discount. A confident architecture description with named citations is much easier to repeat as fact, precisely because it looks like someone already did the work.

## The skin-in-the-game asymmetry, restated

A 25-year warranty is a costly promise — if Kight is wrong about their own battery, they're the ones paying to service or replace units that fail early. That's real exposure, and it's why a specific number like "20,000 cycles" is worth taking more seriously than an adjective. But an unverified claim repeated from a summary has no equivalent cost to whoever repeats it. Nobody pays anything if "Kight has an open VPP API" turns out to be untrue — except the reader who acted on it. That asymmetry is the whole reason checking the primary source matters more than checking how confident or well-formatted the summary sounds.

## One update, since I first checked this

I later asked Kight directly, rather than relying on another summary: is third-party VPP or aggregator dispatch actually possible, or is EnergiFlow the only controller allowed to run the battery? Their answer: EnergiFlow currently brokers to a third-party VPP rather than running dispatch entirely in-house, and the API can be opened to other third parties on request.

So the substance of the claim I couldn't verify turns out to be roughly right — third-party access is real. That doesn't rehabilitate the citations that first carried it. A contact-directory page and an industry-association site with zero mentions of Kight never supported that claim, however true it happens to be. A claim can be true and badly sourced at the same time — which is exactly why checking the citation and checking the claim are two different acts, and why getting the second one right, this time, took a direct question rather than another search.

Worth keeping attached: this was an informal exchange, not a commercial statement from Kight — a real data point, not something to cite as their formal published position.

## What actually checking took

Not much, in the end: open the cited page. If it's empty, or plainly the wrong kind of source for the claim attached to it, that's the answer. Search independently for the specific claim rather than the general topic. Notice when a citation's domain doesn't match what it's supposedly proving — a contact-directory site citing a technical architecture claim was the tell here, before I'd even opened the page.

None of that requires special access or deep expertise. It requires treating "it's cited" as the start of a two-minute check, not the end of one.

Full model, every notebook, every citation: link in the comments.
