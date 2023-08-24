import ast
from returnPoint import getPoint
from makeFolder import mFolder

file = []
# Open the file in read mode
file1 = open("ver1_users.json", "r")
file2 = open("ver2_users.json", "r")
file3 = open("ver3_users.json", "r")
content1 = file1.read()
content2 = file2.read()
content3 = file3.read()
user_data1 = ast.literal_eval(content1)
user_data2 = ast.literal_eval(content2)
user_data3 = ast.literal_eval(content3)


def pushFile(original, destination):
    for x in range(len(original)):
        destination.append(original[x])


pushFile(user_data1, file)
pushFile(user_data2, file)
pushFile(user_data3, file)

for z in range(len(file)):
    value = file[z]["version"]
    yo = getPoint(str(value))
    mFolder(yo, file[z])
