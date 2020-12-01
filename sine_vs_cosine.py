"""
For this project, you will have a generate a sine vs cosine curve. 
You will need to use the numpy library to access the sine and cosine functions. 
You will also need to use the matplotlib library to draw the curve. 
To make this more difficult, make the graph go from -360° to 360°, 
with there being a 180° difference between each point on the x-axis.

Another change

"""


import numpy as np
import matplotlib as plt


# Degrees
t = [0,30,45,60,90]

# Converting to radians
x = [i*(np.pi/180) for i in t]

# Plotting into 
plt.plot(x, np.sin(x))





