import numpy as numpy
from numpy import *
import pylab as pylab 
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import animation

fig=plt.figure()
ax=plt.axes(xlim=(0,100),ylim=(0,100))
line=ax.plot([],[],'ro')[0]
n=1000
x=[]
y=[]
vx=[]
vy=[]

for i in range(n):
    x.append(random()*10)
    y.append(random()*10)
    vx.append(random()-0.5)
    vy.append(random()-0.5)
    
def bouncing_balls(i):
    global x
    global y
    global vx
    global vy
    for a in range(n):
        if x[a]>=100 or x[a]<=0:
            vx[a]=-vx[a]
            x[a]=x[a]+vx[a]
        else:
            x[a]=x[a]+vx[a]
            
            
            
    for a in range(n):
        if y[a]>=100 or y[a]<=0:
            vy[a]=-vy[a]
            y[a]=y[a]+vy[a]
        else:
            y[a]=y[a]+vy[a]
            
    line.set_data(x,y)
    return line,
    
    
anim=animation.FuncAnimation(fig,bouncing_balls,interval=10)    
plt.show()
