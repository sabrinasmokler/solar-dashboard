# Simple Solar Dashboard

A Streamlit dashboard that estimates solar project financial performance based on system size and state electricity prices.

## Overview

This tool allows users to enter a U.S. state and solar system size in kW. It then calculates key solar project metrics, including upfront system cost, annual electricity generation, project IRR, payback period, and a 25-year cash flow table.

## Inputs

- U.S. state
- Solar system size in kW DC

## Outputs

- Solar system upfront price
- Annual generation in kWh
- Project IRR
- Payback period
- 25-year cash flow table

## Financial Assumptions

- Installed cost: $2.50 per watt
- Annual generation: 1,400 kWh per kW
- Electricity price escalation: 2.5% annually
- O&M costs: $15 per kW per year
- 30% ITC tax credit in Year 0
- No financing costs (all equity)

## Technical Requirements Met

- Frontend framework: Streamlit
- Backend calculations: Python
- Cash flows displayed in table format
- IRR and payback period displayed numerically above the table

## Project Structure

- `app.py` — Streamlit dashboard and user interface
- `calculations.py` — solar financial model calculations
- `state_prices.py` — state electricity pricing data
- `requirements.txt` — project dependencies

The project separates frontend code from financial logic to keep the code organized and easier to maintain.

## Technologies Used

- Python
- Streamlit
- pandas
- numpy-financial

Sources Used
Electricity Pricing Data

https://www.electricchoice.com/electricity-prices-by-state/

Residential electricity prices were converted from cents per kWh to dollars per kWh before being used in the model.

AI Assistance

ChatGPT was used as a development aid to validate financial calculations, assist with debugging, and organize code structure.

All final implementation decisions, testing, and project modifications were reviewed and completed by me (Sabrina)