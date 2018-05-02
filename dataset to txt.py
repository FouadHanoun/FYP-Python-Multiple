import os
# Writing the dataset in text

filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
features = []
i=0
j=0
features.append([])
for line in file:
    if (":" not in line):
        features[j].append(float(line.split(" ")[1].strip('\n')))
    i+=1
    if (i==20):
        features.append([])
        i=0
        j+=1
del features[-1]


f= open("dataset.txt","w+")
f.write('[')
u=0
for z in features:
    a="["
    for y in z:
        a+=str(y).strip('\n')+','
    a=a.strip(',')+'],'
    f.write(a)
    f.write('\n')
    u+=1
    if(u==140):
        break
f.seek(0,2)          #go to the end
size=f.tell()        #get the size of the file in order to truncate
f.truncate(size-3)   #remove the last ','
f.seek(0,2)
f.write(']')
f.close()

