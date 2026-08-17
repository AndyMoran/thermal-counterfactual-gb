"""
check_headroom_revenue_scaling.py

"Rung 2" of the VPP-funded-battery ladder (see ADDENDUM.md addition below).
The flat GBP 1,075/year VPP+arbitrage revenue figure used throughout Finding 6
and notebook 05 is applied identically across all three fabric states -- this
project has always flagged that as a REASONED simplification, not a modelled
or field-verified result (see linkedin_article_bess_vendors.md posting notes
and Finding 6's own OMITTED-style caveats). This script asks a narrower,
checkable question: how much of that revenue should actually be expected to
scale with a fabric state's own spare battery capacity, and how much doesn't?

Two revenue components, two different mechanisms, NOT blended into one number:

1. Time-of-use ARBITRAGE (GBP 800-950/yr, Habo Energy market summary, already
   GROUNDED in citations.md): charge cheap overnight, discharge expensive
   during the evening peak. This is mechanically the SAME window Finding 6's
   comfort-holding draw competes for (16:00-20:00) -- a kWh spent holding
   comfort is a kWh that cannot be discharged for arbitrage that same evening.
   So this component should scale with Finding 6's own spare-capacity
   fraction by fabric state (2% / 18% / 74%). New for this check: PROVISIONAL,
   reasoned from Finding 6's already-grounded percentages, not independently
   modelled against real dispatch logs.

2. VPP DISPATCH / frequency-response events (GBP 120-300/yr, same citation):
   short, discrete grid-service events (see Axle Energy's GBP 1/kWh dispatch
   rate, Habo Energy 2026) that are not contractually tied to the 16:00-20:00
   window and can occur at any hour. Left UNSCALED here -- deliberately, not
   as an oversight. Scaling this by fabric state would invent a precision
   this check doesn't have. Flagged caveat: real DFS/frequency-response
   events cluster during winter system-stress periods, which correlates with
   exactly when comfort-holding draw is also highest (the same anti-
   correlation mechanism Finding 4 already found for coastdown exposure) --
   so this UNSCALED treatment is plausibly optimistic for baseline/SWI-only
   homes, not conservative. Named, not modelled.

Source for the "arbitrage scales with capacity, not flat" mechanism itself:
2026 UK installer/aggregator market guides state a 5kWh battery cycled daily
delivers "roughly half the absolute savings" of a 10kWh system -- consistent
with the underlying physics (a roughly constant GBP/kWh price spread, one
dominant daily cycle) rather than a claim pulled from nowhere, but still
PROVISIONAL, aggregator-marketing-adjacent sourcing, same evidentiary tier as
this project's other installer-survey-derived figures.
"""

# ── 1. Inputs already GROUNDED elsewhere in this project ────────────────────

# Finding 6: battery energy needed to fully cover the 16:00-20:00 peak, as a
# fraction of a 10kWh nameplate battery, by fabric state.
capacity_consumed_pct = {
    "baseline": 0.98,
    "swi_only": 0.82,
    "epc_c": 0.26,
}
capacity_spare_pct = {state: 1 - pct for state, pct in capacity_consumed_pct.items()}

# citations.md: Habo Energy market summary (Axle Energy, Kraken/Octopus,
# Tesla UK VPP) -- GROUNDED as a real, currently-contractible revenue stream.
dispatch_gbp_per_year = (120 + 300) / 2       # GBP 210 -- NOT scaled by fabric state (see docstring)
arbitrage_gbp_per_year_full = (800 + 950) / 2  # GBP 875 -- the figure to scale by spare capacity

# Battery-only capex, from check_combined_capex_hypothesis.py (this project's
# own existing figures, kept consistent rather than re-derived from the new
# market-guide cost figures found in this check's research, which quote
# higher installed-cost numbers from different sources -- a full re-check of
# battery capex itself is out of scope here).
battery_capex_gbp = {
    "baseline": 5_500,   # 10kWh-class
    "swi_only": 5_500,   # still needs 10kWh-class (82% consumed)
    "epc_c": 3_250,      # 5kWh-class fits comfort need, but see Rung-3 note below
}
# For the Rung-3 question specifically (a VPP funding a battery IN AN EPC-C
# HOME to capture spare capacity), the relevant capex is the 10kWh-class unit
# even in an EPC-C home, since downsizing to 5kWh-class would remove the
# spare capacity a VPP is funding it to capture. Use the 10kWh cost for that
# scenario explicitly, not the comfort-only 5kWh figure.
vpp_funded_battery_capex_gbp = 5_500

