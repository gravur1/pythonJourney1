import os
import json
import csv
#file = open("/home/kali/hash")
#print(file.read())
#printing the initial 5 bytes of the file
#print(file.read(5))

#file.seek(3) #resetting the cursor
#print(file.read(5)) #read first 5 bytes

#print(file.readline()) #start reading the file from the beggining of the cursor until the end of the line
#file.close() #closing the file once finished

#reading the file and avoid worrying about closing it using the function with

with open("/home/kali/newFile") as f:
    line = f.readline()
    while line:
        #print(line)
        line = f.readline()

#print(data)


###########
# ######
# ###writing to files
#file = open("/home/kali/newFile", 'w')
#file = open("/home/kali/newFile", 'r+') opening the file as read/write. The cursor also starts at the beggining of the file
#file = open("/home/kali/newFile", 'r+') opening the file as read/write. The cursor appends data, starts at the end
#file.write("Test writing to this file")
#file.seek(6)
#file.write(" new string")
#print(file.tell()) #tell how many bytes the file has
#file.truncate(37) #limiting the size of the file to 37 kb
#file.close()


###########
# ######
# ###File OS properties
#import os
#print(os.stat("/home/kali/hash").st_size)


###########
########
##### Working with json files
#import json
#file = open("/home/kali/myJson")
#json_file = json.load(file)
#str = json.dumps(json_file)
#print(json.dumps(str, sort_keys=True))


########
##### Working with csv files
#import csv
csv.register_dialect('tab', delimiter= '\t') #setting delimiters
#csv.reader(file, dialect = 'tab')

file = open('/home/kali/csv.csv', 'r')
with file:
    read = csv.reader(file)

    for row in read:
        print(row)

    