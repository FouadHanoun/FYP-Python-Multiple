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
y=fill(9,"Y.txt")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

#Train the system
k=MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X_train, y_train).predict(X_test)
for i in range (0,270):
    '''if(mean_absolute_error(y_test[i], k[i])>0.1):
        print(y_test[i])
        print(k[i])
    
    '''
    if(k[i][0]>50): print("happy")
    if(k[i][1]>50): print("sad")
    if(k[i][2]>50): print("neutral")
    if(k[i][3]>50): print("pride")
    if(k[i][4]>50): print("guilt")
    if(k[i][5]>50): print("defensive")
    if(k[i][6]>50): print("interest")
    if(k[i][7]>50): print("boredom")
    if(k[i][8]>50): print("impatience")
