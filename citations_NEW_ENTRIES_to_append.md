<!--
RECOVERY FILE, 17 Aug 2026 -- see chat for context. citations.md went missing
from the sandbox along with ADDENDUM.md and the ladder article; the other two
were fully reconstructed from what was already written this session, but the
original citations.md (~226 lines, predating this session's Rung 2 work) was
never held in full in context, so it can't be safely reconstructed here.

Your GitHub copy of citations.md predates all of this session's Rung 2 work
and should be intact. Append everything below it, immediately before its
existing "## How to use this file" closing section, exactly where these
entries were originally inserted.
-->

**UK domestic battery arbitrage revenue scaling with capacity, 2026 UK installer/aggregator market guides** (Spectrum Energy Systems, Premier Electrical Renewables, and equivalent 2026 battery-storage buyer's guides).
Used for: `check_headroom_revenue_scaling.py` — the claim that a 5kWh battery cycled daily delivers roughly half the absolute arbitrage savings of a 10kWh system, i.e. arbitrage revenue scales roughly linearly with usable capacity rather than being flat regardless of battery size. Also used: confirmation that the dominant arbitrage strategy is overnight-cheap-charge / evening-peak-discharge, the same 16:00–20:00-adjacent window this project's comfort-holding draw competes for.
Status: **PROVISIONAL** — installer/aggregator-marketing-adjacent sourcing, same evidentiary tier as this project's other installer-survey-derived figures (battery and ASHP size-banded costs above). The roughly-linear scaling claim is consistent with the underlying physics (a roughly constant £/kWh price spread, one dominant daily cycle — corroborated separately by Predbat/solar-optimisation documentation on daily cycling patterns), not merely asserted by a single source, but no official/regulatory data source for this scaling relationship was found.

**VPP dispatch payment structure and rates, UK 2026**: Habo Energy market summary (as already cited above for the £120–300/£800–950 split) plus Axle Energy's published dispatch rate.
Used for: `check_headroom_revenue_scaling.py` — the structural distinction this check relies on between the two revenue components: availability/dispatch payments (paid for short, discrete grid-service events, e.g. Axle Energy's ~£1/kWh dispatch rate for frequency-response events on Fox ESS/GivEnergy/Solax batteries) versus time-of-use arbitrage (paid for a predictable daily cheap-charge/expensive-discharge cycle). This project treats only the arbitrage component as scaling with fabric-state spare capacity, leaving the dispatch component unscaled — see the script's own docstring for why, including the flagged-not-modelled caveat that real frequency-response events plausibly cluster during winter system-stress periods, correlating with exactly when comfort-holding draw is also highest.
Status: **GROUNDED** for the two-component payment structure and the Axle Energy rate itself (a named, specific commercial rate, not a market-average estimate). **PROVISIONAL/REASONED** for this project's own decision to leave the dispatch component unscaled by fabric state — a simplification flagged in the script, not a sourced finding about how dispatch events actually distribute across fabric states or seasons.

**Beltran, H.; Ayuso, P.; Pérez, E. (2020). "Lifetime Expectancy of Li-Ion Batteries used for Residential Solar Storage."** Energies, 13(3), 568. DOI: 10.3390/en13030568.
[ResearchGate](https://www.researchgate.net/publication/338814859_Lifetime_Expectancy_of_Li-Ion_Batteries_used_for_Residential_Solar_Storage)
Used for: `check_headroom_revenue_scaling.py` — the 7.44–18.37-year battery-life range (to a 60% remaining-capacity threshold), replacing an earlier unsourced 15-year guess for the Rung-3 lifetime-margin sensitivity check.
Status: **GROUNDED** — peer-reviewed (Energies, MDPI), semi-empirical ageing models validated against real PV production and consumption profiles across multiple locations. The wide range reflects genuine climate/usage-profile variation in the underlying study, not this project's own imprecision.

**UK domestic battery warranty and cycle-life norms, 2026**: Aurora Solar (installer-education blog, same evidentiary tier as this project's other installer-guide citations); Solar Insure (US solar/storage warranty provider).
Used for: `check_headroom_revenue_scaling.py` — the industry-standard 10–15-year LFP warranty convention (70–80% capacity retention guaranteed, "generally expected to last 15 years or more" in practice); and the 6,000–10,000-cycle premium-LFP figure, cross-checked against this project's own ~1.5-cycles/day arbitrage rate to give ~11.0–18.3 years to a 70–80% threshold — corroborating, in order of magnitude, the Beltran et al. range above despite a different capacity-retention threshold.
Status: **PROVISIONAL** — installer/warranty-provider tier, same standard already applied to this project's other market-guide citations.

**Kight PowerHub, 25-year warranty / 20,000-cycle claim, 2026**: Best Magazine ("Kight PowerHub launches AI home battery"); kightpowerhub.co.uk.
Used for: `check_headroom_revenue_scaling.py` — named explicitly as a real, specific vendor claim (not used as this check's base case). A genuinely new Scottish-manufactured domestic battery on a chemistry described as "not utilised in production domestic batteries before," with a market-leading 25-year warranty and 20,000-cycle life.
Status: **NAMED, NOT GROUNDED for use as a base-case figure** — the specific numbers are real and verifiably reported (not fabricated or misquoted), but this is a single vendor's own forward warranty commitment on a product with no long-run field track record yet (first UK domestic installations only recently reported), well above every other source in this list. Using it as an anchor would repeat this project's own previously-corrected mistake of accepting a vendor superlative at face value.

**Kight Off-Grid (lighting division), 20-year cell-life claim**: kightoffgrid.com.
Used for: `check_headroom_revenue_scaling.py` — explicitly EXCLUDED as a category mismatch. This is a different product (off-grid solar/wind LED lighting for streets, construction, highways, rail) on a different duty cycle (one shallow nightly discharge) from a home battery doing ~1.5 deep arbitrage cycles a day. Named here only to record why it was considered and rejected, not as a citation this project relies on.
Status: **REJECTED — category mismatch**, same discipline already applied elsewhere in this project (e.g. not using the blended national £6,335 retrofit figure for this specific archetype, Finding 5).

**Local Network (DNO) Flexibility, Axle Energy explainer**, Karl Bach, updated 2026.
[Axle Energy blog](https://www.axle.energy/blog/local-flex)
Used for: `check_headroom_revenue_scaling.py` §5 (Rung 4, DNO co-funding) — the ~20% of GB households within an active constraint zone; the ~£33/kW/year average revenue across all 6 DNOs (2023–24); the four DNO flex product types (Sustain, Secure, Dynamic, Restore) and confirmation that Sustain, the most common, is a seasonal scheduled commitment for a defined time of day rather than a rare event; the 10–50kW minimum bid size per local competition, which rules out a single home's battery participating unaggregated.
Status: **GROUNDED** — a specialist flexibility-market platform's own explainer of a regulated (RIIO-2/Ofgem-mandated) procurement mechanism, with a named, dated average revenue figure, not an estimate. Ceiling prices are explicitly flagged by the source itself as varying up to 100x by DNO/product/competition, carried through into this project's own treatment as an average, not a promised rate.

**Demand Flexibility Service (DFS) and batteries, Habo Energy**, updated April 2026.
[Habo Energy](https://haboenergy.co.uk/demand-flexibility-service-home-battery)
Used for: `check_headroom_revenue_scaling.py` §5 — confirmation that DFS is a NATIONAL NESO/system-balancing product, distinct from DNO local-constraint flex, and therefore already covered (if at all) under Rung 2's dispatch component rather than something to add again under Rung 4. Not used for any DNO-specific figure.
Status: **GROUNDED** for the national/local distinction and DFS's own mechanics; used here only to avoid double-counting, not as a source for any number in this project's own figures.

**DESNZ Greenhouse Gas Reporting: Conversion Factors 2026**, published 11 June 2026, updated 31 July 2026 (unrelated flat-file correction).
[gov.uk publication](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2026) · [Circular Ecology summary](https://circularecology.com/news/desnz-2026-uk-ghg-conversion-factors)
Used for: `check_headroom_revenue_scaling.py` §6 — re-verifying Finding 7's 0.131 kgCO2e/kWh average-grid figure. GROUNDED that the 2026 release cut the UK electricity factor by ~26% via a revised, reduced-lag methodology (Circular Ecology, dated 18 June 2026). The specific resulting figure is corroborated by three independent secondary mentions (~131–141 gCO2e/kWh) but contradicted by one other aggregator (ecohedge.com, 0.207 kg/kWh) — the primary DESNZ spreadsheet (XLSX/PDF) could not be read as text to resolve this directly.
Status: **GROUNDED** for the fact and scale of the 2026 methodology change. **UNRESOLVED** for the exact resulting average-grid figure — majority evidence supports Finding 7's existing 0.131 figure, but this project cannot claim full primary-source verification. Flag for a follow-up check against the actual spreadsheet if this figure needs to be defended precisely (e.g. in a board paper).