# ── 2. Headroom-scaled revenue by fabric state ───────────────────────────────

scaled_revenue_gbp_per_year = {
    state: dispatch_gbp_per_year + arbitrage_gbp_per_year_full * capacity_spare_pct[state]
    for state in capacity_spare_pct
}

flat_revenue_gbp_per_year = 1_075  # the existing flat figure used throughout Finding 6 / notebook 05

# ── 3. Rung-3 re-test: VPP funds the 10kWh battery in an EPC-C home ─────────

payback_years_flat = vpp_funded_battery_capex_gbp / flat_revenue_gbp_per_year
payback_years_scaled = {
    state: vpp_funded_battery_capex_gbp / scaled_revenue_gbp_per_year[state]
    for state in scaled_revenue_gbp_per_year
}

# Battery life -- sourced 17 Aug 2026, replacing the earlier unsourced 15-year
# guess, on the same footing Finding 8 replaced an unsourced 40-year fabric-
# life guess with the cited 36-year Ofgem figure. Three tiers, not blended:
#
# GROUNDED, peer-reviewed: Beltran, Ayuso & Perez (2020), "Lifetime Expectancy
# of Li-Ion Batteries used for Residential Solar Storage", Energies 13(3),
# 568, DOI 10.3390/en13030568 -- semi-empirical ageing models run against real
# PV production and consumption profiles at multiple locations. Finds 7.44-
# 18.37 years to a 60% remaining-capacity threshold. This is a WIDE range
# because it reflects real climate/usage-profile variation, not imprecision.
#
# PROVISIONAL, industry-standard, corroborating: Aurora Solar (installer-
# education tier, same as this project's other installer-guide citations) --
# most LFP home batteries carry 10-15yr warranties, guaranteeing 70-80%
# capacity retention, "generally expected to last 15 years or more" in
# practice. Cross-checked against Solar Insure's 6,000-10,000-cycle premium-
# LFP figure: at this project's own ~1.5 cycles/day arbitrage rate (Predbat
# documentation, cited above), that's ~11.0-18.3 years to 70-80% capacity --
# a different capacity threshold than Beltran's 60%, but landing in a
# consistent order of magnitude, which is reassuring rather than proof of
# either being more "right".
#
# NAMED BUT NOT USED, single-vendor outlier: Kight PowerHub, a genuinely new
# (2026) Scottish-manufactured domestic battery, claims a 25-year warranty
# and 20,000-cycle life on a chemistry "not utilised in production domestic
# batteries before" (Best Magazine, kightpowerhub.co.uk). The specific claim
# is real, not marketing fluff -- but it is a single vendor's own forward
# warranty commitment on a product with no long-run field track record yet
# (first UK domestic installation only recently reported), and it sits well
# above every other source here. Treated as a real upper-bound data point
# worth naming, not as this check's base case -- using an unproven outlier
# as the anchor would repeat the exact mistake this project has corrected
# elsewhere (accepting a vendor superlative at face value).
#
# EXCLUDED, category mismatch: Kight's own off-grid commercial LIGHTING
# division separately cites a 20-year cell life (kightoffgrid.com) -- but
# that's a different product on a different duty cycle (one shallow nightly
# discharge for street/construction lighting) from a home battery doing ~1.5
# deep arbitrage cycles a day. Not a valid comparator, the same category-error
# this project has already flagged elsewhere (e.g. not using the blended
# national £6,335 retrofit figure for this specific archetype, Finding 5).
BATTERY_LIFE_YEARS = {
    "low_grounded": 7.44,      # Beltran et al., pessimistic end (60% capacity threshold)
    "central": 15,             # Aurora Solar / Solar Insure cycle cross-check, PROVISIONAL
    "high_grounded": 18.37,    # Beltran et al., optimistic end (60% capacity threshold)
}

