#Nathan Gong
#Sudo Sensei
#Programming 2: Topics
#April 6, 2023
#Midterm MA: Sensors in TMAC 007

#Prompts (note: alt+z to see text wrap):

#Individual:What was your guiding question about the TMAC 007 classroom?
    #When is door opened in TMAC 007? How loud is the door when the door is opened(usually)? What is the humidity and the temperature when the door is opened (usually)? 
    #How strong is the light near/through the door?

#What patterns did you find about the TMAC 007 classroom?
    #I found that the TMAC 007 classroom often was very noisy during the day, often being 33000. 
    #Though, interestingly, when the door was opened, the noise was still the same. 
    #I also found that the temperature became higher when the door was opened.
    #I found that the light was brighter during the day and darker during the night. I also found that the noise was louder in the day and quieter in the night, though interestingly, the quiet parts of the day was similar to that of the night. I found that the temperature decreased when people weren't there, but that the humidity stayed the same. Finally, I found that the door was opened much less, almost none when it became closer to the night.

#What patterns were you expecting to see and observed in your data that made sense to you, during class?
    #It made sense that temperature and frequency of the door triggering the tilt sensor went down during the night and afterschool. It also made sense that the noise was quieter in the night and that it was darker during the night. 

#What patterns were you not expecting to see and surprised you? Why do you think this happened?

    #I was expecting to see that the temperature go down when the door was opened, but the temperature went up when the door was opened. I think this happened because the temperature outside the classroom was hotter, with it having less air conditioning.
 
    #I also was expecting the noise to change to be louder when the door was opened, but there not a big change, in fact, it sometimes became quieter. I think this happened because the classroom was probably constantly full of people so the noise the students made was similar in decibels to the noise the door made. 

    #I was also not expecting the decibels of the night to be that similar to the decibels of the morning, as the graphs showed them being almost the same (besides a few peaks in the morning). I think this happened because the air conditioning was making the majority of the sound, and may have even drowned out the sound of the door (which was already pretty quiet)



#In pairs: What did you discover when comparing your results with a peer? 
    #I discovered that my light was alarmingly low, especially compared to other light sensors in the class. I also discovered that our volume sensors, which were near the door, remained pretty constant, even when our tilt sensors detected motion.

#What aligns with what you expected? 
    #The sound was about the same for all the sensors that I compared near the door, which was something that I expected. We also got the same temperature, light, noise, and tilt/motion frequency correlation when it approached the nighttime.

#What surprised you? 
    #I was extremely surprised that all of our sound sensors did not change when the door was opened. I also was very surprised that one of my classmates had a humidity sensor that went up in the night, since the rest of the classmates that I compared with had humidity sensors that stayed constant, like me. I was also surprised how much lower my light sensors were compared to everyone else, as I used the same units (ambient light) but had hundreds of units less than they did.

#If something surprised you, what do you think is the explanation for it?
    #I think the reason that the sound remained pretty constant even when the door was opened during the day was because that people in the room was about the same volume as the door, thereby making the door not have much sound. I think one of my classmate had a humidity sensor that went up in the night because that person probably put the sensor near the vent, which probably was set to be more humid during the night. Finally, I think my light sensor was much lower than everyone else's because the glass in the TMAC 007 probably does not pass in as much light as I thought, and was able to pass in way less light compared to the light in the classroom.


#Reflection: How did you challenge yourself in this project?
    #I challenged myself mainly by solving my coding issues, since there were many errors when collecting data with my sensors. I also challenged myself by using different sensors, including the sound sensor, which I needed some help to get working.

#Anything else?
    #There were some unexplained breaks in data for 10-20 minutes, and it seemed that my sensor was tampered with constantly, as there was a period of time where my data updated multiple times within a 10 minute period (meaning that the sensor must have refreshed and the tilt sensor was trigerred during that time frame). I think that either the power glitched or someone tampered my sensors for some reason. I am curious what the actual reason is and how I can prevent this in the future.


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
from adafruit_lc709203f import LC709203F, PackSize
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
#Initilizating tilt_fact, second counter, and other data variables for temperature, sound, humidity, pressure, and light.
tilt_fact=0
counter=0 #set to 0 to count seconds later
temperature=0
sound=0
humidity=0
altitude=0
pressure=0
lux=0
ambient_light=0

# changing this to match your location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1009.144

#for tilt sensor
tilt = DigitalInOut(board.D5)  # For Feather M0 Express, Feather M4 Express
tilt.direction = Direction.INPUT
tilt.pull = Pull.UP

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
    
def data_logger_string(username, device_id, area, temp, light, humidity, sound, motion, tilt, mode):
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

    datalogger_url_str = "https://eps-datalogger.herokuapp.com/api/data/" \
    + username + "/add?device_id=" + device_id + "&temperature=" + str(temp)\
    + "&area=" + area + "&light=" + str(light) + "&humidity=" + str(humidity)\
    + "&motion=" + str(motion) + "&sound=" + str(sound) + "&tilt=" + str(tilt) + "&string1=" + mode
    return datalogger_url_str


# create requests object to send data to the database
# note, if the pool and request variables have already been initialized previously in your code, delete the next two lines of code. You do not need them and they will cause an error on request.post()
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

while True:
    #prints all the required data out
    print("\nTemperature: {:.1f} C".format(bme280.temperature))
    print("Humidity: {:.1f} %".format(bme280.relative_humidity))
    print("Pressure: {:.1f} hPa".format(bme280.pressure))
    print("Altitude: {:.2f} meters".format(bme280.altitude))
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    print("Sound sensor:", soundSensor.value)

    #updating variable data that will be sent to the cloud
    temperature=bme280.temperature
    humidity=bme280.relative_humidity
    pressure=bme280.pressure
    altitude=bme280.altitude
    ambient_light=veml7700.light
    lux=veml7700.lux
    sound=soundSensor.value

    #This loop checks every 1 milisecond if tilt is true in a 10 minute loop
    while counter<600000:
        if tilt.value:
            #if tilt is true, then this loop will break
            tilt_fact=1
            break
        else:
            tilt_fact=0
        time.sleep(0.001)
        counter+=1

    #Prints out if it tilted or not in the 10 minute loop
    if tilt_fact==1:
        print("Tilt: True")
    if tilt_fact==0 and counter>1:
        print("Tilt: False")

    
    #build data string
    data_str = data_logger_string("ngong_midterm1", "ngong_feather1", "tmac007", temperature, ambient_light, humidity, sound, 0, tilt_fact, "s2023_ma1" )

    #upload data string to datalogger db
    try:
        print("uploading the following str to datalogger db:", data_str)
        response = requests.post(data_str)
        print("database upload success with result:", response.json())
    except Exception as e:
        print("Error uploading to datalogger db:", e)
    
    #Sleeps for the remainder of the 10 minutes (will be 0 if tilt fact=false but 10 if tilted immediately)
    time.sleep(600-0.001*counter)
    #resets counter for when next time the tilt is checked within 10 minute timeframe
    counter=0


