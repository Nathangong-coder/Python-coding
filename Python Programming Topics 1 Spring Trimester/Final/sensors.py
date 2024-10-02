#Nathan Gong
#Sudo Sensei
#Programming 2: Topics
#April 6, 2023
#Midterm MA: Sensors in TMAC 007


# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: Unlicense
"""
CircuitPython Simple Example for BME280 and LC709203 Sensors
"""
import time
import board
import digitalio
import adafruit_veml7700
from adafruit_bme280 import basic as adafruit_bme280
from digitalio import DigitalInOut, Direction, Pull
import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import analogio


# Create sensor objects, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
veml7700 = adafruit_veml7700.VEML7700(i2c)
soundSensor= analogio.AnalogIn(board.A0)
sensitiveSoundSensor=analogio.AnalogIn(board.A5)
#Initilizating motion_fact, second counter, and other data variables for temperature, sound, humidity, pressure, and light.
motion_fact=0
counter=0 #set to 0 to count seconds later
temperature=0
sound=0
humidity=0
altitude=0
pressure=0
lux=0
ambient_light=0
ambient_light_Sum=0
soundSum=0
sensSoundSum=0

# changing this to match your location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1009.144

#for motion sensor
motion = DigitalInOut(board.D5)  # For Feather M0 Express, Feather M4 Express
motion.pull = Pull.DOWN

#get wifi creds from secrets.py
try:
    #get creds
    from secrets import secrets
except Exception as e:
    print("Error: Unable to get wifi creds from secrets.py, with error:", e)
    raise

#connect to eps wifi
try:
    print("Connecting to:",secrets["ssid"])
    wifi.radio.connect(secrets["ssid"], secrets["password"])
    print("Connected to wifi successfully!")
    print("My ip address is", wifi.radio.ipv4_address)

    #ping google server to test
    google_address = ipaddress.ip_address("8.8.4.4")
    print("pinging google")
    print(wifi.radio.ping(google_address)*1000)

except Exception as e:
    print("Error connecting to our testing wifi connection, error:",e)

def data_logger_string(username, device_id, area, temp, light, humidity, sound, motion, tilt, mode, sensSoundAvg):
    """
        This function builds a url string to upload  data to the datalogger

        Parameters:
            username (string): student eps username (e.g. "msudo")
            device_id (string): unique device id (e.g. "msudo_feather1")
            area (string): physical location (e.g. "tmac007")
            temp (float): temperature in celcius (e.g. 17.5 )
            light (float): lux or ambient light - class must decide (e.g. 202.1)
            humidity (float): humidity (e.g. 50.0)
            motion (0 or 1): 1 if motion was detected, 0 if not (e.g. 1)
            sound (0 or 1 or int): 1 if sound was detected, 0 if not (e.g. 0), int for analog reading
            tilt (0 or 1): 1 if tilt was detected, 0 if not (e.g. 1)
            mode (string): Class' current development phase - class must decide (e.g. "s2023_test1")

        Returns:
             string used to upload data to datalogger database
    """
 # build the data logger string
    datalogger_url_str = "https://eps-datalogger.herokuapp.com/api/data/" \
    + username + "/add?device_id=" + device_id + "&temperature=" + str(temp)\
    + "&area=" + area + "&light=" + str(light) + "&humidity=" + str(humidity)\
    + "&motion=" + str(motion) + "&sound=" + str(sound) + "&tilt=" + str(tilt) + "&string1=" + mode + "&int1=" + str(sensSoundAvg) + "&float1=" + str(0)
    return datalogger_url_str


# create requests object to send data to the database
# note, if the pool and request variables have already been initialized previously in your code, delete the next two lines of code. You do not need them and they will cause an error on request.post()
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

while True:
    #resets variables back to 0
    motion_fact=0
    sensSoundSum=0
    soundSum=0
    #prints all the required data out
    print("\nTemperature: {:.1f} C".format(bme280.temperature))
    print("Humidity: {:.1f} %".format(bme280.relative_humidity))
    print("Pressure: {:.1f} hPa".format(bme280.pressure))
    print("Altitude: {:.2f} meters".format(bme280.altitude))
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    print("Sound sensor:", soundSensor.value)
    print("Sensitive sound sensor:", sensitiveSoundSensor.value)

    #updating variable data that will be sent to the cloud
    temperature=bme280.temperature
    humidity=bme280.relative_humidity
    pressure=bme280.pressure
    altitude=bme280.altitude
    ambient_light=veml7700.light
    lux=veml7700.lux
    sound=soundSensor.value
    sensSound=sensitiveSoundSensor.value
    #This loop checks every 1 milisecond if motion is true in a 10 minute loop
    while counter<600000:
        if motion.value:
            #if tilt is true, then this loop will break
            motion_fact=1
        if counter%200:
            soundSum+=soundSensor.value
            sensSoundSum+=sensitiveSoundSensor.value
            ambient_light_Sum+=veml7700.light
        time.sleep(0.001)
        counter+=1

    #Prints out if it moved or not in the 10 minute loop
    if motion_fact==1:
        print("Motion: True")
    if motion_fact==0 and counter>1:
        print("Motion: False")


    #calculating sound averages
    soundAvg=soundSum/counter
    soundAvg=int(soundAvg)
    sensSoundAvg=sensSoundSum/counter
    sensSoundAvg=int(sensSoundAvg)
    ambient_light_Avg=ambient_light_Sum/counter
    ambient_light_Avg=int(ambient_light_Avg)

    #resets counter for when next time the motion is checked within 10 minute timeframe
    counter=0

    #build data string
    data_str = data_logger_string("ngong", "ngong_feather1", "teamNONGAS_offices", temperature, ambient_light_Avg, humidity, soundAvg, motion_fact, 0, "s2023-ma2-Final",sensSoundAvg)

    #upload data string to datalogger db
    try:
        print("uploading the following str to datalogger db:", data_str)
        response = requests.post(data_str)
        print("database upload success with result:", response.json())
    except Exception as e:
        print("Error uploading to datalogger db:", e)