# Rung 4: DNO local-constraint flexibility -- sourced 17 Aug 2026, closing the
# one open question flagged since this ladder started. Deliberately kept
# SEPARATE from Rung 2's "dispatch" component (Axle's ~GBP1/kWh frequency-
# response rate) -- that's a NATIONAL NESO/balancing product (Demand
# Flexibility Service and equivalent), open to any battery anywhere. DNO
# local flex is a genuinely different, LOCATION-GATED market: each of GB's 6
# DNOs procures flexibility only where a specific feeder or substation is
# actually constrained (Axle Energy, "Local Network (DNO) Flexibility",
# GROUNDED).
#
# Three facts do almost all the work here, and the first is the one that
# matters most:
#
# 1. Only ~20% of GB households sit inside an active constraint zone at all
#    (Axle Energy). This project has already flagged, twice, that it cannot
#    show whether this archetype's specific streets coincide with a real DNO
#    constraint (Finding 3/4) -- so DNO_ACCESS_FRACTION below is applied as
#    an availability filter, not a probability this project has verified for
#    its own archetype specifically.
# 2. Where flex IS procurable, average revenue across all 6 DNOs was ~GBP33
#    per kW of flex per year in 2023-24 (Axle Energy) -- "kW of flex" meaning
#    variation from a metered baseline, not nameplate inverter rating.
#    Ceiling prices vary up to 100x by DNO/product/competition; GBP33/kW/yr
#    is a real average, not a promised rate.
# 3. Minimum bid size is 10-50kW per local competition -- well above a single
#    home's battery. A single HA property CANNOT participate alone; this only
#    works if enough retrofitted, battery-equipped homes on the SAME local
#    feeder are aggregated together (via a Flexibility Service Provider) to
#    clear the threshold. Not quantified here -- how many units that takes
#    depends on real feeder-level clustering data this project doesn't have.
DNO_ACCESS_FRACTION = 0.20          # Axle Energy: share of GB homes in an active constraint zone
DNO_RATE_GBP_PER_KW_YEAR = 33       # Axle Energy: 2023-24 average across all 6 DNOs
BATTERY_INDICATIVE_POWER_KW = 5.0   # PROVISIONAL: common inverter size for a 10kWh-class product;
                                     # no product-specific citation for the exact unit modelled elsewhere
                                     # in this project -- Finding 6's own cited range is 3.6-11.5kW

# ── Carbon check, 17 Aug 2026 -- two separate questions, not blended ────────
#
# (a) Is Finding 7's average-grid factor (0.131 kgCO2e/kWh, "DESNZ 2026")
#     still current? DESNZ published the 2026 GHG Conversion Factors on 11
#     June 2026 (updated 31 July 2026 for an unrelated flat-file correction),
#     cutting the UK electricity factor by ~26% via a revised methodology
#     that reduces reporting lag from two years to one (gov.uk; Circular
#     Ecology, GROUNDED on the fact of the change and its size). Three
#     independent mentions converge on ~131-141 gCO2e/kWh as the resulting
#     2026 figure, consistent with Finding 7's existing number. One
#     secondary aggregator (ecohedge.com) states 0.207 kg/kWh instead --
#     this project could not access the primary DESNZ spreadsheet (binary
#     file, not fetchable as text) to resolve the conflict with certainty.
#     Treated here as UNRESOLVED, not silently ignored -- Finding 7's figure
#     is very likely still correct (majority of sources agree, and it's
#     consistent with the ~26%-cut framing applied to a plausible ~0.177
#     prior-year figure) but this project cannot claim 100% verification.
#
# (b) NEW, separate question: does the battery's OWN arbitrage/dispatch
#     cycling -- charge cheap/off-peak, discharge expensive/peak -- carry
#     its own carbon value, on top of fabric's heating-carbon savings
#     (Finding 7)? This is the carbon dimension of revenue ALREADY priced in
#     GBP terms above (section 1) -- same physical dispatch activity, a
#     different unit, not new energy to double-count.
AVERAGE_GRID_FACTOR_KGCO2E_PER_KWH = 0.131   # Finding 7, DESNZ 2026 (see caveat above)
# Finding 7's own marginal (CCGT-typical proxy) figure is not restated as a
# standalone citation anywhere this project still holds in full -- back-
# derived here from Finding 7's own published output (2.7-3.0 tCO2e/yr from
# 7,600 kWh/yr displaced) for internal consistency rather than introducing a
# second, differently-sourced marginal factor: 2,700-3,000 kg / 7,600 kWh =
# 0.355-0.395 kgCO2e/kWh, midpoint ~0.375. Cross-checked, not replaced, by
# this session's own research: gas-dominated marginal generation "on the
# order of 400-600 gCO2eq/kWh" (general literature, not UK-2026-dated) --
# same order of magnitude, corroborating rather than overriding.
MARGINAL_GRID_FACTOR_KGCO2E_PER_KWH = 0.375  # midpoint of Finding 7's own back-derived 0.355-0.395 range
CYCLES_PER_DAY = 1.5  # same reused assumption as Rung 4's DNO-revenue framing, Predbat documentation

