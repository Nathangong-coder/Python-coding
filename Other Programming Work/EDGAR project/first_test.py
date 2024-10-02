from edgar import *
from edgar.financials import Financials
import requests
import pandas as pd
import html5lib
# Define a search function
def search_string(s, search):
    return search in str(s).lower()

def searchFairValueMeasurement(df):
    for i in range(len(df)):
        # Search for the string 'al' in all columns
        search = df[i].apply(lambda x: x.map(lambda s: search_string(s, 'Fair Value Measurements')))
        if search.empty==False:
            search = df[i].apply(lambda x: x.map(lambda s: search_string(s, 'Money market funds')))
            if search.empty==False:
                return df[i]
            else:
                print('Kinda Skill Issue')
        else:
            #need to figure out where FairValueTracker was found in the list (which list item it was)
            #then equal it to df and return it
            print('Skill Issue')

def searchOtherFootnotes(df):
    for i in df:
        FootnoteTracker=df.get('')
        OtherFootnoteTracker=df.get('')
        if FootnoteTracker=='Cool':
            return
        elif OtherFootnoteTracker =='Super Cool':  
            return
        else:
            print("Skill issue")

set_identity("Nathan Gong ngong@eastsideprep.org")
company=Company("AAPL")
filings = Company("AAPL").get_filings(form="10-K").latest(10)
print(filings)
#first using only 1 filing (2019 one)
filings=filings[4]


#use the hack from sec-api.io to read in the html file
#first casting to html using edgar library
html_filings = filings.html()

# read HTML table from a string and convert to dataframe
tables = pd.read_html(html_filings)
# first table includes the financial statements
df = tables
print(df)
FairValue=searchFairValueMeasurement(df)
#current not printing what I want, but is still getting somethign...
print(FairValue)
print(type(FairValue))
#grabbing the financial statement (we will use this to take the cash & cash eq total (cash_agg))
#fin=company.financials.balance_sheet()
#balance_sheet_df=fin.to_dataframe()
#print(balance_sheet_df)
#now trying to filter and get the necessary data
#cash_total=balance_sheet_df.loc["Cash and cash equivalents"]
#print(cash_total)
