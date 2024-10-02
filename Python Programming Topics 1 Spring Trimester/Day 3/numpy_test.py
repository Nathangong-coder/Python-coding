import numpy as np
import matplotlib.pyplot as plt


#manual data
x_data = np.array([0,1,2,3,4,5])
y_data = np.array([10,690,4200,240,50,120])
new_y_data=np.array([2000,50,2000,50,2000,2500])

plt.plot(x_data,y_data, ls="-")
plt.title("manual data table")
plt.xlabel("x values")
plt.ylabel("y values")


# change line style and color
plt.plot(new_y_data,ls=':', c='hotpink',linewidth="10")


plt.show()

#now let's generate data automatically with numpy
x_numpy = np.arange(0,50)
y_numpy = np.linspace(0,18,10)

print(y_numpy)

#todo- chart this on a line

#generate a chart with random numbers
x_numpy_50 = np.arange(50)
y_numpy_random = np.random.choice(
    [0,10,20], p=[0.5,0.25,0.25], size=(50)
)

print(y_numpy_random)
plt.title("random data")
plt.plot(x_numpy_50,y_numpy_random,color="green")
plt.show()