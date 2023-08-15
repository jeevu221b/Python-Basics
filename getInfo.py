from getName import getName
from getAge import getAge
from emailCheck import emailChecker
from getPassword import getPassword
from datetime import datetime
from pChecker import passwordChecker
import ast
import json


y = 0
file = open("users.txt", "r")
content = file.read()
data = []
if content:
    data = ast.literal_eval(content)
users = data
while True:
    attempts = False
    email = emailChecker()
    email_exists = False

    for i in range(len(users)):
        if users[i]["email"] == email:
            email_exists = True
            result = passwordChecker(users)

    if email_exists:
        if result[0] == "Time-Out!":
            continue
    if attempts:
        continue

    # If the email doesn't exist, add a new user
    if not email_exists:
        password = getPassword()
        firstName = getName("Enter your first name : ")
        lastName = getName("Enter your last name : ")
        age = getAge()

        users.append(
            {
                "email": email,
                "password": password,
                "firstname": firstName,
                "lastname": lastName,
                "age": age,
                "attendance": 1,
            }
        )

    y = y + 1
    response = input("Are there more users to add ? :")
    if response == "NO" or response == "no":
        break

    else:
        continue
print(users)
print(len(users))
# file = open()
file = open("users.txt", "w")
file.write(str(users) + "\n")
# with open("users.txt", "a") as file:
#     # Write the list of dictionaries as a JSON string followed by a newline
#     json.dump(users, file)
#     file.write("\n")

# print("Data appended to users.txt")
