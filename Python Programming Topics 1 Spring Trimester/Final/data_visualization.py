import requests
import pandas as pd
import matplotlib.pyplot as plt

SUBPLOT_ROW = 2
SUBPLOT_COLUMN = 3

try:
    # send get request to datalogger db to retrieve data
    # values must match the string values you sent from your feathers!
    # it's a good idea to test this url get with the postman app first
    response = requests.get(
    "https://eps-datalogger.herokuapp.com/api/data/area/teamNONGAS_offices/s2023-ma2-Final")

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
    tmac_df=tmac_df.sort_values("time_created")

    #update index to be the datetime column
    tmac_df.index=tmac_df["time_created"]

    #figuring out min & max date
    print("min date:", tmac_df["time_created"].min())
    print("max date:", tmac_df["time_created"].max())

    #test prints to understand dataset
    print(tmac_df.tail())
    print(tmac_df.info())
    print(tmac_df.loc[:,"int1"])
    
    #indexing time
    time_created_dt_index=pd.DatetimeIndex(tmac_df["time_created"])
    tmac_df["month"] = time_created_dt_index.month
    tmac_df["day"] = time_created_dt_index.day
    tmac_df["hour"] = time_created_dt_index.hour
    tmac_df["minute"] = time_created_dt_index.minute

    #truncate time data
    tmac_df["short_time_created"]=tmac_df["time_created"].dt.strftime("%m-%d %H:%M")

    
    #only have my name's data
    ngong_tmac_df=tmac_df[tmac_df.loc[:,"username"]=="ngong"]
    noberoi_tmac_df=tmac_df[tmac_df.loc[:,"username"]=="noberoi"]
    asadahiro_tmac_df=tmac_df[tmac_df.loc[:,"username"]=="asadahiro"]

    #start to groupby with temp
    ngong_hourTemp_sg=ngong_tmac_df.groupby("hour")["temperature"]
    noberoi_hourTemp_sg=noberoi_tmac_df.groupby("hour")["temperature"]
    asadahiro_hourTemp_sg=asadahiro_tmac_df.groupby("hour")["temperature"]

    ngong_hourTemp_avg=ngong_hourTemp_sg.aggregate("mean")
    noberoi_hourTemp_avg=noberoi_hourTemp_sg.aggregate("mean")
    asadahiro_hourTemp_avg=asadahiro_hourTemp_sg.aggregate("mean")
    
    #sens sound
    ngong_hourSensSound_sg = ngong_tmac_df.groupby("hour")["int1"]
    noberoi_hourSensSound_sg = noberoi_tmac_df.groupby("hour")["int1"]
    asadahiro_hourSensSound_sg = asadahiro_tmac_df.groupby("hour")["int1"]

    ngong_hourSensSound_avg = ngong_hourSensSound_sg.aggregate("mean")
    noberoi_hourSensSound_avg = noberoi_hourSensSound_sg.aggregate("mean")
    asadahiro_hourSensSound_avg = asadahiro_hourSensSound_sg.aggregate("mean")

    #light
    ngong_hourLight_sg = ngong_tmac_df.groupby("hour")["light"]
    noberoi_hourLight_sg = noberoi_tmac_df.groupby("hour")["light"]
    asadahiro_hourLight_sg = asadahiro_tmac_df.groupby("hour")["light"]

    ngong_hourLight_avg = ngong_hourLight_sg.aggregate("mean")
    noberoi_hourLight_avg = noberoi_hourLight_sg.aggregate("mean")
    asadahiro_hourLight_avg = asadahiro_hourLight_sg.aggregate("mean")

    #humidity
    ngong_hourHumidity_sg = ngong_tmac_df.groupby("hour")["humidity"]
    noberoi_hourHumidity_sg = noberoi_tmac_df.groupby("hour")["humidity"]
    asadahiro_hourHumidity_sg = asadahiro_tmac_df.groupby("hour")["humidity"]

    ngong_hourHumidity_avg = ngong_hourHumidity_sg.aggregate("mean")
    noberoi_hourHumidity_avg = noberoi_hourHumidity_sg.aggregate("mean")
    asadahiro_hourHumidity_avg = asadahiro_hourHumidity_sg.aggregate("mean")

    #sound
    ngong_hourSound_sg = ngong_tmac_df.groupby("hour")["sound"]
    noberoi_hourSound_sg = noberoi_tmac_df.groupby("hour")["sound"]
    asadahiro_hourSound_sg = asadahiro_tmac_df.groupby("hour")["sound"]

    ngong_hourSound_avg = ngong_hourSound_sg.aggregate("mean")
    noberoi_hourSound_avg = noberoi_hourSound_sg.aggregate("mean")
    asadahiro_hourSound_avg = asadahiro_hourSound_sg.aggregate("mean")

    #start to groupby with temp for day groupby
    ngong_dayTemp_sg=ngong_tmac_df.groupby("day")["temperature"]
    noberoi_dayTemp_sg=noberoi_tmac_df.groupby("day")["temperature"]
    asadahiro_dayTemp_sg=asadahiro_tmac_df.groupby("day")["temperature"]

    ngong_dayTemp_avg=ngong_dayTemp_sg.aggregate("mean")
    noberoi_dayTemp_avg=noberoi_dayTemp_sg.aggregate("mean")
    asadahiro_dayTemp_avg=asadahiro_dayTemp_sg.aggregate("mean")
    
    #sens sound
    ngong_daySensSound_sg = ngong_tmac_df.groupby("day")["int1"]
    noberoi_daySensSound_sg = noberoi_tmac_df.groupby("day")["int1"]
    asadahiro_daySensSound_sg = asadahiro_tmac_df.groupby("day")["int1"]

    ngong_daySensSound_avg = ngong_daySensSound_sg.aggregate("mean")
    noberoi_daySensSound_avg = noberoi_daySensSound_sg.aggregate("mean")
    asadahiro_daySensSound_avg = asadahiro_daySensSound_sg.aggregate("mean")

    #light
    ngong_dayLight_sg = ngong_tmac_df.groupby("day")["light"]
    noberoi_dayLight_sg = noberoi_tmac_df.groupby("day")["light"]
    asadahiro_dayLight_sg = asadahiro_tmac_df.groupby("day")["light"]

    ngong_dayLight_avg = ngong_dayLight_sg.aggregate("mean")
    noberoi_dayLight_avg = noberoi_dayLight_sg.aggregate("mean")
    asadahiro_dayLight_avg = asadahiro_dayLight_sg.aggregate("mean")

    #humidity
    ngong_dayHumidity_sg = ngong_tmac_df.groupby("day")["humidity"]
    noberoi_dayHumidity_sg = noberoi_tmac_df.groupby("day")["humidity"]
    asadahiro_dayHumidity_sg = asadahiro_tmac_df.groupby("day")["humidity"]

    ngong_dayHumidity_avg = ngong_dayHumidity_sg.aggregate("mean")
    noberoi_dayHumidity_avg = noberoi_dayHumidity_sg.aggregate("mean")
    asadahiro_dayHumidity_avg = asadahiro_dayHumidity_sg.aggregate("mean")

    #sound
    ngong_daySound_sg = ngong_tmac_df.groupby("day")["sound"]
    noberoi_daySound_sg = noberoi_tmac_df.groupby("day")["sound"]
    asadahiro_daySound_sg = asadahiro_tmac_df.groupby("day")["sound"]

    ngong_daySound_avg = ngong_daySound_sg.aggregate("mean")
    noberoi_daySound_avg = noberoi_daySound_sg.aggregate("mean")
    asadahiro_daySound_avg = asadahiro_daySound_sg.aggregate("mean")

    #groupby motion + mean sound & senSound with dotplot graphs
    #this is sound
    tmac_motionSound_sg=tmac_df.groupby("motion")["sound"]
    tmac_motionSound_avg = tmac_motionSound_sg.aggregate("mean")

    motion=tmac_df["motion"]
    

    #this is sensSound
    tmac_motionSensSound_sg=tmac_df.groupby("motion")["int1"]
    tmac_motionSensSound_avg = tmac_motionSensSound_sg.aggregate("mean")
    #also gathering some box & whisker plot data for each person on motion + sound & senSound (will plot in 2 different graphs)
    #setting up the motion & non-motion df, then getting the sound & senSound data for each
    ngong_motion_df=ngong_tmac_df[ngong_tmac_df.loc[:,"motion"]==1]
    ngong_noMotion_df=ngong_tmac_df[ngong_tmac_df.loc[:,"motion"]==0]

    noberoi_motion_df=noberoi_tmac_df[noberoi_tmac_df.loc[:,"motion"]==1]
    noberoi_noMotion_df=noberoi_tmac_df[noberoi_tmac_df.loc[:,"motion"]==0]

    asadahiro_motion_df=asadahiro_tmac_df[asadahiro_tmac_df.loc[:,"motion"]==1]
    asadahiro_noMotion_df=asadahiro_tmac_df[asadahiro_tmac_df.loc[:,"motion"]==0]

    #starts setting up the dataframes with sound data with motion, no motion for each person
    ngong_sound_motion=ngong_motion_df.loc[:,"sound"]
    ngong_sound_noMotion=ngong_noMotion_df.loc[:,"sound"]
    ngong_sensSound_motion=ngong_motion_df.loc[:,"int1"]
    ngong_sensSound_noMotion=ngong_noMotion_df.loc[:,"int1"]

    noberoi_sound_motion=noberoi_motion_df.loc[:,"sound"]
    noberoi_sound_noMotion=noberoi_noMotion_df.loc[:,"sound"]
    noberoi_sensSound_motion=noberoi_motion_df.loc[:,"int1"]
    noberoi_sensSound_noMotion=noberoi_noMotion_df.loc[:,"int1"]

    asadahiro_sound_motion=asadahiro_motion_df.loc[:,"sound"]
    asadahiro_sound_noMotion=asadahiro_noMotion_df.loc[:,"sound"]
    asadahiro_sensSound_motion=asadahiro_motion_df.loc[:,"int1"]
    asadahiro_sensSound_noMotion=asadahiro_noMotion_df.loc[:,"int1"]
    
    #finally, ends off with gathering data for graphing some histograms of sound & sensSound to track frequency of loudness of sound 
    sensSound=tmac_df.loc[:,"int1"]
    sound=tmac_df.loc[:,"sound"]

    #starts plotting the graphs, first setting fig size, window 1 is mostly made by Andrew Sadahiro
    fig = plt.figure(figsize = (12, 6))
    #temp graphs
    temp_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 1)
    temp_plot.set_title("Temperature")
    temp_plot.set_xlabel("Hour")
    temp_plot.set_ylabel("Celcius")
    temp_plot.plot(ngong_hourTemp_avg, label = "Nathan")
    temp_plot.plot(noberoi_hourTemp_avg,label = "Nihaal")
    temp_plot.plot(asadahiro_hourTemp_avg,label = "Andrew")
    temp_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #sensitive sound graph
    sens_sound_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 2)
    sens_sound_plot.set_title("Sensitive Sound")
    sens_sound_plot.set_xlabel("Hour")
    sens_sound_plot.set_ylabel("dB")
    sens_sound_plot.plot(ngong_hourSensSound_avg, label="Nathan")
    sens_sound_plot.plot(noberoi_hourSensSound_avg,label="Nihaal")
    sens_sound_plot.plot(asadahiro_hourSensSound_avg,label="Andrew")
    sens_sound_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #humidity graph
    humidity_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 4)
    humidity_plot.set_title("Humidity")
    humidity_plot.set_xlabel("Hour")
    humidity_plot.set_ylabel("g/Kg")
    humidity_plot.plot(ngong_hourHumidity_avg, label="Nathan")
    humidity_plot.plot(noberoi_hourHumidity_avg,label="Nihaal")
    humidity_plot.plot(asadahiro_hourHumidity_avg,label="Andrew")
    humidity_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #sound graph
    sound_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 5)
    sound_plot.set_title("Sound")
    sound_plot.set_xlabel("Hour")
    sound_plot.set_ylabel("Sound Value")
    sound_plot.plot(ngong_hourSound_avg, label="Nathan")
    sound_plot.plot(noberoi_hourSound_avg,label="Nihaal")
    sound_plot.plot(asadahiro_hourSound_avg,label="Andrew")
    sound_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #light graph
    light_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 6)
    light_plot.set_title("Light")
    light_plot.set_xlabel("Hour")
    light_plot.set_ylabel("Lumens")
    light_plot.plot(ngong_hourLight_avg, label="Nathan")
    light_plot.plot(noberoi_hourLight_avg,label="Nihaal")
    light_plot.plot(asadahiro_hourLight_avg,label="Andrew")
    light_plot.legend(loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    #creates the first window
    plt.show()

    #below is made by Nathan Gong and Nihaal Oberoi
    #clears subplots and data so I can create 2nd window later
    plt.clf()

    #creates 2nd window figures
    fig = plt.figure(figsize = (12, 6))

    #temp graphs
    temp_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 1)
    temp_plot.set_title("Temperature")
    temp_plot.set_xlabel("Date")
    temp_plot.set_ylabel("Celcius")
    temp_plot.plot(ngong_dayTemp_avg, label = "Nathan")
    temp_plot.plot(noberoi_dayTemp_avg,label = "Nihaal")
    temp_plot.plot(asadahiro_dayTemp_avg,label = "Andrew")
    temp_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #sensitive sound graph
    sens_sound_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 2)
    sens_sound_plot.set_title("Sensitive Sound")
    sens_sound_plot.set_xlabel("Date")
    sens_sound_plot.set_ylabel("dB")
    sens_sound_plot.plot(ngong_daySensSound_avg, label="Nathan")
    sens_sound_plot.plot(noberoi_daySensSound_avg,label="Nihaal")
    sens_sound_plot.plot(asadahiro_daySensSound_avg,label="Andrew")
    sens_sound_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #made by Nihaal Oberoi
    #humidity graph
    humidity_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 4)
    humidity_plot.set_title("Humidity")
    humidity_plot.set_xlabel("Date")
    humidity_plot.set_ylabel("g/Kg")
    humidity_plot.plot(ngong_dayHumidity_avg, label="Nathan")
    humidity_plot.plot(noberoi_dayHumidity_avg,label="Nihaal")
    humidity_plot.plot(asadahiro_dayHumidity_avg,label="Andrew")
    humidity_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #sound graph
    sound_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 5)
    sound_plot.set_title("Sound")
    sound_plot.set_xlabel("Date")
    sound_plot.set_ylabel("Sound values")
    sound_plot.plot(ngong_daySound_avg, label="Nathan")
    sound_plot.plot(noberoi_daySound_avg,label="Nihaal")
    sound_plot.plot(asadahiro_daySound_avg,label="Andrew")
    sound_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #light graph
    light_plot = fig.add_subplot(SUBPLOT_ROW, SUBPLOT_COLUMN, 6)
    light_plot.set_title("Light")
    light_plot.set_xlabel("Date")
    light_plot.set_ylabel("Lumens")
    light_plot.plot(ngong_dayLight_avg, label="Nathan")
    light_plot.plot(noberoi_dayLight_avg,label="Nihaal")
    light_plot.plot(asadahiro_dayLight_avg,label="Andrew")
    light_plot.legend(loc='upper left')
    plt.xticks(rotation=45)

    #finally, the rest is made by Nathan Gong
    plt.tight_layout()
    #shows 2nd window
    plt.show()
    #delete the 2nd window's data to allow for 3rd window's data to pop up (when 2nd window is closed)
    plt.clf()

    #create the figure for the 3rd window
    fig = plt.figure(figsize = (12, 6))

    #starts with histograms
    #starts with sound
    hist_sound_plot = fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 1)
    hist_sound_plot.hist(sound, bins=3, color="lightblue", ec="black")
    hist_sound_plot.set_title("Histogram of Sound")
    hist_sound_plot.set_xlabel("Sound bins")
    hist_sound_plot.set_ylabel("Sound")

    #continues with sensitive sound
    hist_sensSound_plot = fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 2)
    hist_sensSound_plot.hist(sensSound, bins=3, color="lightblue", ec="black")
    hist_sensSound_plot.set_title("Histogram of Sensitive Sound")
    hist_sensSound_plot.set_xlabel("Sensitive Sound Bins")
    hist_sensSound_plot.set_ylabel("Sensitive Sound")

    #continues with scatter plots
    # draw the scatter plot for sound
    scatter_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,3)
    scatter_plot.scatter(motion,sound)
    #add title, x and y labels
    scatter_plot.set_title("Motion and Sound")
    scatter_plot.set_xlabel("Motion")
    scatter_plot.set_ylabel("Sound")  

    #draw the scatter plot for sensitive sound
    scatter_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,4)
    scatter_plot.scatter(motion,sensSound)
    #add title, x and y labels
    scatter_plot.set_title("Motion and Sensitive Sound")
    scatter_plot.set_xlabel("Motion")
    scatter_plot.set_ylabel("Sensitive Sound")   
    
    #finally, plotting the box plots
    #starts with boxplot of sensitive sounds between people (of motion and non-motion)
    box_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,5)
    #add title, x and y labels
    box_plot.set_title("Senstive Sound and Motion")
    box_plot.set_xlabel("Category")
    box_plot.set_ylabel("Sens Sound")
    #draw boxplot
    box_plot.boxplot([ngong_sound_motion,ngong_sound_noMotion,noberoi_sound_motion,noberoi_sound_noMotion, asadahiro_sound_motion,asadahiro_sound_noMotion], labels=["Nathan - Motion", "Nathan - No motion", "Nihaal - Motion", "Nihaal - No motion", "Andrew - Motion", "Andrew - No motion"])

    box_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,6)
    #ends with boxplot of reg sounds between people (of motion and non-motion)
    box_plot.set_title("Sound and Motion")
    box_plot.set_xlabel("Category")
    box_plot.set_ylabel("Sound")
    #draw boxplot
    box_plot.boxplot([ngong_sensSound_motion,ngong_sensSound_noMotion,noberoi_sensSound_motion,noberoi_sensSound_noMotion, asadahiro_sensSound_motion,asadahiro_sensSound_noMotion], labels=["Nathan - Motion", "Nathan - No motion", "Nihaal - Motion", "Nihaal - No motion", "Andrew - Motion", "Andrew - No motion"])
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("There was an error when trying to get from datalogger at https://eps-datalogger.herokuapp.com/api/:", e)
