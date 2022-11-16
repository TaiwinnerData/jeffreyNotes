# this script is for test pyplot
import matplotlib.pyplot as plt

# line 1 points
x1 = [1, 2, 3]
y1 = [2, 4, 7]


# plotting the line 1 points
plt.scatter(x1, y1, label = "line 1")
plt.plot(x1, y1, color = 'blue')
plt.show()
