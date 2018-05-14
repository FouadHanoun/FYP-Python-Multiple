import time
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import os
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.interpolate import spline


emotions_list=["happiness","sadness","pride","guilt","defensive","interest","bored","impatience"]

filename="plotting.txt"
file = open(filename,'r')
timestamp=[]
emotions=[]
i=0
j=0
T=[]
p=[]
tt=[]
x=[]

size=0


for z in range(0,6):
    emotions.append([])
    for j in range(0,8):
        emotions[z].append([])
    timestamp.append([])
    tt.append([])
    x.append([])
    T.append([])
    p.append([])

'''                                                   ----             FEATURES            ----


HeadBackward HeadBentForward HeadOnHand_Left HeadOnHand_RightHandOnHead_Left HandOnHead_Right SpineForward SpineBackward ShouldersForward ShouldersRaisedArmsAtTrunk
ArmsRaisedShoulder HandsOnKnees CrossedArms ArmsRaisedUp ArmsExtendedDown HandsBehindHead HandOnNeck_Left HandOnNeck_Right


'''

def fill(p,n):
    fx=open(n,'r')
    x=[]
    j=0
    for l in fx:
        x.append([])
        l=l.split(" ")
        for i in range (0,p):
            x[j].append(float(l[i]))
        j+=1
    fx.close()
    return x



#Fill the X features list form the X.txt file
X=fill(19,"X.txt")

#Fill the Y results from the Y.txt file
y=fill(8,"Y.txt")

#Train the system
k=MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X, y)

                                 
filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
features = []
i=0
features.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

for line in file:
    if (":" not in line):
        features[0][i]=float(line.split(" ")[1].strip('\n'))
        i+=1
    else:
        line=line.split("-")
        body=int(line[0])-1
        time=line[1].split(":")
        timestamp[body].append(float(time[0])*3600+float(time[1])*60+float(time[2].strip('\n')))
    if (i==19):
        #Test the system
        emotion=k.predict(features)
        cc=0
        for u in emotion:
            for em in u:
                emotions[body][cc].append(em)
                cc+=1
        i=0

file.close()

for z in range(0,6):
    if(len(timestamp[z])==0):
        break
    tt[z]=np.array(timestamp[z])
    x[z]=np.linspace(tt[z].min(),tt[z].max(),50)
    size+=1


for j in range(0,size):
    plt.figure("body "+str(j))
    plt.ylim(0,105)
    for z in range(0,8):
        T[j].append(np.array(emotions[j][z]))
        p[j].append(spline(tt[j],T[j][z],x[j]))
        plt.plot(x[j],p[j][z],label=emotions_list[z])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
        

plt.show()
