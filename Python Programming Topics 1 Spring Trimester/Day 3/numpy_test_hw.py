import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#challenge 1

#setting x & y data
x_data=np.array([0,1,2,3,4])
y_data=np.array([50,10,30,10,50])

#plotting the data, adding title + labels
plt.plot(x_data,y_data,ls="-",color="green")
plt.title("Challenge 1: W line chart")
plt.xlabel("x values for a W")
plt.ylabel("y values for a W")

#shows the data
plt.show()




#challenge 2

#creating 100 x & 100 y values
x_values_100=np.arange(0,100)
y_values_random = np.random.choice(
    [10,50,100,200,700],p=[0.1,0.55,0.05,0.2,0.1],size=(100)
)

#plotting the data, adding a title
plt.title("100 Random Data points")
plt.plot(x_values_100,y_values_random,color="black", ls=":")

#showing the data
plt.show()





#extra challenge
sensors_df=pd.read_json('Python Programming Topics 1 Spring Trimester\Day 3\midterm_sensors.json')

temp_data=sensors_df["temperature"].to_numpy()
date_data=sensors_df["time_created"].to_numpy()

plt.title("Sensors line graph")
plt.plot(date_data,temp_data,color="black")
plt.show()