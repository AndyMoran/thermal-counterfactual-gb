# PROJECT.md: thermal-counterfactual-gb

**Status:** Scoping complete — pre-Week 1
**Purpose:** Define the research logic, modelling discipline, programming standards, and communication guardrails for the Thermal Envelope as a Passive Grid Asset project, under the universal engineering constitution below.
**Core Philosophy:** *Physical reality and auditable math always trump software illusions. We do not build analytical black boxes. We build transparent, reproducible, and physically grounded frameworks.*

---

# Part 1 — Project Definition & Scoping

## 1. The Project Definition Template

Every project must begin by explicitly defining its scope, avoiding the trap of solving every problem at once.

1. **The Core Thesis:** A single, punchy sentence defining the gap between theory and physical reality.
2. **The Empirical Deliverability Question:** Do not ask if a concept exists in theory. Ask if the physical assets can *actually deliver* the required service when real-world constraints, consumer behaviour, and hardware limits are applied.
3. **The Boundary of the Model:** Explicitly state what the model *does not* do.

---

# Part 2 — Research Philosophy

## 2. The Golden Heuristics

Non-negotiable rules for all modelling, simulation, and analytical work.

### 2.1 Physics Before Economics
Physical feasibility and system need must be established before economic conclusions are drawn. Do not jump directly to NPV, revenue sufficiency, or market design before establishing the physical and technological logic.
*Always begin with: What is constrained? Where? Which direction is power flowing? Can the asset physically perform the action?*

### 2.2 The 'Sledgehammer' Test (Simple Before Complex)
Use the simplest credible method that answers the question. Before implementing advanced algorithms, ask: *"Can a simple, auditable, rule-based or multiplicative model answer the core question?"* If yes, the simple model must be used. Complexity is only justified if it solves a specific, documented gap that the simple model cannot address.

### 2.3 The Physics/Derating Separation (No Double-Counting)
Internal physical constraints must be modeled directly within the core simulation ($P_{simulated}$). Post-hoc derating multipliers ($\eta$) are strictly reserved for external network, operational, or behavioral frictions.

### 2.4 The Anti-Correlation Stress Test
Any flexibility, reliability, or risk model must include a "worst-case correlation" scenario. If a model only tests average conditions, it is over-promising and will fail in the real world.

### 2.5 Time Flows Forwards (Zero Look-Ahead Bias)
No variable, feature, or model input may use information unavailable at the decision timestamp. Strict temporal train/test splits are mandatory.

### 2.6 Mechanism Before Model
Every model result must be attached to a physical or economic mechanism. Use the project loop: *Model result → discomfort → mechanism → sensitivity → policy lever → caveat*.

### 2.7 Ambiguity Is Informative
Treat uncertainty as a signal that understanding is incomplete. Do not force interpretations before sufficient evidence exists.

---

# Part 3 — Analytical Design

## 3. The Universal 6-Stage Pipeline

### Stage A: Empirical Ground Truth
Build the empirical event log or raw data foundation. Preserve empirical correlation between variables. Do not use synthetic data before building the empirical register.

### Stage B: Temporal & Distributional Analysis
Characterise the data by time, season, duration, and severity.

### Stage C: Physical / Synthetic Asset Modelling
Model the physical assets. Do not treat different seasonal services as equivalent. Explicitly model hardware/fabric differences where relevant to the physical outcome.

### Stage D: Dispatch & Scenario Modelling
Run multiple scenarios on the same synthetic fleet/population so differences are attributable to dispatch/policy rules rather than portfolio composition.
1. **Baseline/Naive**
2. **Theoretical Ceiling**
3. **The Realistic Hybrid (Central Case)**
4. **The Anti-Correlation Stress Test**

### Stage E: Value Gap & Derating Framework
$$P_{effective} = P_{simulated} \times (\eta_{thermal} \times \eta_{phase} \times \eta_{comms} \times \eta_{primacy})$$
*Never double-count internal physics here.*

### Stage F: Monte Carlo & Uncertainty Propagation
Simple vectorized Monte Carlo (e.g., NumPy) is the primary uncertainty framework. Always calculate and report **P10, P50, and P90**, not just point estimates.

## Analytical Principles: Feynman Approaches

1. *"You must not fool yourself — and you are the easiest person to fool."* Every assumption documented, every number traceable, invite adversarial review.
2. *"What I cannot create, I do not understand."* Build the physical model from first principles rather than citing a headline number.
3. *"Knowing the name of something is not the same as knowing something."* Decompose "flexibility" into its physical mechanisms.
4. *"Reality must take precedence over public relations."* The physics doesn't care about the pitch deck.
5. *"I would rather have questions that can't be answered than answers that can't be questioned."* State what remains unknown at every stage.
6. *"Explain it simply."* If it can't be explained to a planner or policymaker in one breath, it isn't understood well enough to model.
7. *"Shut up and calculate."* Run the numbers rather than hand-wave.
8. **Map vs. territory.** The model is a map. Never confuse it with reality.

---

# Part 4 — Engineering & Programming Discipline

## 4. The Modern Stack & Environment Rules
- **Environment Management:** `uv` strictly enforced.
- **Dataframes:** Polars strictly enforced over Pandas.
- **Math/Simulation:** NumPy (vectorized), SciPy (distributions).
- **Visualization:** Matplotlib (publication-ready).

### 4.1 Environment Locking & Isolation
Notebooks execute via the project-specific virtual environment. Cross-project kernel usage prohibited. First cell verifies the active Python executable path.

