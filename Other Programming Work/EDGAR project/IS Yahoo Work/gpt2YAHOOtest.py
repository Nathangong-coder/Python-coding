import pandas as pd
import yfinance as yf
import requests

# Load Excel file correctly
df = pd.read_excel("C:/Users/NGong/Downloads/Independent Study Stuff/annual_firm_level_Darmouni_Mota_existingfile_updated.xlsb.xlsx", sheet_name="Tech CIK")

# Ensure correct column for CIKs
df["cik_str"] = pd.to_numeric(df["industry"], errors="coerce")
df = df.dropna(subset=["cik_str"])
df["cik_str"] = df["cik_str"].astype(int).astype(str).str.zfill(10)
df['cik_str'] = df["cik_str"].astype(int).astype(str)
print(df)


# Load CIK-to-Ticker mapping from SEC
headers = {'User-Agent': "ngong@eastsideprep.org"}
companyTickers = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers).json()
cik_map = pd.DataFrame.from_dict(companyTickers, orient="index")
cik_map.columns = ["CIK", "Ticker", "Name"]

# Function to get ticker from CIK
def get_ticker(cik_number):
    ticker = cik_map.loc[cik_map["CIK"] == int(cik_number), "Ticker"]
    return ticker.values[0] if not ticker.empty else None

# List to store financial data
financial_data_list = []

# Function to fetch financial data
def fetch_financial_data(cik_number):
    ticker = get_ticker(cik_number)
    if not ticker:
        print(f"❌ No ticker found for CIK {cik_number}")
        return

    print(f"✅ Fetching financials for {ticker} (CIK: {cik_number})...")
    stock = yf.Ticker(ticker)

    # Extract financial data
    income_stmt = stock.income_stmt.T
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T

    # Convert index to years
    income_stmt.index = pd.to_datetime(income_stmt.index, errors="coerce").year
    balance_sheet.index = pd.to_datetime(balance_sheet.index, errors="coerce").year
    cash_flow.index = pd.to_datetime(cash_flow.index, errors="coerce").year

    # Create DataFrame for each CIK
    temp_df = pd.DataFrame({"Year": income_stmt.index})
    temp_df["CIK"] = cik_number  # Keep CIK column

    # Extract specific financial values
    if "Net Income" in income_stmt.columns:
        net_income = income_stmt[["Net Income"]]
        #net_income.index = net_income.index.year  # Convert to year index
        # Convert to DataFrame for appending
        net_income_df = net_income.reset_index().rename(columns={"index": "Year", "Net Income": "Net_Income"})
        net_income_df["CIK"] = cik_number  # Add CIK column for tracking

        # Append row-wise
        temp_df = pd.concat([temp_df, net_income_df], ignore_index=True)
    if "Stockholders Equity" in balance_sheet.columns:
        stockholder_equity = balance_sheet["Stockholders Equity"]
        #stockholder_equity.index = stockholder_equity.index.year  # Convert to year index
        # Convert to DataFrame for appending
        stockholder_equity_df = stockholder_equity.reset_index().rename(columns={"index": "Year", "Net Income": "Net_Income"})
        # Append row-wise
        temp_df = pd.concat([temp_df, stockholder_equity_df], ignore_index=True)
    if "Capital Expenditure" in cash_flow.columns:
        cap_ex = cash_flow["Capital Expenditure"]
        #cap_ex.index = cap_ex.index.year  # Convert to year index
        # Convert to DataFrame for appending
        cap_ex_df = cap_ex.reset_index().rename(columns={"index": "Year", "Net Income": "Net_Income"})

        # Append row-wise
        temp_df = pd.concat([temp_df, cap_ex_df], ignore_index=True)
    if "Free Cash Flow" in cash_flow.columns:
        free_cash_flow= cash_flow["Free Cash Flow"]
        #free_cash_flow.index = free_cash_flow.index.year  # Convert to year index
        # Convert to DataFrame for appending
        free_cash_flow_df = free_cash_flow.reset_index().rename(columns={"index": "Year", "Net Income": "Net_Income"})

        # Append row-wise
        temp_df = pd.concat([temp_df, free_cash_flow_df], ignore_index=True)
    else:
        temp_df["Free Cash Flow"] = None

    # Append data
    financial_data_list.append(temp_df)

# Loop through all CIKs and fetch data
for cik_number in df["cik_str"]:
    fetch_financial_data(cik_number)

# Combine all financial data into a single DataFrame
if financial_data_list:
    financial_df = pd.concat(financial_data_list, ignore_index=True)
print("CHAT\n")
print(financial_df)
# Ensure both DataFrames have the CIK column as a string
df["CIK"] = df["cik_str"].astype(str)
financial_df["CIK"] = financial_df["CIK"].astype(str)
print(financial_df)
# Merge data with company information
#df = df.merge(financial_df, on="CIK", how="left")
#print("SUPER CHAT\n")
#print(df)
# Pivot table so years are columns
#df_pivoted = df.pivot(index="CIK", columns="Year", values=["Net Income", "Stockholders' Equity", "Capital Expenditures", "Free Cash Flow"])

# Flatten column names
#df_pivoted.columns = [f"{metric}_{year}" for metric, year in df_pivoted.columns]
#df_pivoted.reset_index(inplace=True)

# Save to CSV
financial_df.to_csv("financial_data_newInfo.csv", index=False)
print("✅ Data successfully saved!")

# Display output