if __name__ == "__main__":
    print("=" * 78)
    print("1. Headroom-scaled revenue by fabric state (vs the existing flat GBP1,075 figure)")
    print("=" * 78)
    for state in ("baseline", "swi_only", "epc_c"):
        print(f"  {state:>10}: spare capacity {capacity_spare_pct[state]*100:4.0f}%  ->  "
              f"GBP{dispatch_gbp_per_year:.0f} dispatch (unscaled) + "
              f"GBP{arbitrage_gbp_per_year_full * capacity_spare_pct[state]:.0f} arbitrage (scaled) = "
              f"GBP{scaled_revenue_gbp_per_year[state]:.0f}/yr")
    print(f"  Flat estimate used elsewhere in this project: GBP{flat_revenue_gbp_per_year:,}/yr for ALL states")
    print(f"  -> the flat figure overstates baseline by "
          f"{flat_revenue_gbp_per_year/scaled_revenue_gbp_per_year['baseline']:.1f}x, "
          f"SWI-only by {flat_revenue_gbp_per_year/scaled_revenue_gbp_per_year['swi_only']:.1f}x, "
          f"and roughly matches EPC-C (understates by "
          f"{flat_revenue_gbp_per_year/scaled_revenue_gbp_per_year['epc_c']:.2f}x)")

    print("\n" + "=" * 78)
    print("2. Rung 3 re-test: VPP funds a 10kWh battery (GBP5,500) for dispatch rights")
    print("=" * 78)
    print(f"  Naive flat-revenue payback (used two turns ago): {payback_years_flat:.1f} years")
    for state in ("baseline", "swi_only", "epc_c"):
        print(f"  Headroom-scaled payback if installed in a {state:>10} home: "
              f"{payback_years_scaled[state]:.1f} years")
    print(f"\n  The EPC-C case: {payback_years_scaled['epc_c']:.1f} years payback (vs {payback_years_flat:.1f} "
          f"years naive) -- still solidly economic, just more honestly stated.")
    print(f"  The baseline case: {payback_years_scaled['baseline']:.1f} years -- confirms, with a real number "
          f"now rather than an assertion, why a VPP has no commercial reason to fund a battery")
    print(f"  ahead of fabric retrofit. This is the quantified version of the sequencing")
    print(f"  argument (fabric must come before VPP-funded battery), not just a restated assumption.")

    print("\n" + "=" * 78)
    print("3. Lifetime margin, EPC-C case, SOURCED battery-life range (17 Aug 2026 update)")
    print("=" * 78)
    print(f"  {'life scenario':>16} {'years':>7} {'remaining':>10} {'margin':>12}")
    for label, years in BATTERY_LIFE_YEARS.items():
        remaining = years - payback_years_scaled["epc_c"]
        margin = remaining * scaled_revenue_gbp_per_year["epc_c"]
        print(f"  {label:>16} {years:7.2f} {remaining:9.2f}y  GBP{margin:>9,.0f}")

    low_remaining = BATTERY_LIFE_YEARS["low_grounded"] - payback_years_scaled["epc_c"]
    low_margin = low_remaining * scaled_revenue_gbp_per_year["epc_c"]
    high_remaining = BATTERY_LIFE_YEARS["high_grounded"] - payback_years_scaled["epc_c"]
    high_margin = high_remaining * scaled_revenue_gbp_per_year["epc_c"]

    print(f"\n  This is a WIDE range, and that's the honest finding, not noise to average away:")
    print(f"  at the pessimistic (GROUNDED, peer-reviewed) end of the battery-life range, the")
    print(f"  margin is only GBP{low_margin:,.0f} -- barely profitable, not the comfortable case")
    print(f"  the central 15-year estimate implies. At the optimistic end it's GBP{high_margin:,.0f}.")
    print(f"  The earlier claim (2 turns ago) that this is 'still clearly profitable' only holds")
    print(f"  at the central-to-optimistic end of a real, sourced range -- it does not hold robustly")
    print(f"  across the full peer-reviewed uncertainty band.")
    print(f"\n  Named but NOT used as a base case: Kight PowerHub's own claimed 25yr/20,000-cycle")
    print(f"  warranty (a genuine, specific claim, not marketing fluff -- but a single vendor's")
    print(f"  forward warranty commitment on a brand-new product with no long-run field track")
    print(f"  record yet). Using it as the anchor would repeat the exact mistake this project has")
    print(f"  corrected elsewhere: accepting a vendor superlative at face value.")
    print(f"\n  EXCLUDED as a category mismatch: Kight's own off-grid LIGHTING division's 20-year")
    print(f"  cell-life figure -- a different product on a shallow single-nightly-discharge duty")
    print(f"  cycle, not comparable to a home battery doing ~1.5 deep arbitrage cycles a day.")
    print(f"\n  STILL NOT MODELLED: this treats revenue as flat until a cliff-edge end of life --")
    print(f"  real degradation is gradual, and arbitrage revenue should decline smoothly as")
    print(f"  capacity fades, not hold at GBP{scaled_revenue_gbp_per_year['epc_c']:.0f}/yr right up to the battery-life cutoff.")
    print(f"  A declining-revenue curve would be a further, real refinement, not yet done here.")

    print("\n" + "=" * 78)
    print("4. Value left on the table: the 'silent default' scenario (17 Aug 2026 addition)")
    print("=" * 78)
    print(f"  A vertically-integrated installer+VPP can sell the battery on comfort/EPC")
    print(f"  compliance/asset-protection grounds alone (Finding 6) -- all real, all sufficient")
    print(f"  to justify the purchase -- then privately enrol it in their own aggregator arm")
    print(f"  and keep 100% of dispatch/arbitrage revenue, with nothing about the sale ever")
    print(f"  requiring that to be disclosed or shared. Three scenarios, same GBP5,500 battery:")
    print(f"\n  Scenario A, uninformed default: HA pays full capex, vendor's own VPP keeps the")
    print(f"    revenue. HA's return on the battery's flexibility value: GBP0.")
    print(f"  Scenario B, Rung 3 (VPP funds it): HA pays GBP0 capex, VPP keeps the revenue as")
    print(f"    its return for funding the asset. HA's net cash position: GBP0.")
    print(f"  Scenario C, HA negotiates to keep the revenue: HA pays full capex (same as A),")
    print(f"    but captures the flexibility revenue itself (via an independent aggregator or")
    print(f"    an explicit revenue-share term). HA's return: the full headroom-scaled revenue.")
    print(f"\n  Scenario A is strictly worse than B for an identical revenue outcome (GBP0 either")
    print(f"  way) -- in A the HA also pays the GBP{vpp_funded_battery_capex_gbp:,} capex B avoids entirely.")
    print(f"  That gap alone is pure downside from not asking, before any revenue is even counted.")

    print(f"\n  {'fabric state':>10} {'yr revenue':>11} {'@7.44y life':>13} {'@15y life':>12} {'@18.37y life':>13}")
    for state in ("baseline", "swi_only", "epc_c"):
        rev = scaled_revenue_gbp_per_year[state]
        low_v = rev * BATTERY_LIFE_YEARS["low_grounded"]
        mid_v = rev * BATTERY_LIFE_YEARS["central"]
        high_v = rev * BATTERY_LIFE_YEARS["high_grounded"]
        print(f"  {state:>10} GBP{rev:>7,.0f}  GBP{low_v:>10,.0f}  GBP{mid_v:>9,.0f}  GBP{high_v:>10,.0f}")

    epc_c_mid = scaled_revenue_gbp_per_year["epc_c"] * BATTERY_LIFE_YEARS["central"]
    total_vs_c = vpp_funded_battery_capex_gbp + epc_c_mid
    print(f"\n  Headline, EPC-C stock, central 15-year life: not asking costs an HA up to")
    print(f"  GBP{epc_c_mid:,.0f} in forgone lifetime flexibility revenue (Scenario A vs C), on top of the")
    print(f"  GBP{vpp_funded_battery_capex_gbp:,} they'd have avoided paying under Scenario B. Combined worst-case gap")
    print(f"  between the uninformed default and the best available structure: GBP{total_vs_c:,.0f}.")
    print(f"  This is undiscounted, and inherits every caveat from section 3 above (flat, not")
    print(f"  declining, revenue; a sourced but still wide battery-life range) -- a real order-of-")
    print(f"  magnitude figure to negotiate against, not a number to quote as precise.")

    print("\n" + "=" * 78)
    print("5. Rung 4 CLOSED: DNO local-constraint flexibility (17 Aug 2026)")
    print("=" * 78)
    dno_revenue_if_eligible = DNO_RATE_GBP_PER_KW_YEAR * BATTERY_INDICATIVE_POWER_KW
    print(f"  DNO local flex is a SEPARATE market from Rung 2's dispatch component -- national")
    print(f"  NESO/frequency-response products (Axle's ~GBP1/kWh) are open to any battery anywhere;")
    print(f"  DNO local flex only exists where a specific feeder is actually constrained.")
    print(f"\n  Fact 1 -- access is the gate, not price: only {DNO_ACCESS_FRACTION*100:.0f}% of GB households sit inside")
    print(f"  an active constraint zone at all (Axle Energy). This project has twice flagged (Finding")
    print(f"  3/4) that it cannot show whether this archetype's own streets coincide with a real")
    print(f"  constraint -- so treat eligibility as unverified for this specific archetype, not just")
    print(f"  a probability to multiply through.")
    print(f"\n  Fact 2 -- if eligible, illustrative revenue: GBP{DNO_RATE_GBP_PER_KW_YEAR}/kW/yr average across all 6 DNOs")
    print(f"  (2023-24, Axle Energy) x {BATTERY_INDICATIVE_POWER_KW:.1f}kW indicative inverter size (PROVISIONAL, no product-")
    print(f"  specific citation) = GBP{dno_revenue_if_eligible:.0f}/yr -- real ceiling prices vary up to 100x by DNO,")
    print(f"  product and competition, so this is an average, not a quoted rate.")
    print(f"  For comparison, EPC-C arbitrage+dispatch revenue (Rung 2) is GBP{scaled_revenue_gbp_per_year['epc_c']:.0f}/yr --")
    print(f"  DNO flex would add roughly {dno_revenue_if_eligible/scaled_revenue_gbp_per_year['epc_c']*100:.0f}% on top, where it's even available. Real,")
    print(f"  but modest next to arbitrage -- not the transformative third leg it might have sounded")
    print(f"  like when this was first raised.")
    print(f"\n  Fact 3 -- structural precondition, not just pricing: minimum bid size is 10-50kW per")
    print(f"  local competition, well above one home's battery. A single HA property cannot")
    print(f"  participate alone -- this only works if enough retrofitted, battery-equipped homes on")
    print(f"  the SAME local feeder are aggregated together. How many units that takes isn't")
    print(f"  quantified here; it depends on real feeder-level clustering data this project doesn't have.")
    print(f"\n  NOT resolved: the most common DNO product (Sustain) is a seasonal, scheduled")
    print(f"  commitment for a defined time of day -- often the same evening peak Rung 2's arbitrage")
    print(f"  already targets. Whether a Sustain contract would displace arbitrage revenue on")
    print(f"  contracted days, rather than stack cleanly on top of it, is a real open question this")
    print(f"  check has not modelled -- flagged, not netted off, because inventing a netting factor")
    print(f"  without real overlap data would be less honest than leaving it as a named gap.")
    print(f"\n  CLOSING STATEMENT: Rung 4 is no longer unmodelled. The honest finding is that DNO")
    print(f"  co-funding is real but narrow -- available to roughly a fifth of stock at best, worth")
    print(f"  a real but modest uplift where it exists, and gated by an aggregation threshold no")
    print(f"  single property can clear alone. It's a genuine 'sometimes, modestly, with help'")
    print(f"  answer, not the clean third leg the original framing implied.")

    print("\n" + "=" * 78)
    print("6. Carbon check (17 Aug 2026): DESNZ figure verification + battery-dispatch carbon")
    print("=" * 78)
    print(f"  (a) Finding 7's {AVERAGE_GRID_FACTOR_KGCO2E_PER_KWH} kgCO2e/kWh average-grid figure: UNRESOLVED, not silently")
    print(f"  assumed fine. DESNZ published 2026 GHG Conversion Factors 11 Jun 2026, cutting the UK")
    print(f"  electricity factor ~26% via reduced reporting lag (GROUNDED, gov.uk + Circular Ecology).")
    print(f"  Three sources converge near 131-141 gCO2e/kWh, consistent with Finding 7's figure; one")
    print(f"  aggregator states 0.207 kg/kWh instead. Primary DESNZ spreadsheet not accessible via")
    print(f"  fetch (binary file) to resolve with certainty -- majority evidence supports the existing")
    print(f"  figure, but this is a flagged conflict, not a clean confirmation.")

    print(f"\n  (b) NEW: carbon value of the battery's OWN arbitrage cycling, on top of Finding 7's")
    print(f"  heating-carbon savings -- the carbon dimension of section 1's GBP figures, not new energy.")
    net_carbon_diff = MARGINAL_GRID_FACTOR_KGCO2E_PER_KWH - AVERAGE_GRID_FACTOR_KGCO2E_PER_KWH
    print(f"  Net differential (marginal peak avoided - average off-peak charged): "
          f"{MARGINAL_GRID_FACTOR_KGCO2E_PER_KWH:.3f} - {AVERAGE_GRID_FACTOR_KGCO2E_PER_KWH:.3f} = {net_carbon_diff:.3f} kgCO2e/kWh cycled")
    print(f"\n  {'fabric state':>10} {'kWh cycled/yr':>14} {'tCO2e/yr avoided':>17}")
    dispatch_carbon_tco2e = {}
    for state in ("baseline", "swi_only", "epc_c"):
        kwh_cycled = 10 * CYCLES_PER_DAY * 365 * capacity_spare_pct[state]
        tco2e = kwh_cycled * net_carbon_diff / 1000
        dispatch_carbon_tco2e[state] = tco2e
        print(f"  {state:>10} {kwh_cycled:>13,.0f}  {tco2e:>16.3f}")
    print(f"\n  Striking result: EPC-C's dispatch-carbon saving ({dispatch_carbon_tco2e['epc_c']:.2f} tCO2e/yr) is")
    print(f"  roughly as large as Finding 7's own average-basis HEATING carbon saving (1.0 tCO2e/yr) --")
    print(f"  a genuine, additive carbon benefit from the battery's own cycling that nothing in this")
    print(f"  project has counted before now.")
    print(f"\n  CAVEATS, named not hidden: uses Finding 7's own back-derived marginal factor for internal")
    print(f"  consistency rather than a freshly-sourced one; treats AVERAGE grid intensity as a proxy")
    print(f"  for off-peak charging emissions specifically, not a real time-of-day factor (no such")
    print(f"  UK series was sourced for this check); reuses the same 1.5-cycles/day assumption as")
    print(f"  Rung 4's revenue framing rather than a separately-verified cycling rate. PROVISIONAL/")
    print(f"  REASONED throughout -- a real, order-of-magnitude finding worth stating, not a checked")
    print(f"  number on the same footing as Finding 7's own peer-reviewed-adjacent carbon figures.")
