# import OS module
import os
from stringooo import stringo

# Get the list of all files and directories
path = "/Users/santo/Downloads/Python-Basics/users"
dir_list = os.listdir(path)
for x in range(len(dir_list)):
    paths = "/Users/santo/Downloads/Python-Basics/users" + "/" + str(dir_list[x])
    dList = os.listdir(paths)
    for y in range(len(dList)):
        v = stringo(dList[y])
        print(v)
        os.rename(paths + "/" + v + ".txt", paths + "/" + v + ".json")
