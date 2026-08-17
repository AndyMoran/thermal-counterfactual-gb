"""
check_combined_capex_hypothesis.py

Checks the reader-proposed hypothesis flagged in linkedin_article_business_case.md
("fabric-first sequencing cuts combined BESS+heat pump CapEx by ~40%, fitting
Housing Association deals under grant caps") against real data, rather than
leaving it as an unquantified idea. Three components, three different
confidence levels -- reported separately, not blended into one false-precision
number.

1. Heat pump right-sizing: GROUNDED physics (this project's own H and
   heat_loss_coefficient_w_per_k), PROVISIONAL costing (no official size-banded
   cost table found; triangulated from multiple 2026 UK installer/aggregator
   surveys, materially less rigorous than the rest of this project's sourcing
   standard -- flagged as such throughout).
2. Battery right-sizing: GROUNDED physics (Finding 6's already-published 98%
   vs 26% result), PROVISIONAL costing (multiple independent 2026 UK market
   surveys for discrete 5kWh/10kWh tiers, same evidentiary tier as this
   project's existing battery-cost citation).
3. Grant caps: GROUNDED (Boiler Upgrade Scheme, gov.uk/Ofgem; Warm Homes:
   Social Housing Fund Wave 3 cost caps, cross-checked against a specialist
   audit/assurance advisory source working directly on WHSHF Wave 3
   compliance) -- the most solid part of this check.
"""

# ── 1. Heat pump right-sizing (physics: GROUNDED; costing: PROVISIONAL) ─────

# From physics.py / configs/tenure_insulation_assumptions.yml, reproduced
# directly (see FINDINGS.md Finding 1 for the electrical-demand figures this
# matches exactly): thermal load = electrical demand x COP.
baseline_thermal_kw = 6.15
epc_c_thermal_kw = 1.65

# UK domestic ASHP costs by size band: NOT a single official table (the DESNZ/
# Nesta size-vs-cost breakdown exists as a chart image, not machine-readable
# data this project could fetch). Triangulated from multiple 2026 UK installer
# surveys instead -- deliberately wide ranges, flagged PROVISIONAL, not treated
# as precise. Baseline's 6.15kW need sits in the common "6-8kW, 3-bed" band;
# EPC-C's 1.65kW need is below any commercially available unit, so it has to
# buy the smallest practical tier (4-6kW), not a unit sized to its true load --
# a real ceiling on how much the heat pump side of this hypothesis can save.
baseline_ashp_cost_gbp = 10_500   # midpoint of "6-8kW: GBP9,000-12,000" (pre-grant)
epc_c_ashp_cost_gbp = 7_500       # midpoint of "4-6kW" pre-grant estimates across sources (wide: ~6,000-9,000)

ashp_saving_pct = (baseline_ashp_cost_gbp - epc_c_ashp_cost_gbp) / baseline_ashp_cost_gbp * 100

# ── 2. Battery right-sizing (physics: GROUNDED, Finding 6; costing: PROVISIONAL) ──

# Finding 6: baseline needs 9.84kWh (98% of a 10kWh nameplate battery) to cover
# the peak window; EPC-C needs 2.64kWh (26%). Real product tiers: baseline's
# need rounds up to a 10kWh-class product; EPC-C's fits inside the smallest
# common 5kWh-class tier.
baseline_battery_kwh_needed = 9.84
epc_c_battery_kwh_needed = 2.64

# Multiple independent 2026 UK market surveys, same evidentiary tier as this
# project's existing "UK domestic battery installed cost range" citation.
baseline_battery_cost_gbp = 5_500   # midpoint of 10kWh: GBP4,000-6,500 / GBP4,500-7,000 across sources
epc_c_battery_cost_gbp = 3_250      # midpoint of 5kWh: GBP2,500-4,000

battery_saving_pct = (baseline_battery_cost_gbp - epc_c_battery_cost_gbp) / baseline_battery_cost_gbp * 100

# ── 3. Combined CapEx reduction (weighted, not a simple average of the two %s) ──

baseline_combined_gbp = baseline_ashp_cost_gbp + baseline_battery_cost_gbp
epc_c_combined_gbp = epc_c_ashp_cost_gbp + epc_c_battery_cost_gbp
combined_saving_pct = (baseline_combined_gbp - epc_c_combined_gbp) / baseline_combined_gbp * 100

# ── 4. Grant-cap mechanics (GROUNDED) ────────────────────────────────────────

