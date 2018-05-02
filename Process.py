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

#Train the system
k=MultiOutputRegressor(GradientBoostingRegressor(random_state=0)).fit(X, y)

                                 
filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
features = []
i=0
features.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


f2=open("plotting.txt","w+")
f2.write("")
f2.close()
#realtime analysis
while 1:
    f2=open("plotting.txt","a")
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(0.1)
        file.seek(where)
    else:
        if (":" not in line):
            features[0][i]=float(line.split(" ")[1].strip('\n'))
            i+=1
        else:
            f2.write(line)
        if (i==19):
            #Test the system
            emotion=k.predict(features)
            for u in emotion:
                f2.write(str(max(0,int(u[0])))+" ")
                f2.write(str(max(0,int(u[1])))+" ")
                f2.write(str(max(0,int(u[2])))+" ")
                f2.write(str(max(0,int(u[3])))+" ")
                f2.write(str(max(0,int(u[4])))+" ")
                f2.write(str(max(0,int(u[5])))+" ")
                f2.write(str(max(0,int(u[6])))+" ")
                f2.write(str(max(0,int(u[7])))+" ")
                f2.write(str(max(0,int(u[8])))+" ")
                f2.write("\n")
            i=0
    f2.close()    

'''
for i in range (0,50):
    print(mean_absolute_error(y_test[i], k[i]))'''
