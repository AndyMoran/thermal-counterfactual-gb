"""thermal-counterfactual-gb — Week 4 interactive demo.

Run with: uv run streamlit run demo/app.py

Consumes the parquet outputs of notebooks 01-04 (data/intermediate/). This
app should only read and visualise already-validated notebook outputs, per
the Parquet Handoff Rule (PROJECT.md Section 4.2) — do not recompute physics
here; if a number needs recalculating, fix it upstream in the notebook.
"""
import streamlit as st

st.set_page_config(page_title="Thermal Envelope as a Passive Grid Asset", layout="wide")

st.title("Thermal Envelope as a Passive Grid Asset")
st.caption(
    "Fabric retrofit as a counterfactual grid-flexibility asset — "
    "pre-1919 solid-wall terrace, UK social housing"
)

st.warning(
    "Scaffold only — this app has no data wired up yet. "
    "Point it at data/intermediate/*.parquet once notebooks 01-04 have run."
)

# TODO (Week 4):
# - Slider 1: "Insulation Quality (U-value)" -> watch peak demand drop
# - Slider 2: "Outdoor Temperature" -> watch Coastdown Hours change
# - Headline, in Modelling Prose form (PROJECT.md Section 8.3 pattern —
#   Number, Unit, Denominator, Mechanism, Scope boundary, Caveat):
#   "If you retrofit N homes in this block, you save the DNO £X and
#    generate £Y/year in VPP flexibility revenue, because ... . This
#    covers [scope]. It assumes [caveat]."
