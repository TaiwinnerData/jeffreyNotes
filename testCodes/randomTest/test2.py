import matplotlib.pyplot as plt
import numpy as np


x = [1, 3, 5, 7]
y = [2, 6, 10, 14]

x = np.array(x)
y = np.array(y)

a, b = np.polyfit(x, y, 1)

plt.scatter(x, y)
plt.plot(x, a*x+b)
plt.show()
