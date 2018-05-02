import os
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.interpolate import spline

emotions=["neutral","happiness","sadness","pride","guilt","defensive","interest","bored","impatience"]

filename="plotting.txt"
file = open(filename,'r')
timestamp=[]
features=[]
i=0
j=0
for z in range(0,9):
    features.append([])

for line in file:
    if(":" not in line):
        line=line.split(" ")
        
        for i in range(0,9):
            features[i].append(int(line[i]))
    else:
        time=line.split(":")
        timestamp.append(float(time[1])*60+float(time[2].strip('\n')))

T=[]
p=[]
tt=np.array(timestamp)
x=np.linspace(tt.min(),tt.max(),100)
for z in range(0,8):
    T.append(np.array(features[z+1]))
    p.append(spline(tt,T[z],x))
    plt.figure(emotions[z+1])
    plt.plot(x,p[z])
plt.ylim(ymax = 100, ymin = 0)
plt.show()
