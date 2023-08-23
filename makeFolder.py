import os
import ast
from pathlib import Path


def mFolder(point, user):
    print(point, "pint")
    # Directory
    directory = point
    # Parent Directory path
    parent_dir = "/Users/santo/Downloads/Python-Basics/users"
    # Path

    # check if the directory exists
    # create the directory if it does not exist
    path = os.path.join(parent_dir, str(directory))
    isExist = os.path.exists(path)
    if not isExist:
        os.mkdir(path)

    # now we have to create a file in the directory
    file_name = str(user["version"]) + ".txt"

    # Creating a file at specified folder
    # join directory and file path
    with open(os.path.join(path, file_name), "w") as fp:
        # uncomment below line if you want to create an empty file
        fp.write("This is a new line")
