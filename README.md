# thermal-counterfactual-gb

**Thermal Envelope as a Passive Grid Asset** — a physics-based counterfactual showing how much "hidden battery" a fabric retrofit creates for a VPP during a UK winter cold snap, and who actually controls whether that capacity ever gets unlocked.

## Core Thesis

Fabric retrofit turns leaky social housing into flexible grid capacity — but only for the shrinking share of an estate the landlord actually controls, and nobody currently prices that gap.

## Setup (WSL)

```bash
# from inside WSL, ideally under your Linux home directory (see note below)
bash setup.sh
uv run jupyter lab
```

**Performance note:** keep this project under your Linux home directory (e.g. `~/projects/thermal-counterfactual-gb`), not under `/mnt/c/...`. Jupyter, Polars, and Parquet I/O are markedly slower across the Windows/Linux filesystem boundary. `setup.sh` will warn you if you run it from `/mnt/...`.

When opening a notebook, select the **`thermal-counterfactual-gb`** kernel explicitly — cross-project kernel usage is prohibited (see `PROJECT.md` Section 4.1).

## Project structure

```
thermal-counterfactual-gb/
├── PROJECT.md                          # full research constitution + project spec — read this first
├── README.md                           # this file
├── LICENSE                             # MIT (code only — see LICENSE for the third-party-data scope note)
├── citations.md                        # full source list with links and evidentiary status
├── pyproject.toml                      # uv-managed deps: polars, numpy, scipy, matplotlib, streamlit
├── setup.sh                            # WSL bootstrap
├── configs/
│   └── tenure_insulation_assumptions.yml   # every material assumption, tagged by evidentiary status
├── notebooks/
│   ├── 01_archetype_physics.ipynb          # geometry, envelope states, H/C/tau (Week 1)
│   ├── 02_cold_snap_simulation.ipynb       # hour-by-hour coastdown, baseline vs retrofit (Week 2)
│   ├── 03_estate_population_model.ipynb    # tenure-weighted headline, Monte Carlo, stress test (Week 2-3)
│   ├── 04_vpp_economics.ipynb              # physics-to-£, DNO avoidance, battery equivalence (Week 3)
│   ├── 05_bess_vpp_solar_comparator.ipynb  # BESS+solar+VPP comparator: fabric-only vs BESS-only vs stacked (Week 5)
│   └── 06_annual_impact_and_carbon.ipynb   # whole-year displaced energy, bill savings, carbon (avg+marginal), summer dynamics (Week 6)
├── data/
│   ├── raw/                            # source data (weather, EHS extracts) — not committed
│   └── intermediate/                   # parquet handoff between notebooks — not committed
├── figures/                            # Tufte-compliant output charts — not committed
├── src/thermal_counterfactual_gb/
│   └── physics.py                      # shared RC-model functions, imported by notebooks
└── demo/
    └── app.py                          # Week 4 Streamlit interactive demo
```

## Traceability Table

Every headline number below should be reproducible by hand from `configs/tenure_insulation_assumptions.yml` in under 60 seconds (Traceability Mandate, `PROJECT.md` Section 6). This table is filled in as each notebook produces validated output — do not add a row until the number has been hand-checked.

