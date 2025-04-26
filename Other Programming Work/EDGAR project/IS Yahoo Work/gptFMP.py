import pandas as pd
import requests
#KEY: bwYX4Tu3r2vMW7WH6Q96PcOltpGxruXR
#KEY 2: GxfhxdkXowBVsfA65iwcIICgQWUOIcUa
api_key = "GxfhxdkXowBVsfA65iwcIICgQWUOIcUa"  # Replace with your FMP API key
ticker = "AAPL"  # Example: Apple Inc.

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
    ticker=get_ticker(cik_number)
    if not ticker:
        print(f"❌ No ticker found for CIK {cik_number}")
        return

    print(f"✅ Fetching financials for {ticker} (CIK: {cik_number})...")

    try: 
        url_income = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?apikey={api_key}"
        response = requests.get(url_income)
        income_statement = response.json()
        # Convert to DataFrame
        df_income = pd.DataFrame(income_statement)

        url_balance = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?apikey={api_key}"
        response = requests.get(url_balance)
        balance_sheet = response.json()
        # Convert to DataFrame
        df_balance = pd.DataFrame(balance_sheet)

        url_cashflow = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?apikey={api_key}"
        response = requests.get(url_cashflow)
        cash_flow = response.json()
        # Convert to DataFrame
        df_cashflow = pd.DataFrame(cash_flow)
    except ValueError:
        try:
            url_income = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?apikey={api_key}"
            response = requests.get(url_income)
            income_statement = response.json()
            # Convert to DataFrame
            df_income = pd.DataFrame(income_statement)

            url_balance = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?apikey={api_key}"
            response = requests.get(url_balance)
            balance_sheet = response.json()
            # Convert to DataFrame
            df_balance = pd.DataFrame(balance_sheet)

            url_cashflow = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?apikey={api_key}"
            response = requests.get(url_cashflow)
            cash_flow = response.json()
            # Convert to DataFrame
            df_cashflow = pd.DataFrame(cash_flow)
        except ValueError:
            try:
                url_income = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?apikey={api_key}"
                response = requests.get(url_income)
                income_statement = response.json()
                # Convert to DataFrame
                df_income = pd.DataFrame(income_statement)

                url_balance = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?apikey={api_key}"
                response = requests.get(url_balance)
                balance_sheet = response.json()
                # Convert to DataFrame
                df_balance = pd.DataFrame(balance_sheet)

                url_cashflow = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?apikey={api_key}"
                response = requests.get(url_cashflow)
                cash_flow = response.json()
                # Convert to DataFrame
                df_cashflow = pd.DataFrame(cash_flow)
            except ValueError:
                return 

    #extract the specific columns I need from each df & append them
    #NET INCOME
    if "netIncome" in df_income.columns:
        income_statement_df=df_income[["date","netIncome"]]
    else:
        print("\nsorry, but net income was not extracted successfully")
    #SHAREHOLDER EQUITY
    if "totalStockholdersEquity" in df_balance.columns:
        balance_sheet_df=df_balance[["date","totalStockholdersEquity"]]
    else:
        print("\nsorry, but totalShareholderEquity was not extracted successfully")
    
    #CASH FLOW
    if "freeCashFlow" and "capitalExpenditure" in df_cashflow.columns:
        cash_flow_df=df_cashflow[["date","freeCashFlow","capitalExpenditure"]]
    else:
        print("\n sorry but operatingCashFlow not extract. L BOZO")

    #combine all columns into a df (temp_df), which is appended to financial_data_list for final analysis
    temp_df = income_statement_df.merge(cash_flow_df, on="date", how="outer") \
               .merge(balance_sheet_df, on="date", how="outer")

    financial_data_list.append(temp_df)



# Loop through all CIKs and fetch data
for cik_number in df["cik_str"]:
    fetch_data(cik_number)

# Combine all financial data into a single DataFrame
if financial_data_list:
    financial_df = pd.concat(financial_data_list, ignore_index=True)

#trademark nathan gong print statement
print(financial_df.head())


financial_df.to_csv("FMPfinancial_statements_shops.csv", index=False)
print("✅ Data saved as financial_statements.csv")
