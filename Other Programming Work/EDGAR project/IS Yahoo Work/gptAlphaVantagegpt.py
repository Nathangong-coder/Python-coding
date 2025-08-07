#LETS TRY DOING THIS LATER WITH MY CHATGPT YAHOO CODE TO GET ALL YEARS THANKS TO ALPHA VANTAGE
#APIKEY: XTV98OWBKJHIZKNA
from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd
import requests
import itertools
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

API_KEY = "XTV98OWBKJHIZKNA"
API_KEY_2="MEYTE9R32TK6C1X6"
API_KEY_3="MVP3K0YPL0MG7852"
API_KEY_4="1WS9U087Z35WN7TD"
API_KEY_5="Q7EUG95TKZEF2ZMV"
API_KEY_6="K5SHPI35VODN6CSS"
API_KEY_7="ZYH2EAW7Y4WHQWVA"
API_KEY_8="3ZDIFWCZKIWFH9Z1"
API_KEY_9="YLVI5YHD3DV44LGG"
API_KEY_10="741Q8YNR7TCE2499"
# 🔹 List of API keys
api_keys = [
    API_KEY, API_KEY_2, API_KEY_3, API_KEY_4, API_KEY_5,
    API_KEY_6, API_KEY_7, API_KEY_8, API_KEY_9, API_KEY_10
]

# 🔹 Rotate API keys automatically
key_cycle = itertools.cycle(api_keys)
# Create API connection
fd = FundamentalData(key=API_KEY_2, output_format="pandas")
fd_backup=FundamentalData(key=API_KEY_3,output_format="pandas")
fd_backup_2=FundamentalData(key=API_KEY,output_format="pandas")
fd_backup_3=FundamentalData(key=API_KEY_4,output_format="pandas")
fd_backup_4=FundamentalData(key=API_KEY_5,output_format="pandas")
fd_backup_5=FundamentalData(key=API_KEY_6,output_format="pandas")
fd_backup_6=FundamentalData(key=API_KEY_7,output_format="pandas")
fd_backup_7=FundamentalData(key=API_KEY_8,output_format="pandas")
fd_backup_8=FundamentalData(key=API_KEY_9,output_format="pandas")
fd_backup_9=FundamentalData(key=API_KEY_10,output_format="pandas")
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

def fetch_data(cik_number):
    #get the ticker (print the ones that don't show up)
    api_key=next(key_cycle)
    fd=FundamentalData(api_key,output_format="pandas")
    ticker=get_ticker(cik_number)
    if not ticker:
        print(f"❌ No ticker found for CIK {cik_number}")
        return

    print(f"✅ Fetching financials for {ticker} (CIK: {cik_number})...")
    try:
        income_statement_df, meta = fd.get_income_statement_annual(ticker)
        # Fetch Balance Sheet
        balance_sheet_df, _ = fd.get_balance_sheet_annual(ticker)
        # Fetch Cash Flow Statement
        cash_flow_df, _ = fd.get_cash_flow_annual(ticker)
    except ValueError:
        print("There is value error, haha!")
        time.sleep(random.uniform(5, 10)) 
        return 
    #extract the specific columns I need from each df & append them
    #NET INCOME
    if "netIncome" in income_statement_df.columns:
        income_statement_df=income_statement_df[["fiscalDateEnding","netIncome"]]
    else:
        print("\nsorry, but net income was not extracted successfully")
    #SHAREHOLDER EQUITY
    if "totalShareholderEquity" in balance_sheet_df.columns:
        balance_sheet_df=balance_sheet_df[["fiscalDateEnding","totalShareholderEquity"]]
    else:
        print("\nsorry, but totalShareholderEquity was not extracted successfully")
    
    #CASH FLOW
    if "operatingCashflow" and "capitalExpenditures" in cash_flow_df.columns:
        cash_flow_df=cash_flow_df[["fiscalDateEnding","operatingCashflow","capitalExpenditures"]]
    else:
        print("\n sorry but operatingCashFlow not extract. L BOZO")

    #combine all columns into a df (temp_df), which is appended to financial_data_list for final analysis
    temp_df = income_statement_df.merge(cash_flow_df, on="fiscalDateEnding", how="outer") \
               .merge(balance_sheet_df, on="fiscalDateEnding", how="outer")

    financial_data_list.append(temp_df)



# Loop through all CIKs and fetch data
for cik_number in df["cik_str"]:
    fetch_data(cik_number)
    time.sleep(random.uniform(5, 10)) 

# Combine all financial data into a single DataFrame
financial_df = pd.concat(financial_data_list, ignore_index=True)

#trademark nathan gong print statement
print(financial_df)

# Save to CSV
financial_df.to_csv("financial_data_AlphaVantageFinancialInfo_big5Companies3.csv", index=False)
print("✅ Data successfully saved!")

#TO DO: figure out how saving to CSV can be in certain folders (too many CSVs, getting messy, even for me)