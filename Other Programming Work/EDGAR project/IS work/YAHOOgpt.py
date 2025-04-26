import yfinance as yf
import pandas as pd


# List of ticker symbols
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Empty list to store data
data_list = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    financials = stock.financials.T  # Transpose for readability
    financials["Ticker"] = ticker  # Add ticker for reference
    data_list.append(financials)

# Combine data from all companies
df = pd.concat(data_list)

# Save to CSV
df.to_csv("financial_data.csv")

print(df.head())

import yfinance as yf

ticker = "AAPL"
stock = yf.Ticker(ticker)

# Extract financials (Income Statement, Balance Sheet, Cash Flow)
income_statement = stock.financials.T  # Transpose for better readability

# Convert index to datetime to filter by year
income_statement.index = pd.to_datetime(income_statement.index)

# Filter for a specific year (e.g., 2022)
year = 2022
filtered_data = income_statement[income_statement.index.year == year]