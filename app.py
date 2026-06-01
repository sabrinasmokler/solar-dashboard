import streamlit as st

from state_prices import STATE_PRICES
from calculations import calculate_solar_project


# Page title
st.title("Simple Solar Dashboard")


# User inputs
state = st.selectbox(
    "Select State",
    list(STATE_PRICES.keys())
)

system_size_kw = st.number_input(
    "System Size (kW)",
    min_value=1.0,
    value=10.0
)


# Run calculations
results = calculate_solar_project(
    system_size_kw,
    STATE_PRICES[state]
)


# Display key metrics
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Upfront System Cost",
        f"${results['upfront_cost']:,.0f}"
    )

    st.metric(
        "Annual Generation",
        f"{results['annual_generation']:,.0f} kWh"
    )

with col2:
    st.metric(
        "Project IRR",
        f"{results['irr']:.2f}%"
    )

    st.metric(
        "Payback Period",
        f"{results['payback_period']} years"
    )

# Cash flow table
st.subheader("25-Year Cash Flow Table")

st.dataframe(results["table"])