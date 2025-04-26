import pandas as pd
from typing import Optional, List, Dict
import sqlite3
#NEW CODE 
df=pd.read_excel("C:/Users/NGong/Downloads/Independent Study Stuff/annual_firm_level_Darmouni_Mota_existingfile.xlsx",sheet_name='Tech CIK')
# Convert the column to numeric, coercing errors to NaN for non-integer values
df["cik_str"] = pd.to_numeric(df["industry"], errors='coerce')
print(df)
# Drop rows where 'ID' is NaN (i.e., non-integer values)
df = df.dropna(subset=["cik_str"])

# Convert back to integer if needed
df["cik_str"] = df["cik_str"].astype(int)
df['cik_str'] = df['cik_str'].astype(str).str.zfill(10)
print(df.iloc[1])
print(df["industry.1"])
df['title']=df["industry.1"]
print(df)
#OLD CODE

