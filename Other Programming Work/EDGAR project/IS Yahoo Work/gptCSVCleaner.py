import pandas as pd
# Load Excel file correctly
df = pd.read_csv("C:/Users/NGong/OneDrive - Eastside Preparatory School/Documents/Coding/Python coding/Other Programming Work/financial_data_newInfo.csv")

df_cleaned = df.dropna(how='all', subset=["Net_Income", "Stockholders Equity", "Capital Expenditure", "Free Cash Flow"])
print(df_cleaned)
df_cleaned = df_cleaned.fillna(method="ffill")  # Forward fill to keep data aligned
df_cleaned = df_cleaned.groupby(["CIK", "Year"]).first().reset_index()
print(df_cleaned.head())
df_cleaned.to_csv("financials_cleaned.csv", index=False)

