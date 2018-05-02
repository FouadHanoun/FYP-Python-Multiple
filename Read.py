import time

filename = 'C:\\Users\\fouad.hannoun\\AppData\\Local\\Packages\\a4548d07-af25-4b98-b7b4-ad4c4798fc82_q8p7fyft9r39a\\LocalState\\Test Folder\\sample.txt'
file = open(filename,'r')
while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(0.1)
        file.seek(where)
    else:
        if ":" not in line:
            print (line) # already has newline
