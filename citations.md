# Citations

Full source list for `thermal-counterfactual-gb`, organised by topic. Each entry states exactly what it's used for and where (config field, notebook, or `PROJECT.md` section), plus its evidentiary status per the Assumptions Ledger (`PROJECT.md` Section 8.6): **GROUNDED** / **PROVISIONAL** / **DELIBERATE** / **FORWARD-LOOKING** / **OMITTED**.

This file is the single index. It does not repeat the reasoning behind each number — that lives in `PROJECT.md` Section 8.3–8.6 and in the notebooks themselves — it exists so every citation can be checked in one place instead of hunting through config comments and markdown cells.

---

## Housing stock, tenure, and insulation rates

**English Housing Survey (EHS) 2024–25**, Department for Energy Security and Net Zero / Ministry of Housing, Communities and Local Government.
[Collection page](https://www.gov.uk/government/collections/english-housing-survey-2024-to-2025-headline-findings-on-housing-quality-and-energy-efficiency) · [Headline report on housing quality and energy efficiency (PDF)](https://assets.publishing.service.gov.uk/media/697a0f35005d288bf850deb2/2024-25_EHS_Headline_Report_on_Housing_Quality_and_Energy_Efficiency.pdf)
Used for: `solid_wall_insulation_probability` (Annex Table 2.10), `retrofit_cost_gbp_to_epc_c` (Annex Table 2.14), 89% national double-glazing prevalence (`PROJECT.md` §8.3).
Status: **GROUNDED**.
Note: the 2024–25 headline release was split into two publications — demographics/resilience findings released first, with housing quality and energy efficiency findings (the ones this project relies on) published January 2026. The detailed topic-level Annex Tables this project cites by number are due to roll out through spring/summer 2026; re-verify the exact Annex Table numbers against the final published tables once they land, rather than assuming the numbers cited here are final.

**Department for Energy Security and Net Zero (DESNZ), Household Energy Efficiency Statistics**, statistical releases March 2025 and November 2025.
[Statistics landing page](https://www.gov.uk/government/organisations/department-for-energy-security-and-net-zero/about/statistics)
Used for: corroborating national energy-efficiency uptake context referenced in `PROJECT.md` §8.5 Stage A.
Status: **GROUNDED**.

**Regulator of Social Housing (RSH), local authority stock statistics 2024–25**.
[Statistics at RSH](https://www.gov.uk/government/organisations/regulator-of-social-housing/about/statistics)
Used for: `tenure_mix.local_authority_retained` / `housing_association_retained` split (LA:HA ratio within social stock).
Status: **GROUNDED**.
Note: 2024–25 Local Authority Housing Statistics did not have a 100% response rate (two authorities' Section K data missing); a minor, undocumented source of imprecision in the LA/HA ratio.

**New Economics Foundation (NEF), "More than 4 in 10 council homes sold under right to buy now owned by private landlords"**, May 2024.
[Article](https://neweconomics.org/2024/05/more-than-4-in-10-council-homes-sold-under-right-to-buy-now-owned-by-private-landlords)
Used for: `tenure_mix.ex_rtb_privately_rented` / `ex_rtb_owner_occupied` split basis (the "&gt;4 in 10" finding); cumulative Right to Buy sales and peak 1981 LA stock figure (5.49m homes).
Status: **PROVISIONAL** — NEF's finding is a share of *sold* RTB homes now privately rented, not a precise published rented/owner-occupied ratio for the whole ex-RTB population. `notebooks/03` runs a two-point sensitivity (35%–50% rented fraction) around this because of that imprecision.

---

## Building physics — RdSAP conventions and U-values

**BRE, "In-situ measurements of wall U-values in English housing"**, 2014 (for DECC).
[Report (PDF)](https://assets.publishing.service.gov.uk/media/5a804b9eed915d74e33f99a7/In-situ_u-values_final_report.pdf)
Used for: `envelope_states.baseline.wall_u_w_per_m2k` = 1.7 W/m²K. BRE measured ~300 dwellings (137 solid-wall, 87 with detailed investigation); mean in-situ solid-wall U-value 1.57 W/m²K (n=85), which corroborates RdSAP v9.93's revised default.
Status: **GROUNDED**.

**BRE Group, RdSAP 10 Specification and Conventions** — project used **v11.4** at the time of research; **v12.1 (21 August 2025)** is the current published version as of this citations pass.
[RdSAP 10 Specification, June 2025](https://bregroup.com/documents/d/bre-group/rdsap-10-specification-10-06-2025) · [Conventions v12.1](https://bregroup.com/documents/d/bre-group/rdsap-conventions-v12-1-21-august-2025-final)
Used for: `envelope_states.baseline.window_u_w_per_m2k` = 3.1 W/m²K (RdSAP10 Table 24, pre-2002 wood/PVC frame, 6mm gap); Convention 3.12b (use the narrow-gap value when actual gap width is unknown — this archetype's situation); the v9.93 (Nov 2017) revision of the solid-brick wall default from 2.1 to 1.7 W/m²K.
Status: **GROUNDED**.
Note: conventions have moved from v11.4 (cited when this project's window/wall figures were verified) to v12.1 since. The specific tables and conventions referenced (Table 24, 3.12b) were confirmed against the RdSAP10 specification text directly, not just a secondary summary — but re-check against v12.1 before treating this as still current.

**Likins-White et al. (2023)**, cited via a secondary discussion of window seal degradation / argon-gas loss ("Asphaug" finding, ~+32% U-value degradation).
Used for: considered and explicitly **rejected** as a basis for inflating the baseline window U-value above 3.1 W/m²K — see `PROJECT.md` §8.3 for the full reasoning (arithmetic didn't support the proposed 3.5 figure; the mechanism likely doesn't apply to non-argon-filled pre-2002 units; reveal/perimeter infiltration is a separate physical pathway already captured by the ACH term). Kept here as a record of a rejected shortcut, not an input the model uses.
Status: not used in the baseline model. Flagged as a possible future PROVISIONAL sensitivity (minority-weighted, ~9% of stock per Lingnell's 25-year field failure data) if a degraded-glazing stress case is wanted later.

**BS EN ISO 6946, "Building components and building elements — Thermal resistance and thermal transmittance — Calculation methods."**
Used for: the standard internal surface resistances (Rsi = 0.13 m²K/W walls, 0.10 roofs, 0.17 floors) that split each opaque element's U-value into an "internal film" term and "rest of construction" term for the 2R2C structural sensitivity added after external review (`src/thermal_counterfactual_gb/physics.py`, `two_node_conductances_w_per_k`; `notebooks/01_archetype_physics.ipynb` Section 7). These values are not a new assumption — they're already implicit inside every U-value this project uses, this just makes that decomposition explicit and checkable.
Status: **GROUNDED** — standard, widely-cited values; not independently re-derived from the base standard for this project, but consistent with how RdSAP's own U-value tables are constructed.

**ASHRAE Fundamentals Handbook**, occupant metabolic heat-output data (via H2X Engineering's practical-guide summary, 2026).
[H2X internal heat gain guide](https://www.h2xengineering.com/blogs/internal-heat-gain/)
Used for: `internal_gains_w` (300-500W range, 400W point estimate) — bottom-up cross-check using seated/light-office-work per-person heat output (~115-140W total heat per person) for 3 occupants, plus typical domestic appliance/cooking/lighting casual gains (order ~100-150W time-averaged, general building-physics convention). Added after external review pointed out the model was treating the house as an empty box.
Status: **PROVISIONAL** — a bottom-up estimate cross-checked against a standard per-person figure, not a single directly-cited UK-domestic-specific table value (e.g. a CIBSE Guide A Table 6 domestic casual-gains figure pulled directly). Matches the 300-500W range independently proposed by external review. Modelled as a flat constant with no diurnal occupancy/cooking schedule — see `configs/tenure_insulation_assumptions.yml`, `internal_gains_w.omitted_from_this_figure`.

---

## Weather event

**Met Office, "Prolonged spell of low temperatures, December 2022"**, National Climate Information Centre, published 10 January 2023.
[Report (PDF)](https://www.metoffice.gov.uk/binaries/content/assets/metofficegovuk/pdf/weather/learn-about/uk-past-events/interesting/2022/2022_04_december_low_temperatures_v1.pdf)
Used for: `cold_snap_event` — the 11–17 December 2022 primary event window; UK area-average daily max/min figures used to calibrate the synthetic hourly diurnal profile in `notebooks/02`.
Status: **GROUNDED** for the event dates and UK area-average daily figures; the hourly profile itself is **PROVISIONAL** (a synthetic diurnal cycle calibrated to daily max/min, not raw ERA5/station hourly reanalysis — see `configs/tenure_insulation_assumptions.yml`, `cold_snap_event.hourly_profile_note`).

---

## Policy context

**Warm Homes Plan**, DESNZ, published 21 January 2026.
[Publication (HTML)](https://www.gov.uk/government/publications/warm-homes-plan/warm-homes-plan-html)
Used for: `policy_context` — £15bn total programme, £1.29bn Warm Homes Social Housing Fund, EPC-C backstop year 2030 for social/private rented.
Status: **GROUNDED** for the published figures; continuation of the programme at its current run-rate through 2028–2030 is **FORWARD-LOOKING** (`PROJECT.md` §8.6).

---

## VPP / DNO economics (Week 3, `notebooks/04`)

**Piclo Flex, DNO flexibility tender clearing-price data**, 2024/25/26 delivery windows (search-engine-summarized).
[Piclo Flex](https://picloflex.com/) · [About Piclo](https://www.piclo.com/about)
Used for: `vpp_economics.dno_flexibility_value_gbp_per_kw_per_year` — illustrative point estimate of ~£68/kW/delivery period ("Sustain" service average).
Status: **PROVISIONAL**. The primary Piclo/DNOA tender documents were not independently pulled for this MVP — this figure came from a search-engine summary of tender data, not a verified primary source. Treat the £68 point estimate as illustrative inside a wide £20–£100 band, not a checked market rate.
Category-error correction (external review): these tenders require metered, dispatchable, verifiable demand reduction against a settled baseline. Passive fabric retrofit alone has none of these and cannot bid into this market as modelled. `notebooks/04` and `configs/tenure_insulation_assumptions.yml` now present the resulting £/home/year figure as "what this would be worth if it were contractible," not a revenue estimate — see `vpp_economics.dno_flexibility_value_gbp_per_kw_per_year.category_error_warning`.

**UK Power Networks, DSO Performance Panel Report 2024/25**.
[Report (PDF)](https://d1lf1oz5vvdb9r.cloudfront.net/app/uploads/2025/04/UK-Power-Networks-DSO-Performance-Panel-Report-2024-25.pdf)
Used for: corroborating context only (flexibility delivered ~£91m in avoided-reinforcement customer benefit in 2023/24) — an aggregate figure, not a £/kW rate, so not used directly in any calculation.
Status: **GROUNDED** as context; not a model input.

**UK domestic battery storage installed cost, 2026 UK retail market surveys**: BookaBuilderUK, Renewables Excellence, Habo Energy, How To Go Solar.
[BookaBuilderUK](https://www.bookabuilderuk.com/blog/home-battery-storage-installation-cost-2026) · [Renewables Excellence](https://renewablesexcellence.co.uk/battery-storage-installation-costs-uk/) · [Habo Energy](https://haboenergy.co.uk/home-battery-storage-cost) · [How To Go Solar](https://www.howtogosolar.org/home-battery-storage/)
Used for: `vpp_economics.domestic_battery_installed_cost_gbp_per_kwh` — £400–£950/kWh installed, £650/kWh point estimate.
Status: **GROUNDED** — four independent market surveys triangulate to the same order of magnitude for a ~10kWh installed system (including 0% VAT, available until March 2027).

---

## BESS / solar / VPP comparator (Week 5, `notebooks/05`)

**Tesla Powerwall 3 Datasheet**, Tesla Energy Library.
[Datasheet (PDF)](https://energylibrary.tesla.com/docs/Public/EnergyStorage/Powerwall/3/Datasheet/en-us/Powerwall-3-Datasheet.pdf)
Used for: `bess_solar_vpp.battery_hardware.continuous_power_rating_kw` high end (11.5 kW).
Status: **GROUNDED**.

**GivEnergy All-in-One 2 product data**, via Atlantic Renewables and Lumos Energy 2026 comparison guides.
[Atlantic Renewables comparison](https://www.atlanticrenewables.co.uk/contact-us/news-blog/givenergy-all-in-one-2-vs-tesla-powerwall-3-which-one-works-best-for-you.html) · [Lumos Energy 2026 guide](https://lumos-energy.co.uk/blog/best-home-batteries-uk-2026-sigenergy-tesla-givenergy/)
Used for: `bess_solar_vpp.battery_hardware.continuous_power_rating_kw` low/point end (3.6-6 kW).
Status: **GROUNDED**.

**UK solar specific-yield and system-size market data**: Payaca MCS irradiance calculator, Sunsave, RenewableEnergyHub, 2026.
[Payaca](https://payaca.com/uk/solar-yield-calculator) · [Sunsave](https://www.sunsave.energy/solar-panels-advice/system-size/output) · [RenewableEnergyHub](https://www.renewableenergyhub.co.uk/main/solar-panels/how-much-electricity-does-a-solar-panel-produce)
Used for: `bess_solar_vpp.solar_pv` — 850-1100 kWh/kWp/yr specific yield, 4 kWp typical residential system size.
Status: **PROVISIONAL** — national averages, not archetype-specific; the 15% non-ideal-orientation derate applied on top is a DELIBERATE modelling choice, not itself sourced.

**Bundled solar+battery installed cost, UK 2026 market surveys**: bestbuilders.co.uk, sunsave.energy, uk.jackery.com, spectrumenergysystems.co.uk.
[bestbuilders (solar+battery)](https://www.bestbuilders.co.uk/costs/solar-system-size-cost-uk) · [Sunsave batteries](https://www.sunsave.energy/solar-panels-advice/batteries/costs) · [Jackery 10kW guide](https://uk.jackery.com/blogs/buying-guide/10-kw-solar-battery-price-uk) · [Spectrum Energy](https://spectrumenergysystems.co.uk/articles/solar-panel-installation-cost-uk-2026/)
Used for: `bess_solar_vpp.installed_cost_gbp_bundled_4kwp_10kwh` — GBP 10,500-19,500, point GBP 13,500 for a bundled ~4kWp+10kWh install.
Status: **GROUNDED** — multiple independent 2026 surveys triangulate to a consistent, if wide, order of magnitude.

**VPP dispatch and time-of-use arbitrage earnings, UK 2026**: Habo Energy market summary (Axle Energy, Kraken/Octopus, Tesla UK VPP).
[Habo Energy VPP guide](https://haboenergy.co.uk/virtual-power-plant-uk-home-battery)
Used for: `bess_solar_vpp.vpp_and_arbitrage_earnings_gbp_per_year` — GBP 120-300/yr VPP dispatch, GBP 800-950/yr arbitrage, combined GBP 920-1,250/yr.
Status: **GROUNDED** — this is a real, currently-contractible revenue stream, unlike the fabric DNO-flexibility figure above; the category-error correction that applies to fabric does not apply here, since a battery is metered and dispatchable by construction.

**MCS Certified, solar/battery installation and tenure data, 2026**.
[MCS record-installations release](https://mcscertified.com/record-number-of-renewables-being-installed-into-uk-homes/) · [Marley social-housing solar report](https://www.marley.co.uk/blog/social-housing-solar-panels-upgrade-report)
Used for: `bess_solar_vpp.adoption_by_tenure` — 70.6% of solar owners are owner-occupiers, 12.8% privately rented (tenure composition of solar OWNERS, not a per-tenure rate); 233,061 of ~4.5m social housing units have solar (~5.2%); February 2026 Warm Homes Social Housing Fund battery-storage extension.
Status: **PROVISIONAL** — per-tenure adoption RATES in `adoption_by_tenure` are back-derived from these share-of-owners figures combined with total UK solar counts (Sunsave/Kind Energy, ~1.5-1.95m homes) and EHS tenure population counts, not directly published. Same derivation method already used for `tenure_mix.ex_rtb_privately_rented`/`ex_rtb_owner_occupied` above; treat as order-of-magnitude, and as mixed-vintage across component sources.

**Landlord/tenant split-incentive guidance, UK solar market, 2026**: Upvolt Energy, EnergyPlus, SolarPowerUKGrants; Octopus Energy "Tenant Power" tariff announcement.
[Upvolt Energy](https://upvolt-energy.com/upvolt-blog/can-tenants-benefit-from-solar-panels-in-the-uk/) · [Octopus Tenant Power](https://octopus.energy/blog/introducing-tenant-power-our-tariff-for-social-housing-tenants/)
Used for: `bess_solar_vpp.split_incentive_note` — bill savings and VPP/arbitrage revenue typically accrue to the bill-paying tenant, not the landlord who would fund the install.
Status: **GROUNDED** for the general split-incentive mechanism and the Tenant Power product; **PROVISIONAL** for how commonly landlord-retained vs tenant-claimed export arrangements are actually used in practice (no national survey of arrangement prevalence was found).

**Conservation-area solar planning rules, UK terraced houses**: Spectrum Energy Systems, solarbypostcode.co.uk, 2026 guides.
[Spectrum Energy conservation-area guide](https://spectrumenergysystems.co.uk/articles/solar-panels-in-conservation-areas/) · [Solar by Postcode](https://solarbypostcode.co.uk/guides/planning-permission-conservation-areas-solar-uk/)
Used for: `bess_solar_vpp.solar_pv.roof_constraint_note` — rear-pitch panels are typically permitted development even in a conservation area; street-facing (front) panels typically require planning permission.
Status: **GROUNDED** for the general planning rule; **not independently checked** against this specific archetype's roof geometry or any real conservation-area designation.

---

## Annual impact and carbon (Week 6, `notebooks/06`)

**climate-data.org, Manchester station climatology, 1991-2021 monthly averages.**
[Manchester climate data](https://en.climate-data.org/europe/united-kingdom/england/manchester-3621/)
Used for: `annual_impact.monthly_mean_outdoor_temp_c` — 12 monthly mean temperatures, same North West England region as `cold_snap_event`.
Status: **PROVISIONAL** — a close proxy for the Met Office's own 1991-2020 normals series, not a citation to that primary dataset directly (its full monthly table could not be retrieved in this pass). Same disclosed-proxy pattern as `cold_snap_event.hourly_profile_note`.

**Ofgem, energy price cap announcements, 2026.**
[Q3 2026 price cap change](https://www.ofgem.gov.uk/news/changes-energy-price-cap-between-1-july-and-30-september-2026)
Used for: `annual_impact.electricity_price_gbp_per_kwh` — 26.11 p/kWh, Direct Debit standard variable tariff, 1 July–30 September 2026, GB average incl. VAT.
Status: **GROUNDED** for the quarter cited; the cap moves quarterly (27.69 p/kWh Jan–Mar 2026, 24.67 p/kWh Apr–Jun 2026) — the current quarter's figure is used as a point estimate, not a full-year weighted average.

**DESNZ, 2026 UK Government GHG Conversion Factors for Company Reporting**, published 11 June 2026.
[Publication collection](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2026)
Used for: `annual_impact.grid_carbon_intensity.average` — 0.131 kgCO2e/kWh, location-based UK grid electricity factor (down from 0.177 kg CO2e/kWh in 2025).
Status: **GROUNDED**. Cross-checked against National Grid ESO real-time carbon-intensity tracker data (2026 YTD average ~141 gCO2/kWh, rolling 12-month ~122 gCO2/kWh) — same order of magnitude.

**Combined-cycle gas turbine (CCGT) typical generation emissions intensity** — used as a labelled marginal-generation proxy, not an official series.
Used for: `annual_impact.grid_carbon_intensity.marginal_proxy` — 350-400 gCO2/kWh range.
Status: **PROVISIONAL**, explicitly NOT DESNZ's own long-run marginal emission factor (LRMEF) series, which could not be independently pinned to a precise current value in this pass — DESNZ's own appraisal guidance ("Valuation of energy use and GHG emissions for appraisal") in fact directs analysts to the average factor (Data Table 1) for grid electricity generation in most cases. Reported alongside the average figure per this project's own decision to show both rather than pick one, not because it is more authoritative.

**National Grid Electricity Distribution / Energy Networks Association (ENA), G98/G99 connection guidance.**
Used for: `annual_impact.summer_dynamics.solar_export_voltage_risk` — statutory UK voltage range (216-253V) and the general mechanism by which concentrated domestic solar export can raise local network voltage.
Status: **GROUNDED** for the general mechanism and statutory range; **not quantified** against this archetype or any real network — this project has no monthly/hourly solar generation shape or LV headroom data (Sledgehammer Test, qualitative flag only).

**CIBSE TM59 (2026 update), "Overheating risk in dwellings — a design stage methodology"**; and Buildings journal, "Effects of Retrofit Strategies on Thermal Comfort and Energy Performance in Social Housing for Current and Future Weather Scenarios" (2025).
[CIBSE TM59](https://www.cibse.org/knowledge-research/knowledge-portal/tm59-overheating-risk-in-dwellings-a-design-stage-methodology-2026/) · [Buildings journal paper](https://doi.org/10.3390/buildings15010080)
Used for: `annual_impact.summer_dynamics.overheating_risk` — retrofit can worsen summer overheating risk (particularly south-facing bedrooms in retrofitted social housing); external wall insulation outperforms internal wall insulation on summer comfort specifically.
Status: **GROUNDED** as a literature-documented risk and methodology; **not quantified** against this archetype (Sledgehammer Test, qualitative flag only).

---

## Lifetime economics (Week 6 addendum, Finding 8 / `notebooks/06` Section 8)

**Ofgem, Energy Company Obligation (ECO) "Appropriate Guarantees" scheme documentation.**
[Ofgem ECO Appropriate Guarantees, e.g. V8.0 2018 and successor versions](https://www.ofgem.gov.uk/publications/energy-company-obligation-eco-appropriate-guarantees)
Used for: `annual_impact.lifetime_economics.fabric_life_years` — standard assumed measure lifetimes for insulation installed under ECO/Green Deal: cavity wall insulation 42 years, solid wall insulation 36 years, mobile home insulation 30 years (distinct from the shorter 25-year financial-guarantee period itself).
Status: **GROUNDED** for the solid-wall-insulation figure specifically. Applies to solid wall insulation generally, not independently verified for the external wall insulation (EWI) variant this project assumes throughout — no EWI-specific lifetime figure was found separately. This figure replaced an earlier, unsourced round-number placeholder of 40 years used in an initial article draft; 36 years is the traceable figure and is what all published lifetime-economics numbers in this project now use.

**Derived: simple payback and lifetime marginal abatement cost (gross and net).**
Used for: `annual_impact.lifetime_economics.payback_years_baseline_to_epc_c` and `.marginal_abatement_cost_gbp_per_tco2e` — not an external citation, but a computation combining three already-cited figures (`retrofit_cost_gbp_to_epc_c`, `annual_impact.electricity_price_gbp_per_kwh`, `annual_impact.grid_carbon_intensity`) with the ECO/Green Deal lifetime above. The NET marginal abatement cost (which nets the retrofit's lifetime bill savings off its capital cost before dividing by lifetime carbon abated) is the methodologically standard treatment for a marginal abatement cost curve; the GROSS figure (capital cost only, bill savings ignored) is reported alongside it for readers who want the unnetted number, not because it is more correct.
Status: **GROUNDED** — a direct, reproducible arithmetic combination of GROUNDED/PROVISIONAL inputs already cited elsewhere in this file; see the `derivation` notes in the config block itself for the exact formula and the executed version in `notebooks/06_annual_impact_and_carbon.ipynb` Section 8.

---

## Landlord finance and compliance context (Week 6 addendum, Finding 6)

**UK Government, "Improving the Energy Efficiency of Socially Rented Homes" consultation and government response**, 2026; summarised by Elmhurst Energy and Simmons & Simmons.
[Consultation page](https://consult.communities.gov.uk/social-housing/srs-mees-consultation/) · [Elmhurst Energy summary](https://www.elmhurstenergy.co.uk/blog/2026/02/03/social-rented-homes-to-reach-epc-c-by-1st-april-2030/) · [Simmons & Simmons summary](https://www.simmons-simmons.com/en/publications/cmkws6657001itp58cb0i2cse/the-warm-homes-plan-mees-for-privately-rented-homes-epc-c-by-2030)
Used for: the claim, in `FINDINGS.md` Finding 6, that Minimum Energy Efficiency Standards (MEES) are being extended to the social rented sector for the first time — one reformed EPC metric by 1 April 2030, a second by 1 April 2039, subject to a time-limited £10,000-per-property spend cap exemption on the first deadline.
Status: **GROUNDED** for the compliance dates and spend-cap mechanism (corroborated across two independent secondary summaries of the same government consultation response); the primary consultation-response document itself was not read in full for this pass.

**Ministry of Housing, Communities and Local Government, "A Reformed Decent Homes Standard for Social and Privately Rented Homes" — consultation government response**, published 27 January 2026.
[Government response (GOV.UK)](https://www.gov.uk/government/consultations/consultation-on-a-reformed-decent-homes-standard-for-social-and-privately-rented-homes/outcome/consultation-on-a-reformed-decent-homes-standard-for-social-and-privately-rented-homes-government-response)
Used for: the claim that the reformed Decent Homes Standard's Criterion D (Thermal Comfort) requires MEES compliance, with providers given until 2035; and that a new Criterion E (damp and mould) was added separately.
Status: **GROUNDED**.

**Existing Use Value–Social Housing (EUV-SH)**, RICS-derived social-housing valuation methodology; via Trowers & Hamlins and Inside Housing.
[Trowers & Hamlins, "The Difference between EUV-SH and MV-ST"](https://www.trowers.com/insights/2023/april/the-difference-between-euv-sh-and-mv-st) · [Inside Housing, "Evaluating valuations"](https://www.insidehousing.co.uk/insight/evaluating-valuations-45282)
Used for: the claim, in `FINDINGS.md` Finding 6, that housing associations' stock is carried on the balance sheet at a rental-income-based valuation (EUV-SH) that lenders assess loan covenants against.
Status: **GROUNDED** for what EUV-SH is and that it is rental-income-based (roughly 30–40% of open-market value, region-dependent) and used as a lending/covenant basis. **NOT independently verified** — and explicitly flagged as such in `FINDINGS.md` — is the more specific causal claim that a below-standard EPC directly depresses a property's *reported* EUV-SH figure; no primary source quantifying that specific link was found in this pass. The finding presents this as reasoned inference from the compliance exposure above, not a sourced valuation mechanism.

---

## How to use this file

Every number above traces to exactly one row in `configs/tenure_insulation_assumptions.yml` or one named figure in `PROJECT.md` §8.3–8.4. If a notebook prints a number that isn't traceable to something in this list (or flagged `OMITTED`/`DELIBERATE` in the Assumptions Ledger), that's a bug — flag it, don't wave it through (Traceability Mandate, `PROJECT.md` Section 6).
