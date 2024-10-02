# import modules
import requests
import pandas as pd
from edgar import *

#rando stuff
set_identity("Nathan Gong ngong@eastsideprep.org")
filings = Company("AAPL").get_filings(form="10-K").latest(5)

# create request header
headers = {'User-Agent': "email@address.com"}

# get all companies data
companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
    )

# review response / keys
print(companyTickers.json().keys())

# format response to dictionary and get first key/value
firstEntry = companyTickers.json()['0']

# parse CIK // without leading zeros
directCik = companyTickers.json()['0']['cik_str']

# dictionary to dataframe
companyData = pd.DataFrame.from_dict(companyTickers.json(),
                                     orient='index')

# add leading zeros to CIK
companyData['cik_str'] = companyData['cik_str'].astype(
                           str).str.zfill(10)

# review data
print(companyData[:1])

cik = companyData[0:1].cik_str[0]

# get company specific filing metadata
filingMetadata = requests.get(
    f'https://data.sec.gov/submissions/CIK{cik}.json',
    headers=headers
    )

# review json 
print(filingMetadata.json().keys())
filingMetadata.json()['filings']
filingMetadata.json()['filings'].keys()
filingMetadata.json()['filings']['recent']
filingMetadata.json()['filings']['recent'].keys()

# dictionary to dataframe
allForms = pd.DataFrame.from_dict(
             filingMetadata.json()['filings']['recent']
             )

# review columns, taking all the 10Ks ONLY
allForms.columns
allForms = allForms[allForms.loc[:,"form"]=="10-K"]
print(allForms[['accessionNumber','reportDate','form']].head())

#taking the 2nd one (doesn't really matter right now)
coolforms=allForms.iloc[4]
print(coolforms)
#using the edgartools library to cast "coolforms" into a xbrl
#coolforms=coolforms.xbrl()
#filings=filings.xbrl()
#casting the xbrl into a pandas df
#coolforms=coolforms.to_pandas()
#filings=filings.to_pandas()
# get company facts data
companyFacts = requests.get(
    f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',
    headers=headers
    )

#review data
companyFacts.json().keys()
companyFacts.json()['facts']
print(companyFacts.json()['facts'].keys())
print(companyFacts.json()['facts']['us-gaap'].keys())

print(companyFacts.json()['facts']['us-gaap']['CashAndCashEquivalentsAtCarryingValue'])
