import numpy as np
import matplotlib.pyplot as plt

#define data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 5, 6, 7, 9, 12, 16, 19])

#find line of best fit
a, b = np.polyfit(x, y, 1)

#add points to plot
plt.scatter(x, y)

#add line of best fit to plot
plt.plot(x, a*x+b)      

plt.show()