bus_grant_gbp = 7_500  # flat, regardless of ASHP size -- gov.uk/Ofgem BUS terms
whshf_base_cap_gbp = 7_500       # per home, any measure, 50:50 match funding, "any starting EPC band or wall type"
whshf_off_gas_uplift_gbp = 7_500  # additional, for off-gas-grid low-carbon heating
whshf_on_gas_cap_gbp = 20_000     # for up to 10% of homes in an application, on-gas-grid low-carbon heating

if __name__ == "__main__":
    print("=" * 78)
    print("1. Heat pump right-sizing (costing PROVISIONAL -- no official size-banded table)")
    print("=" * 78)
    print(f"  Required thermal output: baseline {baseline_thermal_kw}kW -> EPC-C {epc_c_thermal_kw}kW "
          f"({(1 - epc_c_thermal_kw/baseline_thermal_kw)*100:.0f}% less thermal load)")
    print(f"  But EPC-C's true need is below any commercially available domestic ASHP --")
    print(f"  it has to buy the smallest practical tier (4-6kW), not a unit sized to 1.65kW.")
    print(f"  Estimated pre-grant cost: baseline GBP{baseline_ashp_cost_gbp:,} -> EPC-C GBP{epc_c_ashp_cost_gbp:,} "
          f"({ashp_saving_pct:.0f}% lower)")
    print(f"  -- a real saving, but far smaller than the thermal-load ratio alone would suggest,")
    print(f"     because of the practical minimum-unit-size floor.")

    print("\n" + "=" * 78)
    print("2. Battery right-sizing (costing PROVISIONAL, same tier as existing project citation)")
    print("=" * 78)
    print(f"  Energy needed: baseline {baseline_battery_kwh_needed}kWh -> EPC-C {epc_c_battery_kwh_needed}kWh (Finding 6)")
    print(f"  Real product tier: baseline needs 10kWh-class, EPC-C fits a 5kWh-class product")
    print(f"  Estimated pre-grant cost: baseline GBP{baseline_battery_cost_gbp:,} -> EPC-C GBP{epc_c_battery_cost_gbp:,} "
          f"({battery_saving_pct:.0f}% lower)")

    print("\n" + "=" * 78)
    print("3. Combined CapEx (weighted by each component's own cost, not a simple average)")
    print("=" * 78)
    print(f"  Baseline combined: GBP{baseline_combined_gbp:,}  (ASHP GBP{baseline_ashp_cost_gbp:,} + battery GBP{baseline_battery_cost_gbp:,})")
    print(f"  EPC-C combined:    GBP{epc_c_combined_gbp:,}  (ASHP GBP{epc_c_ashp_cost_gbp:,} + battery GBP{epc_c_battery_cost_gbp:,})")
    print(f"  Combined reduction: {combined_saving_pct:.0f}%")
    print(f"  The original hypothesis said ~40%. This check lands in a plausible but wider")
    print(f"  range around it -- the battery component alone is close to 40% and well-evidenced;")
    print(f"  the heat pump component is real but smaller and much less precisely costed.")

    print("\n" + "=" * 78)
    print("4. Grant-cap fit (GROUNDED)")
    print("=" * 78)
    print(f"  BUS grant for the ASHP: flat GBP{bus_grant_gbp:,} regardless of unit size.")
    print(f"  -> covers {bus_grant_gbp/baseline_ashp_cost_gbp*100:.0f}% of baseline's ASHP cost, "
          f"but {bus_grant_gbp/epc_c_ashp_cost_gbp*100:.0f}% of EPC-C's smaller unit's cost.")
    print(f"  WHSHF Wave 3 (social housing only): GBP{whshf_base_cap_gbp:,}/home base cap (any measure, 50:50 match),")
    print(f"  +GBP{whshf_off_gas_uplift_gbp:,} off-gas-grid heating uplift, or up to GBP{whshf_on_gas_cap_gbp:,} on-gas-grid")
    print(f"  heating for a 10%-of-application quota.")
    print(f"  This project's own fabric cost (GBP10,728) exceeds the GBP{whshf_base_cap_gbp:,} base cap alone --")
    print(f"  at 50:50 match, the achievable base grant is min(cap, 50% of actual cost) = "
          f"GBP{min(whshf_base_cap_gbp, 10_728*0.5):,.0f}, not the full cap.")
    print(f"  IMPORTANT SEQUENCING POINT: WHSHF Wave 3's core scope is EPC bands D-G. A home")
    print(f"  already retrofitted to EPC-C is only eligible for further funding under the")
    print(f"  10%-quota/infill route -- so heat pump + fabric should be bundled into ONE")
    print(f"  application while the home is still D-G, not sequenced as separate funding rounds.")
