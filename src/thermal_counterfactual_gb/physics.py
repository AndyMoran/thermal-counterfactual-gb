"""Core RC thermal-model physics for the pre-1919 solid-wall mid-terrace archetype.

Every function here is small, has a clear contract, and asserts its physical
boundaries — PROJECT.md Section 5 (NASA/JPL-inspired coding standards).

Implementation is Week 1 work (see notebooks/01_archetype_physics.ipynb and
PROJECT.md Section 8.3 for the derivation and the values these functions must
reproduce). This module exists so notebooks import shared, testable logic
instead of duplicating it — and so a bug gets fixed in one place, not four.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class EnvelopeState:
    """One envelope state (baseline / swi_only / epc_c_package).

    All U-values in W/m2K, matching configs/tenure_insulation_assumptions.yml.
    """

    wall_u_w_per_m2k: float
    roof_u_w_per_m2k: float
    floor_u_w_per_m2k: float
    window_u_w_per_m2k: float
    infiltration_ach: float


def heat_loss_coefficient_w_per_k(
    state: EnvelopeState,
    wall_area_m2: float,
    roof_area_m2: float,
    floor_area_m2: float,
    window_area_m2: float,
    heated_volume_m3: float,
) -> float:
    """Total fabric + ventilation heat loss coefficient, H, in W/K.

    H = sum(area_i * U_i) + 0.33 * ACH * volume

    The 0.33 W/m3K constant is the standard specific heat capacity of air
    per unit volume flow (CIBSE/SAP convention: rho * cp / 3600 ~= 0.33).
    """
    for area in (wall_area_m2, roof_area_m2, floor_area_m2, window_area_m2, heated_volume_m3):
        assert area > 0, "areas and volume must be positive"

    h = (
        wall_area_m2 * state.wall_u_w_per_m2k
        + roof_area_m2 * state.roof_u_w_per_m2k
        + floor_area_m2 * state.floor_u_w_per_m2k
        + window_area_m2 * state.window_u_w_per_m2k
        + 0.33 * state.infiltration_ach * heated_volume_m3
    )
    assert h > 0, "H must be positive"
    return h


def thermal_time_constant_hours(c_kwh_per_k: float, h_w_per_k: float) -> float:
    """tau = C / H, converted to hours.

    C in kWh/K, H in W/K. Multiplying C by 1000 converts kWh/K to Wh/K so
    the units cancel cleanly against H in W/K, leaving hours.
    """
    assert c_kwh_per_k > 0, "thermal capacity must be positive"
    assert h_w_per_k > 0, "H must be positive"
    return (c_kwh_per_k * 1000) / h_w_per_k


def effective_outdoor_temp_c(
    t_outdoor_c: float,
    h_w_per_k: float,
    internal_gains_w: float = 0.0,
) -> float:
    """Outdoor temperature that produces the same net heat loss as the real
    outdoor temperature does once constant internal gains are netted off.

    Constant internal gains (occupants, appliances, cooking, lighting) are a
    heat SOURCE inside the building, not a change to the fabric/ventilation
    loss coefficient H — so they don't belong inside heat_loss_coefficient_w_per_k
    (PROJECT.md Section 2.3, no double-counting between the physics and a
    derating/offset applied on top of it). Instead, a constant gain Q shifts
    the equilibrium the building coasts towards: solving
        C dT/dt = -H(T - T_out) + Q
    is algebraically identical to plain Newton cooling with T_out replaced by
        T_out_eff = T_out + Q / H
    which is what this function returns. Every gains-aware function in this
    module is built on this single substitution, so the "no double-counting"
    check lives in one place.
    """
    assert h_w_per_k > 0, "H must be positive"
    return t_outdoor_c + internal_gains_w / h_w_per_k


def coastdown_hours(
    tau_hours: float,
    t_start_c: float,
    t_min_c: float,
    t_outdoor_c: float,
    h_w_per_k: float | None = None,
    internal_gains_w: float = 0.0,
) -> float:
    """Time to coast from t_start_c down to t_min_c, given outdoor t_outdoor_c.

    Newton's law of cooling (exponential decay), not a linear approximation:
        t = tau * ln((T_start - T_out) / (T_min - T_out))

    internal_gains_w (default 0, i.e. unchanged behaviour): constant internal
    heat gains (occupants/appliances/cooking) shift the effective outdoor
    temperature the building coasts towards (effective_outdoor_temp_c above).
    h_w_per_k is REQUIRED whenever internal_gains_w is nonzero, since tau
    alone (C/H) doesn't let H be recovered separately.

    If gains alone would hold the building above t_min_c forever (the
    building's free-running equilibrium temperature is at or above the
    comfort floor even with no heating), this returns math.inf rather than
    raising — a real, physically meaningful result worth surfacing, not an
    error to hide.
    """
    assert tau_hours > 0, "tau must be positive"
    assert t_start_c > t_min_c, "expected t_start_c > t_min_c — check comfort band inputs"

    t_outdoor_eff_c = t_outdoor_c
    if internal_gains_w:
        assert h_w_per_k is not None and h_w_per_k > 0, (
            "h_w_per_k is required when internal_gains_w is nonzero"
        )
        t_outdoor_eff_c = effective_outdoor_temp_c(t_outdoor_c, h_w_per_k, internal_gains_w)

    if t_outdoor_eff_c >= t_min_c:
        return math.inf

    assert t_start_c > t_outdoor_eff_c, (
        "expected t_start_c above the (gains-adjusted) effective outdoor temperature"
    )
    return tau_hours * math.log((t_start_c - t_outdoor_eff_c) / (t_min_c - t_outdoor_eff_c))


def decay_one_hour(
    t_indoor_c: float,
    t_outdoor_c: float,
    tau_hours: float,
    dt_hours: float = 1.0,
    h_w_per_k: float | None = None,
    internal_gains_w: float = 0.0,
) -> float:
    """One discrete timestep of unheated Newton's-law-of-cooling decay.

    T(t + dt) = T_out + (T(t) - T_out) * exp(-dt / tau)

    This is the same physics as coastdown_hours(), inverted into a stepper
    so a control loop (preheat / curtail / resume) can be simulated hour by
    hour against a real, time-varying outdoor temperature series, rather
    than only solving the closed-form single continuous coastdown.

    internal_gains_w (default 0, unchanged behaviour): see
    effective_outdoor_temp_c — h_w_per_k is required whenever nonzero.
    """
    assert tau_hours > 0, "tau must be positive"
    if internal_gains_w:
        assert h_w_per_k is not None and h_w_per_k > 0, (
            "h_w_per_k is required when internal_gains_w is nonzero"
        )
        t_outdoor_c = effective_outdoor_temp_c(t_outdoor_c, h_w_per_k, internal_gains_w)
    return t_outdoor_c + (t_indoor_c - t_outdoor_c) * math.exp(-dt_hours / tau_hours)


def net_heating_power_kw(
    h_w_per_k: float,
    t_indoor_c: float,
    t_outdoor_c: float,
    cop: float,
    internal_gains_w: float = 0.0,
) -> float:
    """Electrical power to hold t_indoor_c against t_outdoor_c, net of
    constant internal gains, floored at zero.

    P_thermal_net = max(H * (T_indoor - T_outdoor) - Q_gains, 0)
    P_electrical  = P_thermal_net / COP

    Shared by every place in this project that computes a heating-power
    draw, so gains are netted off consistently everywhere power is computed
    — not just in the coasting/decay path (effective_outdoor_temp_c above).
    Floored at zero rather than asserting: for a well-retrofitted state, at
    a mild-enough outdoor temperature, gains alone can cover the whole load
    (zero heating demand) — a real, physically meaningful result worth
    surfacing, not an error to hide (PROJECT.md Section 2.7, Ambiguity Is
    Informative).
    """
    assert h_w_per_k > 0
    assert cop > 0, "COP must be positive"
    p_thermal_w = max(h_w_per_k * (t_indoor_c - t_outdoor_c) - internal_gains_w, 0.0)
    return (p_thermal_w / cop) / 1000


def simulate_vpp_control_hours(
    tau_hours: float,
    h_w_per_k: float,
    outdoor_temps_c,
    setpoint_c: float,
    preheat_c: float,
    minimum_c: float,
    cop: float,
    peak_start: int,
    peak_end: int,
    internal_gains_w: float = 0.0,
):
    """Hour-by-hour VPP control: preheat before the peak window, curtail
    during it, resume only if the comfort floor would otherwise be breached.

    Shared by notebooks/02 (single archetype) and notebooks/03 (estate
    population / stress test), so the control logic is defined once.
    Note: notebooks/02 currently carries its own inline copy of this same
    logic, predating this function -- worth consolidating in a future pass
    (PROJECT.md Section 2.7, ambiguity/technical debt should stay visible,
    not hidden).

    internal_gains_w (default 0, unchanged behaviour): constant internal
    gains extend the coasting decay (via decay_one_hour) AND reduce the
    heating power needed to hold a setpoint (via net_heating_power_kw) --
    both paths share the same effective_outdoor_temp_c substitution, so
    gains are netted off exactly once, consistently, not double-counted
    between the two.

    Returns (indoor_temps_c, heating_on, electrical_kw) as numpy arrays,
    matching notebooks/02's simulate_vpp.
    """
    import numpy as np

    assert tau_hours > 0
    assert h_w_per_k > 0
    assert cop > 0
    assert setpoint_c > minimum_c
    assert 0 <= peak_start < peak_end <= 24

    outdoor_temps_c = np.asarray(outdoor_temps_c, dtype=float)
    n = len(outdoor_temps_c)
    pre_peak_hour = (peak_start - 1) % 24

    indoor = np.zeros(n)
    heating_on = np.zeros(n, dtype=bool)
    electrical_kw = np.zeros(n)

    t_indoor = setpoint_c
    for i in range(n):
        hour_of_day = i % 24
        t_out = outdoor_temps_c[i]
        in_peak = peak_start <= hour_of_day < peak_end

        if not in_peak:
            target = preheat_c if hour_of_day == pre_peak_hour else setpoint_c
            t_indoor = target
            on = True
        else:
            candidate = decay_one_hour(
                t_indoor, t_out, tau_hours, h_w_per_k=h_w_per_k, internal_gains_w=internal_gains_w
            )
            if candidate >= minimum_c:
                t_indoor = candidate
                on = False
            else:
                t_indoor = minimum_c
                on = True

        indoor[i] = t_indoor
        heating_on[i] = on
        electrical_kw[i] = (
            net_heating_power_kw(h_w_per_k, t_indoor, t_out, cop, internal_gains_w) if on else 0.0
        )

    return indoor, heating_on, electrical_kw


def simulate_naive_heating_hours(
    h_w_per_k: float,
    outdoor_temps_c,
    setpoint_c: float,
    cop: float,
    internal_gains_w: float = 0.0,
):
    """Hour-by-hour naive/status-quo heating: hold setpoint continuously,
    no preheat, no curtailment. Returns (indoor_temps_c, electrical_kw).

    internal_gains_w (default 0, unchanged behaviour): see
    net_heating_power_kw.
    """
    import numpy as np

    assert h_w_per_k > 0
    assert cop > 0
    outdoor_temps_c = np.asarray(outdoor_temps_c, dtype=float)
    indoor = np.full(len(outdoor_temps_c), setpoint_c)
    electrical_kw = np.array([
        net_heating_power_kw(h_w_per_k, setpoint_c, t_out, cop, internal_gains_w)
        for t_out in outdoor_temps_c
    ])
    return indoor, electrical_kw


def two_node_conductances_w_per_k(
    state: EnvelopeState,
    wall_area_m2: float,
    roof_area_m2: float,
    floor_area_m2: float,
    window_area_m2: float,
    heated_volume_m3: float,
    r_si_wall_m2k_per_w: float = 0.13,
    r_si_roof_m2k_per_w: float = 0.10,
    r_si_floor_m2k_per_w: float = 0.17,
) -> tuple[float, float, float]:
    """Split the 1R1C heat loss coefficient into a 2-node (air / mass) network.

    Added in response to external review: a single-node model cannot show
    the air node cooling faster than the whole-building average implies,
    because it has no separate, small air capacitance to do so. This
    function derives a defensible 2R2C split WITHOUT double-counting
    against the 1R1C model (PROJECT.md Section 2.3, Physics/Derating
    Separation, applied here to a structural rather than economic split).

    Three loss paths:
      H_direct  — ventilation + windows. These bypass the thermal mass
                  entirely (window panes and infiltrating air have
                  negligible thermal mass of their own).
      H_im      — air-to-mass conductance, via the INTERNAL surface film
                  only (r_si), summed across wall/roof/floor.
      H_mo      — mass-to-outdoor conductance for the opaque fabric as a
                  whole, BACKED OUT algebraically (not summed per-element)
                  so that H_im and H_mo in series exactly reproduce the
                  known-correct opaque-fabric total, area_i * U_i summed —
                  see the note below on why summing per-element splits
                  doesn't do this.

    r_si values are the standard internal surface resistances used to
    build the U-values in the first place (BS EN ISO 6946): 0.13 m2K/W
    for walls (horizontal flow), 0.10 for roofs (upward flow), 0.17 for
    floors (downward flow).

    Why H_mo is backed out rather than summed per-element: a first attempt
    at this function computed each element's own (r_si, 1/U - r_si) split
    and separately summed the r_si-conductances into H_im and the
    remainder-conductances into H_mo. That is only exact if every element
    has the same r_si-to-total-resistance ratio — false here (SWI's wall
    r_si is ~4% of its total resistance once insulated; the untouched roof
    and floor are ~23-26%), so aggregating them into one shared mass node
    quietly changed the steady-state total by a few percent for the
    retrofitted states. Backing out H_mo instead guarantees the 2-node
    network's steady state matches the 1R1C model EXACTLY, by
    construction, for every state -- H_im is still independently derived
    from BS EN ISO 6946 (it depends only on areas and r_si, not U, so it
    is identical across baseline/SWI/EPC-C), it just isn't forced to also
    fix the total on its own.
    """
    for area in (wall_area_m2, roof_area_m2, floor_area_m2, window_area_m2, heated_volume_m3):
        assert area > 0, "areas and volume must be positive"

    h_direct = 0.33 * state.infiltration_ach * heated_volume_m3 + window_area_m2 * state.window_u_w_per_m2k

    h_im = (
        wall_area_m2 / r_si_wall_m2k_per_w
        + roof_area_m2 / r_si_roof_m2k_per_w
        + floor_area_m2 / r_si_floor_m2k_per_w
    )

    h_fabric_opaque = (
        wall_area_m2 * state.wall_u_w_per_m2k
        + roof_area_m2 * state.roof_u_w_per_m2k
        + floor_area_m2 * state.floor_u_w_per_m2k
    )
    assert h_im > h_fabric_opaque, (
        "internal-film conductance is not larger than the total opaque fabric conductance -- "
        "cannot back out a positive H_mo; check areas, U-values, and r_si inputs"
    )
    h_mo = 1.0 / (1.0 / h_fabric_opaque - 1.0 / h_im)

    # No-double-counting check: the 2-node split, recombined, must
    # reconstruct the original 1R1C H exactly (to floating-point tolerance).
    h_1r1c = heat_loss_coefficient_w_per_k(state, wall_area_m2, roof_area_m2, floor_area_m2, window_area_m2, heated_volume_m3)
    h_mass_path_series = 1.0 / (1.0 / h_im + 1.0 / h_mo)
    h_reconstructed = h_direct + h_mass_path_series
    relative_error = abs(h_reconstructed - h_1r1c) / h_1r1c
    assert relative_error < 1e-6, (
        f"2R2C split does not reconstruct 1R1C H (reconstructed={h_reconstructed:.4f}, "
        f"original={h_1r1c:.4f}, {relative_error:.4%} off) -- this would mean the mass "
        f"and air nodes are double-counting or losing resistance somewhere"
    )

    return h_direct, h_im, h_mo


def simulate_2r2c_coastdown_hours(
    f_air: float,
    c_total_kwh_per_k: float,
    h_direct_w_per_k: float,
    h_im_w_per_k: float,
    h_mo_w_per_k: float,
    t_start_c: float,
    t_min_c: float,
    t_outdoor_c: float,
    t_max_hours: float = 40.0,
    internal_gains_w: float = 0.0,
):
    """Time for the AIR node to cool from t_start_c to t_min_c under a 2-node
    (air / mass) RC network, given no heating input (coastdown only).

    f_air is the DELIBERATE, swept fraction of total thermal capacity
    assigned to the fast-responding air node (air + light contents); the
    remainder sits in the slow-responding mass node. This is not
    independently grounded for this archetype -- report it as a sensitivity
    band, not a point estimate (PROJECT.md Section 2.7, Ambiguity Is
    Informative).

    internal_gains_w (default 0, unchanged behaviour): constant internal
    gains enter the AIR node, not the mass node -- occupants, appliances,
    cooking and lighting heat the room air directly; any warming of the
    structural mass happens only secondhand, via the same air-to-mass
    conductance (h_im) already in the model, not as a separate injected
    term (PROJECT.md Section 2.3, no double-counting).

    Returns None if the air node never reaches t_min_c within t_max_hours.
    """
    from scipy.integrate import solve_ivp

    assert 0 < f_air < 1, "f_air must be a fraction strictly between 0 and 1"
    assert c_total_kwh_per_k > 0
    assert t_start_c > t_min_c > t_outdoor_c

    c_air_wh_per_k = f_air * c_total_kwh_per_k * 1000.0
    c_mass_wh_per_k = (1 - f_air) * c_total_kwh_per_k * 1000.0

    def rhs(_t, y):
        t_air, t_mass = y
        d_air = (
            -(t_air - t_mass) * h_im_w_per_k - (t_air - t_outdoor_c) * h_direct_w_per_k + internal_gains_w
        ) / c_air_wh_per_k
        d_mass = (-(t_mass - t_air) * h_im_w_per_k - (t_mass - t_outdoor_c) * h_mo_w_per_k) / c_mass_wh_per_k
        return [d_air, d_mass]

    def hit_floor(_t, y):
        return y[0] - t_min_c
    hit_floor.terminal = True
    hit_floor.direction = -1

    sol = solve_ivp(
        rhs, [0, t_max_hours], [t_start_c, t_start_c],
        max_step=0.01, events=hit_floor, method="RK45", rtol=1e-8, atol=1e-8,
    )
    if sol.t_events[0].size > 0:
        return float(sol.t_events[0][0])
    return None


_DAYS_PER_MONTH_NON_LEAP = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def annual_heating_electrical_kwh(
    h_w_per_k: float,
    monthly_mean_outdoor_temps_c,
    setpoint_c: float,
    cop: float,
    internal_gains_w: float = 0.0,
    days_per_month=None,
) -> float:
    """Annual space-heating electrical demand (kWh), built from 12
    representative monthly mean outdoor temperatures rather than a single
    design-point or a single 7-day event (Week 5's cold-snap scope).

    For each month, treats that month's mean outdoor temperature as
    constant and applies net_heating_power_kw (the same steady-state,
    gains-netted function used everywhere else in this project) for every
    hour of the month, then sums across all 12 months:

        monthly_kWh = net_heating_power_kw(H, setpoint, T_month_mean, COP,
                                            gains) * 24 * days_in_month
        annual_kWh  = sum(monthly_kWh for all 12 months)

    This deliberately reuses net_heating_power_kw rather than importing an
    externally-published heating-degree-day figure at a fixed conventional
    base temperature (traditionally 15.5C in the UK). A fixed base
    temperature implicitly assumes a single "typical" level of internal
    gains applied uniformly regardless of a building's own H -- exactly
    the kind of state-independent assumption this project's coastdown work
    already showed is wrong (Finding 1: a fixed 400W gain matters far more,
    proportionally, against EPC-C's small H than against baseline's large
    one). Using net_heating_power_kw's own max(..., 0) floor means each
    fabric state's effective "no heating needed" threshold falls out of
    its own H and its own gains automatically, with no separate base-
    temperature assumption to keep consistent with the rest of the model
    (PROJECT.md Section 2.3, no double-counting).

    KNOWN CONSERVATIVE BIAS, stated explicitly rather than hidden: using a
    single mean temperature per month, then flooring at zero, is not the
    same as flooring at zero for every individual day within that month.
    A month whose mean sits just above a state's effective balance-point
    temperature will show zero heating demand here, even though its
    colder-than-average days individually would have needed heating. This
    biases the annual figure to UNDERSTATE true heating demand somewhat,
    more so for low-H (well-insulated) states, whose effective balance
    point sits further below the setpoint. Monthly (not daily or hourly)
    resolution is a deliberate Sledgehammer Test simplification -- a full
    daily-resolution version is flagged as future work, not silently
    assumed equivalent (the same discipline already applied to the Dec
    2022 event's own synthetic hourly profile, PROJECT.md Section 8.3).

    monthly_mean_outdoor_temps_c: 12 values, January through December.
    days_per_month: 12 values matching the same order; defaults to a
    non-leap year (365 days) if not supplied.
    """
    assert h_w_per_k > 0
    assert cop > 0, "COP must be positive"
    monthly_mean_outdoor_temps_c = list(monthly_mean_outdoor_temps_c)
    assert len(monthly_mean_outdoor_temps_c) == 12, "expected 12 monthly mean temperatures"

    if days_per_month is None:
        days_per_month = _DAYS_PER_MONTH_NON_LEAP
    days_per_month = list(days_per_month)
    assert len(days_per_month) == 12, "expected 12 days-per-month values"

    total_kwh = 0.0
    for t_month_c, days in zip(monthly_mean_outdoor_temps_c, days_per_month):
        power_kw = net_heating_power_kw(h_w_per_k, setpoint_c, t_month_c, cop, internal_gains_w)
        total_kwh += power_kw * 24 * days
    return total_kwh


def peak_electrical_demand_kw(
    h_w_per_k: float,
    delta_t_k: float,
    cop: float,
    internal_gains_w: float = 0.0,
) -> float:
    """Steady-state electrical demand to hold a given temperature delta.

    P_thermal = max(H * delta_T - Q_gains, 0); P_electrical = P_thermal / COP.

    internal_gains_w (default 0, unchanged behaviour): constant internal
    gains (occupants, appliances, cooking, lighting) net off part of the
    fabric+ventilation loss before the heat pump has to replace it -- see
    net_heating_power_kw, which this function now delegates to. Still
    ignores solar gains, which are far more time-variable and archetype/
    orientation-dependent than casual internal gains (PROJECT.md Section
    8.3) -- solar is handled separately in notebooks/05's BESS/solar
    comparator, not folded in here.
    """
    assert h_w_per_k > 0
    assert delta_t_k > 0
    return net_heating_power_kw(h_w_per_k, delta_t_k, 0.0, cop, internal_gains_w)
