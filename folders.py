import ast
from returnPoint import getPoint
from makeFolder import mFolder

# Open the file in read mode
file = open("ver1_users.json", "r")
content = file.read()
# print(content[0]["email"])
# Convert the content to a dictionary using ast.literal_eval
user_data = ast.literal_eval(content)
value = user_data[0]["version"]
print(value)
yo = getPoint(str(value))
mFolder(yo, user_data[0])