### 4.2 The Parquet Handoff Rule
Notebooks must not pass massive dataframes in memory across stages. Minimum 4 modular notebooks. Each saves output to `data/intermediate/*.parquet`; the next reads from it.

### 4.3 Polars Quirks & Gotchas
- No `.item()` needed — aggregations return native Python floats.
- `.with_columns()` evaluates in parallel — cannot reference an alias created in the same block.

## 5. NASA/JPL-Inspired Coding Standards
*Make wrong results hard to produce silently.*

1. **Small Functions, Clear Contracts.** No hidden global state.
2. **Assertions Protect Physics.** e.g. `assert 0 <= indoor_temp_frac <= 1`, `assert h_total_w_per_k > 0`.
3. **Fail Loudly.** No silent failures, no broad `except: pass`.
4. **Schema Before Analysis.** Explicit schema (column, type, unit, allowed range) for every intermediate dataset.
5. **Deterministic Baseline Before Randomness.** Run one transparent, deterministic example before Monte Carlo.
6. **Configuration, Not Magic Numbers.** Material assumptions live in named config, not buried in logic.
7. **Warnings Are Evidence.** Do not suppress globally.

---

# Part 5 — Communication, Traceability, & Reporting

## 6. The Traceability Mandate
Every headline metric must be reproducible via a documented, row-by-row traceability table. If a reviewer cannot reproduce your headline number in a spreadsheet in under 60 seconds, the model is a black box and is rejected.

## 7. Translate to Physical Units
Every headline percentage must be accompanied by its physical MW, kWh, or £ equivalent for the target scale.

## 8. Writing Principles: Strunk & White, Zinsser, and the Human Voice

### 8.1 Strunk & White
Omit needless words. Active voice. Positive form. Definite, specific, concrete language — "3.5%" not "approximately 3-4%". Do not overstate. Be clear.

### 8.2 Zinsser
Clarity is the foundation. Cut clutter. Write for the reader. Use active verbs. Be yourself. Simplify.

### 8.3 Modelling Prose — The Standard Pattern
Every major claim needs: **Number. Unit. Denominator. Mechanism. Scope boundary. Caveat.**

## 9. Visual Design Principles: Tufte's Standards
Maximize data-ink ratio. No chartjunk, no pie charts, no 3D, no decorative dashboards. Show the denominator. Direct-label, don't force legend eye-travel. Use small multiples for scenario comparison. y-axis starts at zero unless justified and marked. Show P10/P90 uncertainty when it affects the decision.

## 10. The README Standard
Every repository README.md includes: Core Thesis (one sentence), Traceability Table, explicit No-Double-Counting documentation, a "Limitations & Future Work" section, and at least one Tufte-compliant figure.

## 11. External Communication
Tuesday/Wednesday 8:00–9:30am UK. Link in first comment. One Tufte-compliant chart attached. Confident but humble tone, pre-empt expert critiques. Pivot to "lessons learned" framing if a technical post doesn't land.

---

# Part 6 — Forbidden Shortcuts & Known Risks

## 12. Forbidden Shortcuts
Do not: use synthetic data before the empirical register exists; double-count derating on top of physics already modeled; reach for MCMC/GANs/MILP when simple Monte Carlo or rule-based logic answers the question; treat non-equivalent seasonal/state services as equivalent; condition on post-event outcomes; hide material assumptions inside notebook cells; claim locational or tenure-specific value without an event-level or tenure-level counterfactual.

## 13. Known Risks & Mitigations
Generic risk categories: public data may not reveal the finest-grained constraint (mitigate by reporting each data granularity separately, never blended); behavioural/comfort constraints may dominate technical capacity (mitigate by modelling the comfort floor explicitly and running the Anti-Correlation Stress Test); synthetic population assumptions may overstate coordinated response (mitigate with explicit derating and P10/P50/P90 reporting).

---

# Part 7 — The Final Discipline

Do not let the model become clever before the mechanism becomes clear.

**Project order:** Physics → Event Register → Mechanism → Scenario Model → Sensitivity → Monte Carlo → Policy Lever → Caveat

**The Final Project Loop:** Model result → discomfort → mechanism → sensitivity → policy lever → caveat

---

# Part 8 — thermal-counterfactual-gb: Project Specification

## 8.1 Project Definition

**Core Thesis:** Fabric retrofit turns leaky social housing into flexible grid capacity — but only for the shrinking share of an estate the landlord actually controls, and nobody currently prices that gap.

**Empirical Deliverability Question:** Not "does thermal mass provide flexibility in theory," but: given the real, tenure-fragmented state of a pre-1919 terrace estate today — most of it still uninsulated, split across local authority, housing association, and ex-Right-to-Buy ownership with wildly different retrofit odds — how much coastdown capacity genuinely exists right now, and how much is achievable only if a specific, currently-underfunded segment gets treated?

