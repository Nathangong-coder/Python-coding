import pandas as pd
import matplotlib.pyplot as plt

#open the json file and explore it
tmac_df=pd.read_json("Python Programming Topics 1 Spring Trimester\Day 6\\midterm_sensors.json")

#getting rid of columns with no data first
tmac_df=tmac_df.drop(columns=["battery", "float1", "float2", "int1", "int2", "key", "string2", "time_updated", "motion","vibration", "water_level"])

#getting info on df to see what else I neeed to remove
print(tmac_df.info())

#converting from UDT to PST
tmac_df["time_created"]=pd.to_datetime(tmac_df["time_created"])
tmac_df["time_created"]=tmac_df["time_created"].dt.tz_convert("US/Pacific")

#now let's sort data in order of time
tmac_df=tmac_df.sort_values("time_created")

#update index to be the datetime column
tmac_df.index=tmac_df["time_created"]

#see the beginning & end of the dataframe
print(tmac_df.head())
print(tmac_df.tail())

#get data from a single day
print(tmac_df.loc["2023-4-07"])


#using this dataframe, now chart 2 lines on a line chart (temp & humidity as y axis)
plt.title("onboard sensors")
plt.xlabel("date and time")
plt.xticks(rotation=90)
plt.ylabel("values")
plt.plot(tmac_df["temperature"], label="temp - celcius")
plt.plot(tmac_df["humidity"],label="humidity - %")
plt.legend()
plt.show()