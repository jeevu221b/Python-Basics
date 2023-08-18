import ast
import json

obj = {}
file = open("64KB.json", "r")
content = file.read()
user_data = ast.literal_eval(content)
for x in range(len(user_data)):
    obj[user_data[x]["id"]] = user_data[x]
# print(obj)

for users in obj:
    print(obj[users])

# def write(file_name, data):
#     with open(file_name, "w") as output:
#         json.dump(data, output)


# write("users.json", obj)
