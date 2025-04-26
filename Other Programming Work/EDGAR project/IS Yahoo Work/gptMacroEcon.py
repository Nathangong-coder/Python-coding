import pandas_datareader as pdr

# Get US GDP data
df = pdr.get_data_fred("GDP")

print(df.head())
