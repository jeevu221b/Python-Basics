# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "yolo"

# Parent Directory path
parent_dir = "/Users/santo/Downloads/Python-Basics/users"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)

# importing the os module
# import os

# # to get the current working directory
# directory = os.getcwd()

# print(directory)

# users (folder)
# 1 (folder)
# 1.0.txt
# 1.02.txt

# 1.1 (folder)
# 1.1.txt
# 1.2.txt