**Boundary of the Model:**
- Covers the pre-1919 solid-wall mid-terrace archetype only. Does not cover flats, post-war cavity stock, or non-traditional/PRC construction.
- Covers space-heating coastdown and peak-demand reduction only. Does not cover domestic hot water, summer overheating, or full annual energy bills.
- Covers England-specific tenure and policy context (Right to Buy, Warm Homes Plan, RdSAP conventions). Not directly transferable to Scotland or Wales without re-grounding those inputs.
- Is a physics-based digital twin calibrated against national statistics (EHS, DESNZ), not measured performance of a specific real building or estate.
- Week 3 VPP/DNO economics are illustrative placeholders (electricity price, reinforcement cost, flexibility revenue) — this is not a merchant dispatch or market-mechanics model. Whether a payment mechanism exists for this specific flexibility product is a **forward-looking, unresolved** question, not an assumption.
- Week 5 extends the model to a BESS+solar+VPP comparator (`notebooks/05`) using the same archetype and event, not a new archetype or a new geography — and, unlike fabric's flexibility revenue, BESS/VPP's revenue mechanism is real and contractible today, not forward-looking. This does not change the fabric-only findings in Weeks 1-3; it adds a second, differently-shaped asset alongside them.
- Week 6 extends the model from a single cold-snap event to a whole-year view (`notebooks/06`): annual displaced space-heating energy, customer bill savings, and carbon abatement (both average-grid and marginal-proxy bases, deliberately reported side by side — see 8.9), computed via 12 monthly-mean-temperature runs through the same `net_heating_power_kw` function used everywhere else, not an externally-published degree-day figure at a fixed base temperature (which would reintroduce exactly the internal-gains inconsistency Section 8.3 already resolved once, since a fixed base temperature implicitly assumes uniform gains regardless of a state's own H). Summer dynamics (solar export/voltage risk, overheating risk) are addressed via the Sledgehammer Test (Section 2.2) — literature-grounded and qualitatively flagged, not simulated — since building either mechanism properly is out of this project's scope.

## 8.2 What This Project Is / Is Not

**This project is:** a synthetic-population physics model showing how much thermal storage a real, mixed-tenure pre-1919 terrace estate holds today, and how much more it could hold under current retrofit funding mechanisms — expressed in coastdown hours, MW of avoided peak demand, and £ of avoided DNO reinforcement.

**This project is not:**
- A claim that any specific real estate has been measured or surveyed.
- A whole-house annual energy or carbon model — `notebooks/06` (Week 6) adds whole-year space-heating electricity, bill savings, and carbon abatement (average-grid and marginal-proxy bases, reported side by side), but domestic hot water and occupant behaviour remain explicitly out of scope. Summer dynamics (solar export/voltage risk, overheating risk) are qualitatively flagged with literature grounding, not quantified or simulated.
- A market-ready VPP dispatch or revenue-stacking product.
- An argument that fabric retrofit alone solves a DNO's substation constraint — Right to Buy fragmentation means a meaningful share of any real estate sits outside the modelled intervention entirely.
- A bet that today's 1R1C single-node thermal model is a precision instrument — it is the deliberately simple version (Golden Heuristic 2.2), documented as likely to overstate coastdown time relative to a 2R2C air/fabric split model.

## 8.3 Archetype & Envelope States

Pre-1919 solid-wall mid-terrace, 2 storeys, 70 m² total floor area, 175 m³ heated volume, 40 m² exposed façade (front + rear only, party walls adiabatic), 10 m² window area.

| State | Wall U | Roof U | Floor U | Window U | Infiltration |
|---|---|---|---|---|---|
| A — Baseline | 1.7 W/m²K | 2.3 W/m²K | 1.5 W/m²K | **3.1 W/m²K** | 1.0 ACH |
| B — SWI only | 0.30 W/m²K | 2.3 W/m²K | 1.5 W/m²K | **3.1 W/m²K** | 1.0 ACH |
| C — EPC-C package | 0.30 W/m²K | 0.16 W/m²K | 0.25 W/m²K | 1.6 W/m²K | 0.8 ACH |

**Resolved H / τ / coastdown / peak demand (wall and window corrections applied, PLUS a 400W internal-gains netting — see below):**

| State | H (W/K) | τ (h) | Coastdown at −3°C (h) | Peak electrical demand @ COP 2.5 (kW) |
|---|---|---|---|---|
| A — Baseline | 273 | 36.6 | 5.0 | 2.46 |
| B — SWI only | 231 | 43.3 | 6.0 | 2.06 |
| C — EPC-C package | 86 | 116 | 18.7 | 0.66 |

Baseline→EPC-C peak reduction = 1.80 kW/home = **1.8 MW per 1,000 homes**, independently re-derived (not reverse-fitted to a prior estimate). This figure is UNCHANGED by the internal-gains revision below, and always will be, for a structural reason worth stating explicitly: gains are applied identically to every state, so they cancel out of any DIFFERENCE between two states' peak demand, even though they change each state's own absolute peak-kW and coastdown-hours figures. Pre-gains figures (4.7h / 5.5h / 15.0h coastdown, 2.62 / 2.22 / 0.82 kW peak) are kept in `configs/tenure_insulation_assumptions.yml`, `resolved_physics.pre_gains_reference`, for traceability.

**Internal gains — added after external review, RESOLVED.** The model previously treated the dwelling as an empty box: no allowance for the ~300-500W of constant heat a household's occupants, appliances, cooking and lighting generate (external review point, bottom-up cross-checked against ASHRAE occupant metabolic figures — 400W point estimate, PROVISIONAL, see `configs/tenure_insulation_assumptions.yml`, `internal_gains_w`). This is now netted off every state's heating demand identically via `src/thermal_counterfactual_gb/physics.py`'s `effective_outdoor_temp_c`/`net_heating_power_kw` (PROJECT.md Section 2.3, no double-counting: gains are a heat source, not a change to H). In the single-node (1R1C) model alone, purely as an illustration of the mechanism, the effect is asymmetric by design, not by error: against baseline's large loss (273 W/K), 400W is a small fraction and coastdown extends only modestly (4.7h → 5.0h, single-node figures); against EPC-C's small loss (86 W/K), the same 400W is a much larger fraction and coastdown extends substantially (15.0h → 18.7h, single-node figures). Those single-node numbers are not the standing result. Under the 2R2C structural sensitivity (Section 8.9), with gains netted off throughout, the standing coastdown range is baseline 1.6–3.9h (never clears the 4-hour window), SWI-only 2.0–4.4h (newly, narrowly clears only at the single most generous point in the sweep, f_air=0.20), and EPC-C 11.4–14.3h (clears throughout, already-robust margin more robust still).

**Baseline HTC sanity check — RESOLVED, no correction needed.** External review separately asked whether the baseline heat-loss coefficient might be artificially low (citing ~120 W/K as a red flag, and 250-300 W/K as the expected range for a "truly leaky" unretrofitted pre-1919 mid-terrace). This project's baseline H = 273 W/K (215 W/K fabric + 58 W/K ventilation) already falls inside that range and always has — verified by direct hand calculation, not adjusted (`notebooks/01` Section 6).

C (thermal capacity) = 10 kWh/K [**PROVISIONAL** — asserted in the original brief, not yet independently sourced against a pre-1919 brick archetype study].

**Wall U-value — RESOLVED, GROUNDED (was PROVISIONAL at 2.1).** RdSAP's own official default for solid brick wall was revised from 2.1 to 1.7 W/m²K in v9.93 (Nov 2017), after BRE in-situ measurement of 300 dwellings found actual performance better than the old theoretical default (drylining/lath-and-plaster present drops it further to 1.55). BRE's primary data for standard-thickness (<330mm) solid walls — the relevant category for an ordinary mid-terrace, as opposed to thicker "non-standard" tenement walls — measured a mean of 1.57 W/m²K (n=85, median 1.59), closely corroborating the revised default. Source: BRE (2014), *In-situ measurements of wall U-values in English housing*; RdSAP v9.93 conventions.

**Window U-value — RESOLVED, GROUNDED at 3.1 W/m²K.** RdSAP10 Table 24 gives pre-2002 wood/PVC-frame double glazing as 3.1 / 2.8 / 2.7 W/m²K for 6mm / 12mm / 16mm+ gaps; the era-band structure (before 2002 / 2002–2022 / after 2022) was directly confirmed against the primary RdSAP10 specification text. Convention 3.12b instructs assessors to use the 6mm (narrow-gap) value when the actual gap can't be identified — exactly this archetype's situation — giving 3.1 as the convention-compliant conservative cell, with no further adjustment needed. An earlier proposal to layer an additional seal-failure/gas-loss degradation penalty on top (targeting 3.5) was rejected: the cited "+32%" figure (Asphaug, via Likins-White et al. 2023) applied correctly to 3.1 gives ~4.1, not 3.5, so the arithmetic didn't support the number; the mechanism (argon-gas loss) likely doesn't apply to pre-2002 units, which typically weren't argon-filled to begin with; and reveal/perimeter infiltration is a distinct physical pathway already captured by the model's ACH term, not something that belongs folded into a conduction U-value (same no-double-counting principle as Section 2.3, applied to a different variable). If a degraded-glazing stress case is wanted later, it should be a separate, minority-weighted (~9%, per Lingnell's 25-year field failure data) PROVISIONAL sensitivity — not the baseline.

Resolved as a side effect: the baseline state now represents typical retrofitted-but-dated double glazing, not worst-case single glazing — consistent with 89% of English dwellings nationally already having double glazing (EHS 2024-25).

## 8.4 Tenure & Insulation Model

| Tenure | Estate share | Solid wall insulation probability | Status |
|---|---|---|---|
| Local authority (retained) | ~24% | 34% | GROUNDED (share derived from RSH 2024-25 stock split; probability directly cited, EHS 2024-25 Annex 2.10) |
| Housing association (retained) | ~41% | 37% (up from 28% in 2023) | GROUNDED |
| Ex-Right to Buy, privately rented | ~15% | 10% | GROUNDED |
| Ex-Right to Buy, owner-occupied | ~20% | 11% | GROUNDED |

Weighted current-state insulation prevalence ≈ 27%.

LA and HA are modelled as **separate trajectories, not combined** — HA's one-year jump (28%→37%) plausibly reflects more flexible access to blended private finance versus LA's ring-fenced but resource-constrained Housing Revenue Account. This divergence is itself a modelling output worth tracking over future funding rounds, not a static input.

## 8.5 Six-Stage Pipeline Mapping

| Stage | thermal-counterfactual-gb deliverable |
|---|---|
| A — Empirical Ground Truth | EHS/DESNZ tenure, insulation-rate, and retrofit-cost data; Warm Homes Plan funding figures — all cited, not assumed |
| B — Temporal & Distributional Analysis | Cold snap event selection (December 2022 coldest 7-day window, primary; Beast from the East 2018, backlog sensitivity) |
| C — Physical / Synthetic Asset Modelling | Pre-1919 mid-terrace RC model, 3 envelope states, H/C/τ derivation |
| D — Dispatch & Scenario Modelling | Baseline (no VPP) / theoretical ceiling (100% EPC-C) / realistic hybrid (tenure-weighted current-state population) / anti-correlation stress test (see below) |
| E — Value Gap & Derating Framework | DNO reinforcement avoidance and VPP flexibility value applied only on top of the physical peak-reduction result — never double-counted against comfort-floor behaviour already in the coastdown model |
| F — Monte Carlo & Uncertainty Propagation | Estate-wide headline is a **deterministic weighted average** (Σ tenure share × insulation probability × per-state peak reduction) — not a population simulation, since category assignment carries no real per-dwelling stochastic variation once shares are known. Monte Carlo is reserved for (i) propagating uncertainty in the PROVISIONAL parameters (COP, C, ex-RTB rented/owner split, geometry) into a genuine P10/P50/P90 band, and (ii) a separate small-N (~20–50 home) feeder-level sensitivity, where which dwellings actually land on a given feeder is a real source of variability a DNO would care about |

**Anti-Correlation Stress Test for this project:** the coldest evening of the event window coincides with (a) the lowest-insulation tenure segments being disproportionately represented in a specific feeder, and (b) tenant comfort overrides triggering simultaneously across the population — i.e. the "hidden battery" being smallest exactly when the grid needs it most. This must be run and reported, not assumed away.

## 8.6 Assumptions Ledger

**GROUNDED:** solid wall insulation rate by tenure (EHS 2024-25); national LA/HA social stock split (RSH 2024-25); cumulative Right to Buy sales and peak 1981 LA stock; cost to reach EER C by tenure and age band (EHS 2024-25); Warm Homes Plan and Social Housing Fund figures; solid wall U-value range for pre-1919 stock (RdSAP conventions); internal surface resistances used to derive the 2R2C air-mass coupling (BS EN ISO 6946 — the same standard already implicit in every U-value used elsewhere in this project); UK domestic battery installed cost range (multiple independent 2026 market surveys); domestic battery power rating range (Tesla Powerwall 3 / GivEnergy datasheets); bundled solar+battery installed cost (multiple independent 2026 UK market surveys); VPP+arbitrage real earnings range (Axle Energy, Kraken/Octopus, Tesla UK VPP, 2026); electricity price for bill-saving calculations (26.11 p/kWh, Ofgem Q3 2026 price cap); average grid carbon intensity (0.131 kg CO2e/kWh, DESNZ 2026 GHG Conversion Factors, cross-checked vs National Grid ESO); statutory low-voltage band relevant to solar export risk (216–253V, ENA/NGED G98-G99 — mechanism only, not quantified against this archetype); MEES extension to the social rented sector (EPC C-equivalent by 2030/2039, £10,000/property spend cap) and the reformed Decent Homes Standard's Criterion D (Thermal Comfort, compliant by 2035) — both real, dated government commitments underpinning Finding 6's landlord-finance framing; what Existing Use Value-Social Housing (EUV-SH) is and that it is a rental-income-based valuation lenders assess covenants against (the specific EPC-to-EUV-SH causal link is DELIBERATE reasoning, tagged below, not this definitional fact); solid wall insulation's standard assumed measure life (36 years, Ofgem ECO/Green Deal "Appropriate Guarantees" convention — cavity wall insulation is 42, mobile-home insulation 30), used in Finding 8's lifetime economics.

**PROVISIONAL:** ex-RTB private-rented vs owner-occupied split (derived from NEF's ">4 in 10" finding, not a precise published ratio); dwelling geometry defaults; C = 10 kWh/K; heat pump COP = 2.5 at −3°C; DNO flexibility-service illustrative rate (£68/kW/year, search-summarized Piclo Flex tender data, not independently verified against a primary document); the 2R2C air-node capacitance fraction (swept 2-20%, not independently grounded for this archetype); UK solar specific yield and system size (850-1100 kWh/kWp/yr, 4kWp typical); BESS/solar adoption rate by tenure (back-derived from MCS tenure-share-of-owners data and total UK install counts, not a directly published per-tenure rate — same derivation method already used for the ex-RTB rented/owner split); internal gains (300-500W range, 400W point estimate — bottom-up estimate cross-checked against ASHRAE occupant metabolic figures, not a single directly-cited UK-domestic table value; modelled as a flat constant with no diurnal schedule); monthly mean outdoor temperatures used for the Week 6 annual-energy calculation (climate-data.org Manchester climatology, disclosed as a proxy for Met Office 1991-2020 averages, not the primary series itself); marginal grid carbon intensity (0.35-0.40 kg CO2e/kWh, a CCGT-typical-emissions proxy, explicitly NOT an official long-run marginal emissions factor series — the choice between average and marginal bases for a carbon headline is itself a genuinely unresolved methodological question in the wider literature, which is why both are reported rather than one being picked).

**DELIBERATE:** 1R1C single-node thermal model as the primary model, cross-checked (not replaced) by a 2R2C structural sensitivity — see 8.9 for what that sensitivity found; single archetype rather than multi-archetype estate; adiabatic party walls; external wall insulation (EWI) assumed for both retrofit states, not internal (IWI) — see 8.9; a 15% non-ideal-orientation solar yield derate for a mid-terrace's front/rear roof pitches; marginal (flat £/kWh) battery-cost comparison in `notebooks/05` Section 5, which ignores real batteries' discrete standard sizes and fixed inverter/install costs; the Week 6 annual-energy method uses 12 monthly mean temperatures run through the project's own `net_heating_power_kw` function rather than an externally-published heating-degree-day figure at a fixed base temperature, specifically to avoid reintroducing the internal-gains double-counting/inconsistency Section 8.3 already resolved once (a fixed base temperature implicitly assumes uniform gains regardless of a state's own H, which this project's own Finding 1 shows is false) — this is a known conservative bias, since monthly-mean flooring understates true demand more for low-H/well-insulated states than for high-H/leaky ones; the Week 6 landlord-finance framing in Finding 6 (`bess_solar_vpp.landlord_finance_context`) reasons that a below-standard EPC plausibly depresses a housing association's reported EUV-SH stock valuation, as an inference from real MEES/Decent-Homes compliance exposure rather than an independently sourced valuation-methodology link.

**FORWARD-LOOKING:** any VPP/DNO payment mechanism that would actually monetise fabric's flexibility at the residential scale modelled here (note: this does NOT apply to BESS/VPP, whose revenue mechanism is real and contractible today — see `notebooks/05`); continuation of the Warm Homes Fund at its current run-rate through 2028–2030; the February 2026 Warm Homes Social Housing Fund extension to battery storage actually shifting social housing's ~5.2% BESS/solar adoption rate (too recent to be reflected in current data).

**OMITTED (not modelled, must stay visible, never hidden):** domestic hot water; measured smart-meter data; manufacturer-specific heat pump COP curves; real DNO substation-level headroom; actual tenant behaviour data including occupant heating patterns and fuel-poverty self-rationing; a verified one-off avoided-reinforcement CAPEX value (distinct from the illustrative recurring flexibility-service rate); spatial autocorrelation of tenure within real streets/feeders; a metered, dispatchable asset layer that would make fabric-driven flexibility actually contractible; hour-by-hour solar generation/self-consumption/export dispatch simulation; real roof-area/orientation survey data for this specific archetype; battery degradation, round-trip efficiency losses, and inverter clipping.

**OMITTED_QUALITATIVE (Week 6, new status — flagged with literature grounding via the Sledgehammer Test, but not modelled or quantified for this archetype):** summer solar export / voltage rise risk at the LV feeder (mechanism grounded in ENA/NGED G98-G99 statutory voltage limits, but no export volume, no feeder-level voltage simulation, no interaction with this project's own retrofit states); summer overheating risk (mechanism grounded in CIBSE TM59 2026 and 2025 peer-reviewed literature on EWI-vs-IWI summer comfort — the same EWI assumption already used in this project's retrofit states plausibly outperforms IWI here too, but that is a literature-sourced direction, not a modelled result — no indoor temperature simulation, no overheating-hours count for this archetype).

## 8.7 Notebook Plan

- `01_archetype_physics.ipynb` — geometry, three envelope states, H/C/τ derivation and hand-check (Week 1)
- `02_cold_snap_simulation.ipynb` — weather data ingestion, hour-by-hour coastdown simulation, baseline vs. retrofit comparison (Week 2)
- `03_estate_population_model.ipynb` — deterministic tenure/insulation weighted-average headline; parameter-uncertainty Monte Carlo over PROVISIONAL inputs for P10/P50/P90; small-N street-level sensitivity (a real LV feeder serves ~100-300 homes, so a 30-home sample is a street, not a feeder — terminology corrected after external review); anti-correlation stress test (Week 2–3)
- `04_vpp_economics.ipynb` — physics-to-£ translation, retrofit cost-benefit, battery-equivalence framing (led by delivered not nominal capacity), and an explicit category-error correction on DNO flexibility-service value: passive fabric cannot bid into metered tenders, so that figure is presented as illustrative-if-contractible, not a revenue estimate (Week 3)
- `05_bess_vpp_solar_comparator.ipynb` — extends the model to a BESS (battery energy storage system) + rooftop solar + VPP fit-out, compared against fabric retrofit three ways (fabric-only / BESS+solar-only / fabric+BESS stacked): whether a battery can physically cover peak demand (power rating) and for how long (energy capacity); the fabric-shrinks-the-battery-you-need synergy; real (not illustrative-if-contractible) VPP+arbitrage revenue; and a tenure-adoption comparison showing BESS/solar's own, differently-shaped split-incentive problem (Week 5)
- `06_annual_impact_and_carbon.ipynb` — extends the model from the single −3°C design-condition event to a whole-year view: annual space-heating electricity by fabric state (12 monthly-mean-temperature method, not an external HDD figure — see 8.6 DELIBERATE), displaced energy/bill savings/carbon abatement per home for each pairwise fabric comparison (carbon reported on both average-grid and marginal-proxy bases, no single headline picked), an estate-scale potential-vs-today's-27%-uptake view paralleling the DNO article's peak-demand framing, a qualitative (Sledgehammer Test) treatment of two summer risks — solar export/voltage rise and overheating — neither of which this project models quantitatively (Week 6), and a Section 8 lifetime-economics extension (Finding 8) computing simple payback and gross-vs-net marginal abatement cost over a sourced 36-year fabric life, reusing Section 3's baseline→EPC-C figures directly so the two sections cannot drift out of sync
- `07_interactive_demo/` — Streamlit app consuming the parquet outputs of 01–06 (Week 4, renumbered from 05 when the BESS/VPP/solar comparator was inserted ahead of it, and renumbered again from 06 to 07 when the Week 6 annual-impact notebook was inserted ahead of it — same transparent-renumbering practice as before, not a silent change)

Each notebook writes to `data/intermediate/*.parquet` per the Parquet Handoff Rule; no in-memory dataframe passing across weeks.

## 8.8 Definition of Done — MVP (Weeks 1–4)

- [ ] `configs/tenure_insulation_assumptions.yml` populated, every value tagged GROUNDED/PROVISIONAL/DELIBERATE/FORWARD-LOOKING/OMITTED
- [ ] Archetype geometry and three envelope states documented with sources
- [ ] H, C, τ hand-verified for all three states before any simulation code runs
- [ ] Cold snap event and region selected and pinned to a data source
- [ ] Coastdown simulation run hour-by-hour; baseline vs. SWI-only vs. EPC-C compared
- [ ] Estate-level headline computed as a deterministic weighted average across the corrected LA (~24%) / HA (~41%) / ex-RTB tenure shares — reproducible by hand, not a population simulation
- [ ] P10/P50/P90 reported only from genuine sources of uncertainty: Monte Carlo over PROVISIONAL parameters (COP, C, ex-RTB split, geometry) and/or a small-N feeder-level draw — never from resampling a categorical mix whose shares are already fixed
- [ ] Anti-correlation stress test run and reported
- [ ] No £/MW avoidance figure published without a cited or explicitly-flagged-placeholder cost source
- [ ] Every headline number reproducible from the config files in under 60 seconds
- [ ] README states what the model does **not** prove

## 8.9 Open Questions Not Yet Resolved

Does any mechanism currently exist for a VPP or DNO to pay for this specific form of residential thermal flexibility, or is it — like the bilateral contract question in prior work — recommended-but-not-yet-real? **Resolved, negatively:** it does not. Passive fabric retrofit has no meter, no controllable asset, and no dispatch signal, so it cannot bid into metered flexibility-service tenders (Piclo Flex and equivalent) as currently structured — pricing avoided-kW against a flexibility-service rate is a category error, not just an optimistic assumption. `notebooks/04` and `configs/tenure_insulation_assumptions.yml` (`vpp_economics.dno_flexibility_value_gbp_per_kw_per_year.category_error_warning`) now say this explicitly; the £/kW figure is retained only as a "what would this be worth if it were contractible" illustration.

Is the LA/HA ownership split for pre-1919 terrace stock specifically different from the national all-ages ratio used here? Still open.

**Resolved:** would a 2R2C model change the headline coastdown numbers enough to matter? Yes, substantially, and asymmetrically. External review correctly flagged that a 1R1C model cannot show indoor air cooling faster than the whole-building average implies, because it has no separate low-capacity air node — and that gap is concentrated in exactly the first few hours after heating stops, i.e. the peak window this project's claims are about. A 2R2C sensitivity (`notebooks/01_archetype_physics.ipynb` Section 7), with the air-mass coupling grounded in BS EN ISO 6946 standard surface resistances and the capacitance split swept across a deliberately generous range, shows baseline and SWI-only fabric mostly do NOT clear the 4-hour peak window (2R2C range 1.6-4.4h vs the 1R1C headline of 5.0-6.0h — figures include the internal-gains revision below; SWI-only clears it only at the single most generous sweep point), while EPC-C clears it comfortably across the same range (11.4-14.3h vs the 1R1C headline of 18.7h). The 1R1C coastdown-hours figures are now documented as upper bounds, not point estimates, everywhere they're quoted. The steady-state peak-kW reduction figure (1.80 kW/home) is unaffected, since it doesn't depend on how C is split, nor on the internal-gains revision (see below — gains cancel out of any difference between states).

**New, from external review, not yet resolved:** does the swi_only/epc_c_package retrofit assume external (EWI) or internal (IWI) wall insulation? This project now states EWI explicitly (`configs/tenure_insulation_assumptions.yml`, `envelope_states.wall_insulation_type_assumption`) but has not built a parallel IWI sensitivity — IWI would likely strand more of the brick's thermal mass on the cold side of the new insulation layer, reducing usable capacitance and shortening the effective coastdown relative to what's reported here. Does the ex-RTB low-insulation streets identified in the anti-correlation stress test spatially coincide with a DNO's actual constrained feeders? Not established — flagged as a testable hypothesis, not a finding, in `notebooks/03` Section 6b.

**Resolved (two-part follow-up review):** was the model treating the dwelling as an empty box with no internal heat gains, and was the baseline heat-loss coefficient artificially low? Internal gains: yes, and now fixed — a 400W constant gain (PROVISIONAL, ASHRAE-cross-checked) is netted off every state's heating demand. In the single-node model alone, purely as a mechanism illustration, this extends coastdown asymmetrically (baseline 4.7h→5.0h, EPC-C 15.0h→18.7h); the standing 2R2C+gains range is baseline 1.6–3.9h (never clears), SWI-only 2.0–4.4h (newly, narrowly clears only at its single most generous sweep point), EPC-C 11.4–14.3h. Baseline HTC: no, it was not artificially low — 273 W/K already sat inside the 250-300 W/K range independently proposed for a leaky pre-1919 terrace; verified, not adjusted. See Section 8.3 above for the full before/after figures.

**Resolved (same follow-up review, stress-test reconciliation):** does the anti-correlation stress test's "zero breaches during the recorded event" square with Finding 1's "baseline never clears the 4-hour window at −3°C design temp"? Yes — the recorded December 2022 peak window (16:00–20:00) only reached about −1.4°C to +2.0°C across the whole week, well above the −3°C design case, so the absence of breaches at recorded temperatures is consistent with a thin design-temp margin, not a contradiction of it. Also caught in this pass: the stress test (`notebooks/03` cell 15/17) was not netting off `internal_gains_w` at all, unlike every other heating-power calculation in this project — fixed, which moved the breach point from −6°C to **−8°C** colder than the recorded event (outdoor min in peak window at breach: −9.4°C). The stress test uses the single-node (1R1C) model, matching `notebooks/02`, not the 2R2C structural sensitivity — that sensitivity has not been wired into the dynamic event simulation, only into the static coastdown check in `notebooks/01` Section 7. This makes the stress test conservative in a specific, identifiable direction: since 1R1C coasts longer than 2R2C, the standing 2R2C coastdown ranges imply some original-fabric homes would likely breach even in the recorded week's milder window — the dynamic test's zero-breaches result understates today's exposure, not overstates it. The 22/30 and 27/30 street-exposure counts are pure population-tenure arithmetic and are unchanged by the gains fix; the coincident-spike kW figures shifted slightly to ~64.6 kW / ~79.2 kW.

Independently re-derived from the exact pipeline intermediates (not the rounded display figures): baseline H = 272.75 W/K (displays as 273), and the breach-point reference outdoor minimum = −9.37°C (displays as −9.4°C). Hand-reproducing the per-home coincident-spike kW using the *displayed* rounded figures (273 W/K, −9.4°C, 19°C comfort floor, 400W gains, COP 2.5) gives 2.941 kW/home, versus the pipeline's exact 2.935 kW/home — a ~0.2% gap from display rounding, not a computation bug. 2.935 × 22 = 64.57 kW and 2.935 × 27 = 79.24 kW, both matching the printed 64.6 kW / 79.2 kW. A reader hand-checking from the rounded table values alone may land on 64.7/79.4 instead — expected, and within the rounding tolerance of a two-decimal display table, not a discrepancy in the underlying model.

**New, from the Week 5 BESS/VPP/solar extension, not yet resolved:** does BESS/solar's real ~5.2-8.3% tenure-level adoption rate (`configs/tenure_insulation_assumptions.yml`, `bess_solar_vpp.adoption_by_tenure`) actually have a genuine LA-vs-HA or ex-RTB-rented-vs-owner breakdown, or is the current combined/national-rate approximation hiding real variation the way the pre-correction LA/HA fabric figures once did? Would a real roof-area and orientation survey for this specific pre-1919 mid-terrace archetype change the 4 kWp achievable-system-size assumption materially — particularly given the conservation-area front-pitch planning restriction noted in `bess_solar_vpp.solar_pv.roof_constraint_note`? Does the February 2026 Warm Homes Social Housing Fund battery-storage extension change social-landlord BESS/solar uptake enough, over the next 1-2 years, to close any of the 4.6x adoption gap with fabric retrofit — genuinely unknown, since the mechanism is too new to have observable uptake data yet.

**New, from the Week 6 annual-impact extension, not yet resolved:** which grid-carbon basis (average vs marginal) is the *right* one for a retrofit carbon-abatement headline is a genuinely contested methodological question in the wider decarbonisation literature, not something this project can resolve on its own — the deliberate choice here is to report both, explicitly labelled, rather than pick one and imply the debate is settled; a reader with a house view on this question should substitute their own preferred marginal series for the CCGT-typical proxy used here. The monthly-mean-temperature method for annual energy (8.6 DELIBERATE) has a known conservative bias that has not been quantified — how much would a full degree-day or hourly-temperature-distribution method raise the annual kWh figures, particularly for EPC-C, where the bias is largest? Both summer-dynamics risks (solar export/voltage rise, overheating) are flagged with real literature but have not been checked against this specific archetype's own roof area, glazing ratio, or feeder characteristics — a natural Week 7+ extension, not attempted here per the Sledgehammer Test (Section 2.2).

**Resolved (negawatt/policy-audience article, lifetime economics):** an early draft of a general-policy-audience article computed a "£/tonne abated" figure using an unsourced, round-number 40-year fabric life, and — more substantively — treated the retrofit's capital cost as a pure cost without netting off the lifetime bill savings the same spend also buys, despite the same draft separately stating a 5.4-year bill-saving payback. Both are now fixed: the fabric life is sourced (36 years, Ofgem ECO/Green Deal "Appropriate Guarantees" convention for solid wall insulation — see 8.6 GROUNDED), and Finding 8 reports both a GROSS figure (capital cost only, ≈£299/tCO2e average) and the methodologically standard NET figure (capital cost minus lifetime bill savings, ≈–£1,694/tCO2e average — negative, meaning the measure is cash-positive over its life even before counting carbon value at all). The net figure is the correct one for a like-for-like comparison against other measures' marginal abatement costs; the gross figure is retained alongside it only for readers who want the unnetted number, not because it is more authoritative.

**New, from the Week 6 landlord-finance addendum to Finding 6, not yet resolved:** does a below-standard EPC actually depress a housing association's reported EUV-SH valuation, and by how much? This project reasons that it plausibly does, from the real MEES/Decent-Homes compliance exposure now attached to non-compliant stock (`bess_solar_vpp.landlord_finance_context.euv_sh_valuation_link`, DELIBERATE), but has not found or checked a primary RICS/valuer methodology document that states this link directly, nor any figure for its size. Treat the landlord-finance framing in Finding 6 as a well-evidenced *mechanism* (real compliance dates, real spend caps, real valuation basis) with an *inferred*, not sourced, connection between the pieces — the honest state of this argument, not a gap to quietly paper over.

## 8.10 References

Full citation list carried from the project scoping conversation: English Housing Survey 2024–25 (Chapters 1–2, Annex Tables 2.1–2.15), DESNZ Household Energy Efficiency Statistical Releases (March 2025, November 2025), Regulator of Social Housing local authority stock statistics (2024–25), New Economics Foundation Right to Buy analysis (2024), Warm Homes Plan and Warm Homes: Social Housing Fund publications (January 2026), RdSAP Conventions v11.4, BRE in-situ U-value measurements.
