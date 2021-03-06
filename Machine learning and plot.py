import time
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import os
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from scipy.interpolate import spline


from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score, KFold
from keras.models import Sequential
from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor



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


def baseline_model():
    model = Sequential()
    model.add(Dense(19, input_dim=19, activation='relu'))
    model.add(Dense(8))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


#Fill the X features list form the X.txt file
X=fill(19,"X.txt")

#Fill the Y results from the Y.txt file
y=fill(8,"Y.txt")

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

                         
filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
features = []
i=0
features.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


seed = 7
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=100, verbose=False)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, np.array(X), np.array(y), cv=kfold)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

estimator.fit(np.array(X), np.array(y))
prediction = estimator.predict(np.array(X))
print(mean_squared_error((y), prediction))

'''

for line in file:
    if (":" not in line):
        features[0][i]=float(line.split(" ")[1].strip('\n'))
        i+=1
    else:
        line=line.split("-")
        body=int(line[0])
        time=line[1].split(":")
        timestamp[body].append(float(time[0])*3600+float(time[1])*60+float(time[2].strip('\n')))
    if (i==19):
        #Test the system
        emotion=estimator.predict(np.array(features))
        cc=0
        for u in emotion:
            emotions[body][cc].append(max(0,min(u*100,100)))
            cc+=1
        i=0

file.close()
for z in range(0,6):
    if(len(timestamp[z])==0):
        break
    tt[z]=np.array(timestamp[z])
    x[z]=np.linspace(tt[z].min(),tt[z].max(),20)
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
'''
