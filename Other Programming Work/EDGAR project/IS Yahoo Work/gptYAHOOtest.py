import pandas as pd
from typing import Optional, List, Dict
import sqlite3
import yfinance as yf
import requests

# Empty list to store data
data_list = []

#NEW CODE 
df=pd.read_excel("C:/Users/NGong/Downloads/Independent Study Stuff/annual_firm_level_Darmouni_Mota_existingfile.xlsx",sheet_name='Tech CIK')
# Convert the column to numeric, coercing errors to NaN for non-integer values
df["cik_str"] = pd.to_numeric(df["industry"], errors='coerce')
# Drop rows where 'ID' is NaN (i.e., non-integer values)
df = df.dropna(subset=["cik_str"])
# Convert back to integer if needed
df["cik_str"] = df["cik_str"].astype(int)
df['cik_str'] = df['cik_str'].astype(str).str.zfill(10)
df['cik_str'] = df["cik_str"].astype(int).astype(str)
print(df)

# Load CIK-to-Ticker mapping from SEC
# create request header
headers = {'User-Agent': "ngong@eastsideprep.org"}
# get all companies data
companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
    )
cik_map = companyTickers.json()
cik_map = pd.DataFrame.from_dict(cik_map, orient="index")
print(cik_map)
# Rename columns for readability
cik_map.columns = ["CIK", "Ticker", "Name"]
print(cik_map.head())
# Function to get ticker from CIK
def get_ticker(cik_number):
    ticker = cik_map.loc[cik_map["CIK"] == int(cik_number), "Ticker"]
    print(ticker)
    return ticker.values[0] if not ticker.empty else None

def fetch_financial_data(cik_number):
    ticker = get_ticker(cik_number)
    if not ticker:
        print(f"❌ No ticker found for CIK {cik_number}")
        return

    print(f"✅ Fetching financials for {ticker} (CIK: {cik_number})...")
    stock = yf.Ticker(ticker)

    # Extract financial statements

    financials = stock.financials.T
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T
    #data_list.append(financials)
    #data_list.append(balance_sheet)
    #data_list.append(cash_flow)

    income_statement=stock.income_stmt.T
    # Extract only the "Net Income" column
    if "Net Income" in income_statement.columns:
        net_income = income_statement[["Net Income"]]
        #net_income.index = net_income.index.year  # Convert index (datetime) to year
        df["Net Income"]=net_income
        data_list.append(net_income)
    #Extract only the "Stockholders Equity" column
    if "Stockholders Equity" in balance_sheet.columns:
        stockholder_equity = balance_sheet["Stockholders Equity"]
        #stockholder_equity.index = stockholder_equity.index.year  # Convert index (datetime) to year
        df["Stockholders Equity"]=stockholder_equity
        data_list.append(stockholder_equity)
    else:
        print(f"❌ 'Stockholders' Equity' not found for {ticker}")
    #Extract only the Capital Expenditure column
    if "Capital Expenditure" in cash_flow.columns:
        cap_ex = cash_flow["Capital Expenditure"]
        #cap_ex.index = cap_ex.index.year  # Convert index (datetime) to year
        df["Capital Expenditure"]=cap_ex
        data_list.append(cap_ex)
    else:
        print("hehehaw")
    #Extract only the Free Cash Flow column
    if "Free Cash Flow" in cash_flow.columns:
        free_cash_flow= cash_flow["Free Cash Flow"]
        #free_cash_flow.index=free_cash_flow.index.year
        df["Free Cash Flow"]=free_cash_flow
        data_list.append(free_cash_flow)
    else:
        print(f"❌ 'Free Cash Flow' not found for {ticker}")

for cik_number in df["cik_str"]:
    #print(cik_number)
    #print("This is a super cool tracking print statement")
    fetch_financial_data(cik_number)    

# Combine data from all companies (NOT needed since not appending to data_list)
financial_df = pd.concat(data_list)

#printing the columns of both dataframes to make sure they match
print(financial_df.columns)
print(df.columns)

print(financial_df.head())
df=df.merge(financial_df,on="Net Income",how="left")
#
print(df)

# Convert datetime column to year (assuming it's named 'Date')
#df['Year'] = pd.to_datetime(df['Date']).dt.year

# Drop the original Date column (optional)
#df.drop(columns=['Date'], inplace=True)

# Sort by Year
#df = df.sort_values(by='Year')

# Save to CSV
df.to_csv("financial_data_COOLInfo.csv")

print(df.head())


#TO DO: 
#1) EXTRACT THE YEARS OF 2008->2021, see if that's possible (not just most recent 5 years)
#2) Add company names as extra column
#3) figure out which columns correspond to what i want, filter them
#3b) after filtering data, i'll compare average of asset vs average of the financial data i extract (first need new pivottable to have year instead of cik for priority for Darmouni_excel, then compare with filtered, year-averaged columns of financial_data)
#4