"""
For this project, you will have a generate a sine vs cosine curve. 
You will need to use the numpy library to access the sine and cosine functions. 
You will also need to use the matplotlib library to draw the curve. 
To make this more difficult, make the graph go from -360° to 360°, 
with there being a 180° difference between each point on the x-axis.

Another change

"""
import numpy as np
import matplotlib.pyplot as plt

#Remember to put .pyplot in order for the plotting to work

# Degrees
t = [i for i in range(-360, 361)]

# Converting to radians
x = [i*(np.pi/180) for i in t]


# Plotting


plt.title("Sine vs Cosine graph")

# .sin() and .cos() only recieves radians as inputs

plt.plot(t, np.sin(x), label = 'Sines', color = "orange")

plt.plot(t, np.cos(x), label = "Cosines", color = "blue")

plt.xticks(np.arange(-360,361, step=180))

# top right hand corner
plt.legend(bbox_to_anchor=(1, 1),
           bbox_transform=plt.gcf().transFigure)

plt.xlabel("Angles")
plt.ylabel("Values")
plt.show()





