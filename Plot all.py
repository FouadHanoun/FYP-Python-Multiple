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
T=[]
p=[]
tt=[]
x=[]

size=0


for z in range(0,6):
    features.append([])
    for j in range(0,8):
        features[z].append([])
    timestamp.append([])
    tt.append([])
    x.append([])
    T.append([])
    p.append([])

for line in file:
    if(":" not in line):
        line=line.split(" ")
        for i in range(0,8):
            features[body][i].append(int(line[i]))
    else:
        line=line.split("-")
        body=int(line[0])
        time=line[1].split(":")
        timestamp[body].append(float(time[0])*3600+float(time[1])*60+float(time[2].strip('\n')))



for z in range(0,6):
    if(len(timestamp[z])==0):
        break
    tt[z]=np.array(timestamp[z])
    x[z]=np.linspace(tt[z].min(),tt[z].max(),25)
    size+=1



for j in range(0,size):
    plt.figure("body "+str(j))
    plt.ylim(ymax = 100, ymin = 0)
    for z in range(0,8):
        T[j].append(np.array(features[j][z]))
        p[j].append(spline(tt[j],T[j][z],x[j]))
        plt.plot(x[j],p[j][z],label=emotions[z])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
        

plt.show()
