import ast
import json
ver1_user = []
ver2_user = []
ver3_user = []
file = open("64KB.json", "r")
content = file.read()
user_data = ast.literal_eval(content)
# print(user_data[0]["name"])
# print(len(user_da ta))
for x in range(len(user_data)):
    if user_data[x]["version"] < 2:
        # print("Inside if")
        ver1_user.append(user_data[x])
        # file = open("users.txt", "w")
        # file.write(str(users) + "\n")
    elif user_data[x]["version"] > 1 and user_data[x]["version"] < 3:
        ver2_user.append(user_data[x])
    elif user_data[x]["version"] > 2 and user_data[x]["version"] < 4:
        ver3_user.append(user_data[x])


def write(file_name, data):
    with open(file_name, "w") as output:
        json.dump(data, output)


write("ver1_users.json", ver1_user)
write("ver2_users.json", ver2_user)
write("ver3_users.json", ver3_user)


# print(ver2_user[0], "Version 2")
# print(ver3_user[0], "Version 3")
