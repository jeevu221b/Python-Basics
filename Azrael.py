from getName import getName
from getAge import getAge
from emailCheck import emailChecker
from getPassword import getPassword
from datetime import datetime

# curr_dt = datetime.now()
# print(curr_dt)
# curr_dt2 = datetime.now()
# difference = curr_dt2 - curr_dt
# time = difference.seconds
# print(time)
users = []
email_attendance = {}
while True:
    x = 0
    attempts = False
    email = emailChecker()
    email_exists = False
    for i in range(len(users)):
        if users[i]["email"] == email:
            if users[i].get("lastattempt") != None:
                curr_dt = datetime.now()
                difference = curr_dt - users[i]["lastattempt"]
                diff = difference.seconds
                print(diff, "Seconds")
                if diff < 300:
                    attempts = True
                    break
            else:
                while x < 3:
                    password = getPassword()
                    if users[i]["password"] == password:
                        users[i]["attendance"] += 1
                        email_exists = True
                        break
                    x = x + 1
                    print(x, "Value of x")
                    if x == 3:
                        attempts = True
                        users[i]["lastattempt"] = datetime.now()
    if attempts:
        print("inside dum")
        continue

    # If the email doesn't exist, add a new user
    if not email_exists:
        print("Inside not")
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

    response = input("Are there more users to add ? :")
    if response == "NO" or response == "no":
        break

    else:
        continue
print(users)
