#LETS TRY DOING THIS LATER WITH MY CHATGPT YAHOO CODE TO GET ALL YEARS THANKS TO ALPHA VANTAGE
#APIKEY: XTV98OWBKJHIZKNA
from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd
import requests

API_KEY = "XTV98OWBKJHIZKNA"
symbol="AAPL"
# Create API connection
fd = FundamentalData(key=API_KEY, output_format="pandas")

# Fetch income statement data for Apple
income_statement_df, meta = fd.get_income_statement_annual("AAPL")
# Fetch Balance Sheet
balance_sheet_df, _ = fd.get_balance_sheet_annual(symbol)

# Fetch Cash Flow Statement
cash_flow_df, _ = fd.get_cash_flow_annual(symbol)
merged_df = pd.merge(balance_sheet_df, cash_flow_df, on="fiscalDateEnding", how="outer")
megaMerged_df= pd.merge(income_statement_df, merged_df, on="fiscalDateEnding", how="outer")

merged_df = income_statement_df.merge(cash_flow_df, on="fiscalDateEnding", how="outer") \
               .merge(balance_sheet_df, on="fiscalDateEnding", how="outer")
# Save to CSV
merged_df.to_csv("financial_data_AlphaVantageAppleInfo.csv", index=False)
print("✅ Data successfully saved!")


