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
y=fill(8,"Y.txt")

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



filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\emotions.txt'

emotions_list=["happiness","sadness","pride","guilt","defensive","interest","bored","impatience"]


#realtime analysis
while 1:
    f2=open("plotting.txt","a")
    f3 = open(filename,'w+')
    #f3.close()
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
            body=line.split("-")[0]
        if (i==19):
            #Test the system
            emotion=k.predict(features)
            for u in emotion:
                if((u[0]<30) and (u[1]<30) and (u[2]<30) and (u[3]<30) and (u[4]<30) and (u[5]<30) and (u[6]<30) and (u[7]<30)):
                        f3=open(filename,'a')
                        f3.write(body+" "+"neutral ")
                else:
                    for z in range(0,8):
                        if(max(0,int(u[z]))>70):
                            f3=open(filename,'a')
                            f3.write(body+" "+emotions_list[z]+" ")
                    f3.close()
                    time.sleep(0.02)
                    
                for z in range(0,8):
                        f2.write(str(max(0,int(u[z])))+" ")
                f2.write("\n")
                
                
            i=0
    f2.close()
    
