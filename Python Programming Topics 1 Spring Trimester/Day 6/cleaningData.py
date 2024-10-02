import pandas as pd
import matplotlib.pyplot as plt

#open the json file and explore it
tmac_df=pd.read_json("Python Programming Topics 1 Spring Trimester\Day 6\\tmac-feather1-response.json")

print(tmac_df.head())
print(tmac_df.info())

#getting rid of columns with no data first
tmac_df=tmac_df.drop(columns=["battery", "float1", "float2", "int1", "int2", "key", "vibration", "water_level"])
print(tmac_df.info())

#what do we do with columns with partial data, like string2?

print(tmac_df.loc[:,"string2"].value_counts())

#only keep row data when string data = test, drop anything else that doesn't match
tmac_df=tmac_df[tmac_df.loc[:,"string2"]=="test"]
print(tmac_df.info())

#now let's change the timezone to pst
#first convert string to datetime object
tmac_df["time_created"]=pd.to_datetime(tmac_df["time_created"])


#check datatypes of the df
print(tmac_df.dtypes)

print("min date:", tmac_df["time_created"].min())
print("max date:", tmac_df["time_created"].max())

#now let's sort data in order of time
tmac_df=tmac_df.sort_values("time_created")

#finally actually converting it from utc to pst
tmac_df["time_created"]=tmac_df["time_created"].dt.tz_convert("US/Pacific")

#update index to be the datetime column
tmac_df.index=tmac_df["time_created"]
print(tmac_df.head())

#get data from a single day
print(tmac_df.loc["2022-10-28"])

#for just sensors
print(tmac_df.loc["2022-10-28"].loc[:,["light","temperature"]])

#smaller time range
print(tmac_df["2022-10-28 08:29:15.338200-07:00":"2022-10-28 09:15:42.751370-07:00"])

#using this dataframe, now chart 2 lines on a line chart (temp & humidity as y axis)
plt.title("onboard sensors")
plt.xlabel("date and time")
plt.ylabel("values")
plt.plot(tmac_df["temperature"], label="temp - celcius")
plt.plot(tmac_df["humidity"],label="humidity - %")
plt.legend()
plt.show()