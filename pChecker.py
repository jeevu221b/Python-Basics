from datetime import datetime
from getPassword import getPassword

# message = "Time-out!"
# message1 = "Attendance updated!"
message = []


def passwordChecker(users):
    message = []
    x = 0
    for i in range(len(users)):
        if users[i].get("lastattempt") != None:
            curr_dt = datetime.now()
            difference = curr_dt - users[i]["lastattempt"]
            diff = difference.seconds
            print("Return after ", diff, "Seconds")
            if diff < 300:
                # attempts = True
                message.append("Time-Out!")
                return message
        else:
            while x < 3:
                password = getPassword()
                if users[i]["password"] == password:
                    users[i]["attendance"] += 1
                    email_exists = True
                    message.append("Attendance updated!")
                    return message

                x = x + 1
                print(x, "Value of x")
                if x == 3:
                    # attempts = True
                    users[i]["lastattempt"] = datetime.now()
                    print("All three attempts used!")
                    message.append("Time-Out!")
                    return message
