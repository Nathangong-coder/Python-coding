import requests
import pandas as pd
import matplotlib.pyplot as plt

SUBPLOT_ROW = 2
SUBPLOT_COLUMN = 3

try:
    # send get request to datalogger db to retrieve data
    # values must match the string values you sent from your feathers!
    # it's a good idea to test this url get with the postman app first
    response = requests.get("https://eps-datalogger.herokuapp.com/api/data/area/teamNONGAS_offices/s2023-ma2-superFinal")
    
    # convert response to json format
    response_json = response.json()

    # print(response_json)
    # convert json to dataframe
    df = pd.DataFrame.from_dict(response_json)

    #getting rid of columns with no data first/useless data, like tilt
    tmac_df=df.drop(columns=["battery", "float1", "float2", "int2", "key", "string2", "time_updated", "tilt","vibration", "water_level"])

    #converting from UDT to PST
    tmac_df["time_created"]=pd.to_datetime(tmac_df["time_created"])
    tmac_df["time_created"]=tmac_df["time_created"].dt.tz_convert("US/Pacific")

    #now let's sort data in order of time
    tmac_df = tmac_df.sort_values("time_created")

    #update index to be the datetime column
    tmac_df.index=tmac_df["time_created"]

    ngong_tmac_df=tmac_df[tmac_df.loc[:,"username"]=="ngong"]
    noberoi_tmac_df=tmac_df[tmac_df.loc[:,"username"]=="noberoi"]
    asadahiro_tmac_df=tmac_df[tmac_df.loc[:,"username"]=="asadahiro"]

    #figuring out min & max date
    print("min date:", tmac_df["time_created"].min())
    print("max date:", tmac_df["time_created"].max())

    #test prints to understand dataset
    print(tmac_df.tail())
    print(tmac_df.info())
    print(tmac_df.loc[:,"int1"])
    print(tmac_df.loc[:,"time_created"])
    print(asadahiro_tmac_df.loc[:,"int1"].tail())

    
    fig = plt.figure(figsize = (12, 6))

    #temp graphs
    temp_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 1)
    temp_plot.set_title("onboard sensors - temp")
    temp_plot.set_xlabel("date and time")
    temp_plot.set_ylabel("values")
    temp_plot.plot(ngong_tmac_df["temperature"], label="temp - nathan")
    temp_plot.plot(noberoi_tmac_df["temperature"],label="temp - nihaal")
    temp_plot.plot(asadahiro_tmac_df["temperature"],label="temp - andrew")
    temp_plot.legend(loc='upper left')
    plt.xticks(rotation=90)

    #sensitive sound graph
    sens_sound_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 2)
    sens_sound_plot.set_title("sensitive sound")
    sens_sound_plot.set_label("date and time")
    sens_sound_plot.set_ylabel("values")
    sens_sound_plot.plot(ngong_tmac_df["int1"], label="nathan")
    sens_sound_plot.plot(noberoi_tmac_df["int1"],label="nihaal")
    sens_sound_plot.plot(asadahiro_tmac_df["int1"],label="andrew")
    sens_sound_plot.legend(loc='upper left')
    plt.xticks(rotation=90)


    #motion graph
    motion_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 3)
    motion_plot.set_title("motion")
    motion_plot.set_xlabel("date and time")
    motion_plot.set_ylabel("values")
    motion_plot.plot(ngong_tmac_df["motion"], label="nathan")
    motion_plot.plot(noberoi_tmac_df["motion"],label="nihaal")
    motion_plot.plot(asadahiro_tmac_df["motion"],label="andrew")
    motion_plot.legend(loc='upper left')
    plt.xticks(rotation=90)

    #humidity graph
    humidity_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 4)
    humidity_plot.set_title("humidity")
    humidity_plot.set_xlabel("date and time")
    humidity_plot.set_ylabel("values")
    humidity_plot.plot(ngong_tmac_df["humidity"], label="nathan")
    humidity_plot.plot(noberoi_tmac_df["humidity"],label="nihaal")
    humidity_plot.plot(asadahiro_tmac_df["humidity"],label="andrew")
    humidity_plot.legend(loc='upper left')
    plt.xticks(rotation=90)

    #sound graph
    sound_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 5)
    sound_plot.set_title("sound")
    sound_plot.set_label("date and time")
    sound_plot.set_ylabel("values")
    sound_plot.plot(ngong_tmac_df["sound"], label="nathan")
    sound_plot.plot(noberoi_tmac_df["sound"],label="nihaal")
    sound_plot.plot(asadahiro_tmac_df["sound"],label="andrew")
    sound_plot.legend(loc='upper left')
    plt.xticks(rotation=90)

    #light graph
    light_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 6)
    light_plot.set_title("light")
    light_plot.set_label("date and time")
    light_plot.set_ylabel("values")
    light_plot.plot(ngong_tmac_df["light"], label="nathan")
    light_plot.plot(noberoi_tmac_df["light"],label="nihaal")
    light_plot.plot(asadahiro_tmac_df["light"],label="andrew")
    light_plot.legend(loc='upper left')
    plt.xticks(rotation=90)


    plt.show()

except Exception as e:
    print("There was an error when trying to get from datalogger at https://eps-datalogger.herokuapp.com/api/:", e)