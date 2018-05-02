import time
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split



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
y=fill(5,"Y.txt")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

#Train the system
k=MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X, y)

k=MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X_train, y_train).predict(X_test)
for i in range (0,147):
    #print(mean_absolute_error(y_test[i], k[i]))
    if(mean_absolute_error(y_test[i], k[i])>1):
        print(X_test[i],y_test[i],k[i])
                                 
filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
features = []
i=0
features.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
'''

#realtime analysis
while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(0.1)
        file.seek(where)
    else:
        if (":" not in line):
            features[0][i]=float(line.split(" ")[1].strip('\n'))
            i+=1
        else: print(line,end="")
        if (i==19):
            #Test the system
            emotion=k.predict(features)
            for u in emotion:
                print(max(0,int(u[0])),"% neutral")
                print(max(0,int(u[1])),"% happy")
                print(max(0,int(u[2])),"% sad")
                print(max(0,int(u[3])),"% pride")
                print(max(0,int(u[4])),"% guilt")
            print()
            i=0
        
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
'''


'''for i in range (0,50):
    print(mean_absolute_error(y_test[i], k[i]))'''