| Headline number | Value | Key inputs | Computed in |
|---|---|---|---|
| Baseline coastdown at −3°C (1R1C, **upper bound** — see 2R2C row) | 5.0 h | wall 1.7, window 3.1, roof 2.3, floor 1.5 W/m²K; 1.0 ACH; C=10 kWh/K; 400W internal gains netted off | `notebooks/01` |
| EPC-C coastdown at −3°C (1R1C, upper bound) | 18.7 h | wall 0.30, window 1.6, roof 0.16, floor 0.25 W/m²K; 0.8 ACH; 400W internal gains netted off | `notebooks/01` |
| 2R2C sensitivity range: baseline / SWI-only / EPC-C coastdown | 1.6–3.9 h (never clears 4h) / 2.0–4.4 h (clears only at f_air=0.20) / 11.4–14.3 h | BS EN ISO 6946 internal surface resistances; air-capacitance fraction swept 2–20%; 400W internal gains | `notebooks/01` §7 |
| Peak reduction, baseline→EPC-C (steady-state, unaffected by 1R1C-vs-2R2C or by internal gains — gains cancel in the difference) | 1.8 MW per 1,000 homes | 2.46 kW − 0.66 kW per home, COP 2.5, both net of the same 400W gain | `notebooks/01`, `04` |
| Estate weighted insulation prevalence (today) | 27% | LA 24%×34%, HA 41%×37%, ex-RTB rented 15%×10%, ex-RTB owner 20%×11% | `notebooks/03` |
| Peak kW avoided per home, baseline→EPC-C (MC P10/P50/P90) | 1.53 / 1.87 / 2.30 kW | COP∼U(2,3), C∼U(7,13) kWh/K, floor area∼U(60,85) m² (internal gains cancel out of this difference, so this range is unchanged by the gains revision) | `notebooks/03` |
| EPC-C coastdown hours, design temp (MC P10/P50/P90) | 13.1 / 17.9 / 23.5 h | same MC draws, with 400W internal gains netted off (this range DOES shift with gains, since it's not a difference between states) | `notebooks/03` |
| Anti-correlation stress test breach point | event 8°C colder than recorded (outdoor min −9.4°C in peak window; recorded event's own peak-window range was ≈ −1.4°C to +2.0°C) | baseline fabric, 1R1C coastdown vs Dec 2022 calibrated hourly profile, gains netted off (22/30 and 27/30 street exposure counts are population-composition arithmetic, unaffected by internal gains; coincident-spike kW figures are ~64.6/~79.2 kW) | `notebooks/03` |
| Retrofit cost, pre-1919 age-band average | £10,728/home | EHS 2024-25 Annex Table 2.14 | `notebooks/04` |
| Illustrative flexibility value **if contractible** (it is not, today — see Limitations) | £127/home/year | 1.87 kW × £68/kW/yr (PROVISIONAL, Piclo Flex tender summary) | `notebooks/04` |
| Simple payback at that illustrative value | ~84 years | £10,728 retrofit ÷ £127/year | `notebooks/04` |
| Battery-hardware-equivalent value, **delivered** (headline) | £1,447/home | 2.2 kWh_e actually drawn down in the real event (net of internal gains) × £650/kWh | `notebooks/04` |
| Battery-hardware-equivalent value, nominal ceiling (context only, unaffected by internal gains) | £7,800/home | 12 kWh_e theoretical × £650/kWh installed | `notebooks/04` |
| Battery power rating never limits peak coverage, any fabric state | 3.6–11.5 kW (point 5.0 kW) vs 0.66–2.46 kW peak demand | Tesla Powerwall 3 / GivEnergy datasheets vs `resolved_physics` | `notebooks/05` |
| Battery energy needed for full 4h peak coverage (the real constraint) | 9.84 kWh baseline (98% of a 10kWh battery) / 2.64 kWh EPC-C (26%) | peak kW × 4h peak window | `notebooks/05` |
| Bundled BESS+solar install cost / real annual VPP+arbitrage revenue / payback | £13,500/home / £1,075/home/yr / 12.6 years | 2026 UK market surveys; Axle/Kraken/Tesla VPP (all GROUNDED, currently contractible; unaffected by internal gains, which is a fabric-physics input only) | `notebooks/05` |
| Estate-weighted BESS/solar adoption today, vs fabric's 27% | 5.8% (4.6× lower than fabric) | MCS tenure-share data back-derived by tenure (PROVISIONAL) | `notebooks/05` |
| Annual space-heating electricity, baseline / SWI-only / EPC-C (per home) | 9,671 / 7,966 / 2,071 kWh/yr | 12 monthly mean outdoor temps (Manchester, PROVISIONAL) run through the same `net_heating_power_kw` used everywhere else, COP 2.5, 400W gains netted off each month — not an external HDD figure (would double-count against the gains already in the model) | `notebooks/06` |
| Annual displaced energy / bill saving / carbon abated, baseline→EPC-C (per home) | 7,600 kWh/yr / ≈£1,984/yr / ≈996 kg CO2e/yr (avg) or 2,660–3,040 kg CO2e/yr (marginal proxy) | electricity 26.11 p/kWh (Ofgem Q3 2026 price cap, GROUNDED); grid carbon 0.131 kg/kWh average (DESNZ 2026, GROUNDED) and 0.35–0.40 kg/kWh marginal (CCGT-typical PROXY, PROVISIONAL, explicitly not an official LRMEF series) | `notebooks/06` |
| Estate-scale annual potential vs today's 27% uptake, per 1,000 homes | 7,600 MWh/yr / £1,984,272/yr / 996 tCO2e/yr (avg) potential vs 2,054 MWh/yr / £536,349/yr / 269 tCO2e/yr (avg) today | same per-home baseline→EPC-C figures scaled to full retrofit vs the actual 27% weighted prevalence | `notebooks/06` |
| Summer dynamics (solar export/voltage risk; overheating risk) | Not quantified — flagged qualitatively only (OMITTED_QUALITATIVE) | ENA/NGED G98-G99 statutory voltage band 216–253V (mechanism, GROUNDED, not modelled here); CIBSE TM59 2026 + 2025 Buildings-journal literature on EWI-vs-IWI summer comfort (GROUNDED literature, not simulated) | `notebooks/06` |
| Fabric measure life | 36 years | Ofgem ECO/Green Deal "Appropriate Guarantees" solid-wall-insulation convention (GROUNDED) | `notebooks/06` §8 |
| Simple bill-saving payback, baseline→EPC-C | 5.4 years | £10,728 retrofit cost ÷ £1,984.27/yr bill saving (exact pipeline value) | `notebooks/06` §8 |
| Lifetime marginal abatement cost, GROSS (capex only) | ≈£299/tCO2e average / £98–112/tCO2e marginal | £10,728 ÷ (36 yr × annual carbon abated, avg or marginal-proxy basis) | `notebooks/06` §8 |
| Lifetime marginal abatement cost, NET (capex minus lifetime bill savings — the standard MACC treatment) | ≈–£1,694/tCO2e average / –£555 to –£635/tCO2e marginal | (£10,728 − (£1,984.27/yr × 36 yr)) ÷ (36 yr × annual carbon abated); negative = cash-positive over the fabric's life, not a sign error | `notebooks/06` §8 |

## No-Double-Counting

Physical mechanisms are modelled once, in their proper place — never bundled with something else because it's convenient:

- **Infiltration / reveal leakage** lives in the ACH ventilation term, not folded into the window conduction U-value. (An earlier proposal to inflate the window U-value for "seal degradation + reveal bridging" was rejected for exactly this reason — see `PROJECT.md` Section 8.3.)
- **Population composition** (which tenure/insulation bucket a dwelling falls into) is a deterministic weighted average, not a Monte Carlo population simulation — resampling a categorical mix whose shares are already known only manufactures fake uncertainty from sampling noise. Monte Carlo is reserved for genuinely uncertain parameters (COP, thermal capacity, geometry) and for small-N street-level realism (a real LV feeder serves ~100-300 homes; a 30-home sample here is called a street, not a feeder).
- **Comfort-floor behaviour** is modelled directly inside the coastdown simulation, never as an external derating multiplier applied on top of a simulation that already accounts for it.

## Limitations & Future Work

This project is **not**:
- A claim that any specific real estate has been measured or surveyed — it's a physics-based digital twin calibrated against national statistics (EHS, DESNZ), not measured smart-meter data.
- A whole-house annual energy or carbon model — `notebooks/06` extends coverage to whole-year space-heating electricity, bill savings, and carbon abatement (both average-grid and marginal-proxy bases, reported side by side rather than a single headline — the choice between them is a genuinely unresolved methodological question, not a modelling detail), but domestic hot water and occupant behaviour remain explicitly **omitted**, not modelled as zero. Summer dynamics (solar export/voltage risk, overheating risk) are now qualitatively flagged with literature grounding (`notebooks/06`, Sledgehammer Test per `PROJECT.md` §2.2) rather than silently omitted, but are still not quantified — no solar-export volumes, no voltage simulation, no overheating hours modelled. `notebooks/06` §8 also extends the annual view to a lifetime one (36-year sourced fabric life), reporting both a gross and a bill-savings-netted marginal abatement cost — but this is simple, undiscounted arithmetic, not a discounted cash-flow or NPV appraisal, and doesn't account for real-world degradation of insulation performance, energy price changes, or grid decarbonisation over that 36-year window.
- A market-ready VPP dispatch or revenue-stacking product, and specifically **not evidence that passive fabric retrofit can be sold into a flexibility-service tender today** — those tenders require metered, dispatchable, verifiable demand reduction, which passive fabric alone cannot provide (external review, `PROJECT.md` §8.9). The £/kW/year figure in `notebooks/04` is labelled "if contractible," not a revenue estimate.
- An argument that fabric retrofit alone solves a DNO's substation constraint — Right to Buy fragmentation means a meaningful share of any real estate (modelled at ~35% ex-Right-to-Buy) sits outside a housing association or council's direct control entirely — nor a claim that these low-insulation streets spatially coincide with a DNO's actual constrained feeders, which this project has not checked against real network data.
- A precision instrument — the primary thermal model is a simple single-node (1R1C) model. A 2R2C structural sensitivity added after external review (`notebooks/01` §7) confirms this overstates baseline and SWI-only coastdown substantially (1R1C says 5.0h/6.0h including internal gains; a more realistic 2-node model says 1.6-4.4h) — those figures are documented as upper bounds throughout, not point estimates. EPC-C's margin is robust to this same check, and to the internal-gains revision (§ below) — if anything, gains make it more robust, since a fixed 400W gain is proportionally larger against EPC-C's small heat loss than against baseline's large one.
- A claim that internal gains are modelled with any time structure — `internal_gains_w` (400W point estimate, PROVISIONAL) is a flat constant, identical across all three fabric states and all hours, not a diurnal occupancy/cooking schedule. This likely understates real gains during the 16:00-20:00 peak window specifically (when cooking and occupancy are typically highest) and overstates them overnight — a simplification in both directions, not a conservative one in either. Solar gains through windows are still not modelled at all (distinct from the internal/casual gains that now are).
- An argument that fabric retrofit and a BESS+solar+VPP fit-out are substitutes with one comparable ROI — `notebooks/05` treats them as complements answering different questions (fabric: comfort/health/EPC compliance, no real flexibility revenue today; BESS/VPP: real, currently-contractible revenue, but no comfort or fabric benefit). Collapsing them into a single number would repeat the same category error the DNO-economics correction above already fixed once. BESS/solar's own tenure-adoption figures (`notebooks/05`) are PROVISIONAL, back-derived from share-of-owners data rather than a directly published per-tenure rate.

See `PROJECT.md` Section 8.9 for the current list of open questions, and Section 8.6 for the full assumptions ledger (GROUNDED / PROVISIONAL / DELIBERATE / FORWARD-LOOKING / OMITTED).

## Governing framework

The full research philosophy, six-stage analytical pipeline, and engineering standards live in [`PROJECT.md`](./PROJECT.md). Read it before adding a notebook cell or a number.

The full, checkable source list — every citation used anywhere in this project, with links and evidentiary status — lives in [`citations.md`](./citations.md).

## License

The code in this repository (notebooks, `src/thermal_counterfactual_gb/`, configs, analysis scripts) is MIT licensed — see [`LICENSE`](./LICENSE). Third-party data cited in `citations.md` (EHS, DESNZ, Ofgem, Met Office, and others) remains subject to its own original publishers' terms; this license does not extend to it.
