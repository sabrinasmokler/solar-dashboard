import pandas as pd
import numpy_financial as npf


def calculate_solar_project(system_size_kw, electricity_rate):

    # Upfront system cost
    upfront_cost = system_size_kw * 1000 * 2.5

    # 30% federal tax credit
    tax_credit = upfront_cost * 0.30

    # Net Year 0 cost
    year_0_cash_flow = -upfront_cost + tax_credit

    # Annual electricity generation
    annual_generation = system_size_kw * 1400

    # Annual maintenance cost
    om_cost = system_size_kw * 15

    cash_flows = [year_0_cash_flow]

    table_data = []

    cumulative_cash_flow = year_0_cash_flow

    payback_period = None

    for year in range(1, 26):

        # Electricity price increases 2.5% annually
        adjusted_rate = electricity_rate * (1.025 ** (year - 1))

        # Annual electricity savings
        annual_savings = annual_generation * adjusted_rate

        # Net yearly cash flow
        net_cash_flow = annual_savings - om_cost

        cash_flows.append(net_cash_flow)

        cumulative_cash_flow += net_cash_flow

        # Find payback year
        if cumulative_cash_flow > 0 and payback_period is None:
            payback_period = year

        table_data.append({
            "Year": year,
            "Electricity Rate": round(adjusted_rate, 4),
            "Annual Savings ($)": round(annual_savings, 2),
            "O&M Cost ($)": round(om_cost, 2),
            "Net Cash Flow ($)": round(net_cash_flow, 2),
            "Cumulative Cash Flow ($)": round(cumulative_cash_flow, 2)
        })

    # Calculate IRR
    irr = npf.irr(cash_flows) * 100

    # Create table
    df = pd.DataFrame(table_data)

    return {
        "upfront_cost": upfront_cost,
        "annual_generation": annual_generation,
        "irr": irr,
        "payback_period": payback_period,
        "table": df
    }