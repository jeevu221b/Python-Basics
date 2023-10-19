import sqlite3
import sys
from users import getUser
from mac import get_mac_address
from datetime import datetime
from notifyy import notifier
import time

# Building the connection with the database
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
mac_address = get_mac_address()
cmd = sys.argv

try:
    userId = ""
    try:
        if cmd[1] != "login" and cmd[1] != "signup" and cmd[1] != "help":
            cursor.execute("SELECT * FROM logged WHERE mac = ?", (mac_address,))
            user = cursor.fetchall()
            if user:
                for info in user:
                    loggedUser = info[0]

    except:
        pass

    if cmd[1] == "help":
        help.prompt()

    if cmd[1] == "signup":
        user_email = cmd[2]
        user_password = cmd[3]
        try:
            user_id = getUser(user_email, user_password)
        except:
            print("Email already in the existence, try again :)")

    if cmd[1] == "login":
        try:
            user_email = cmd[2]
            user_password = cmd[3]
            cursor.execute(
                "SELECT * FROM users WHERE user_email = ? AND user_password = ?",
                (user_email, user_password),
            )
            user = cursor.fetchall()
            if user:
                print(f"Login succesful :)")
                current_time = int(time.time())
                for info in user:
                    user_id = info[0]
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS logged
                    (
                        
                        user_id INTEGER,
                        lastlogin INTEGER,
                        mac TEXT
                    )
                    """
                )

                cursor.execute(
                    "INSERT INTO logged(user_id,lastlogin, mac) VALUES (?,?,?)",
                    (user_id, current_time, mac_address),
                )

                conn.commit()
                cursor.execute("SELECT * FROM logged")
                print(cursor.fetchall(), "login")
        except:
            print("No such user in the DB :(")

    if cmd[1] == "create":
        try:
            taskname = cmd[2]
            try:
                duedate = cmd[3]
                duedate = datetime.strptime(duedate, "%H:%M:%S")
                duedate = duedate.strftime("%H:%M:%S")
                print(loggedUser)
                cursor.execute(
                    """
                        CREATE TABLE IF NOT EXISTS tasks
                        (
                             task_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            taskname TEXT,
                            duedate TEXT
                        )
                        """
                )
                cursor.execute(
                    "INSERT INTO tasks(user_id,taskname, duedate ) VALUES (?,?,?)",
                    (loggedUser, taskname, duedate),
                )
                conn.commit()
                cursor.execute("SELECT * FROM tasks")
                print(cursor.fetchall())
            except ValueError:
                print("Invalid time format. Please enter time in hh:mm:ss format.")
        except NameError:
            print("You're not logged in, log in first :)")

    if cmd[1] == "list":
        try:
            cursor.execute("SELECT * FROM tasks where user_id = ?", (str(loggedUser)))
            print("task_id, user_id, task, duedate")
            print(cursor.fetchall())
        except NameError:
            print("You're not logged in, log in first :)")

    if cmd[1] == "notify":
        task_id = cmd[2]
        cursor.execute("SELECT * FROM tasks where task_id = ?", (task_id))
        task = cursor.fetchall()
        for info in task:
            duedate = info[3]
            task = info[2]
        while True:
            current = datetime.now()
            current_time = current.strftime("%H:%M:%S")
            print(current_time)
            if str(duedate) < current_time:
                print("Task was in past :(")
                break
            elif str(duedate) == current_time:
                notifier(task)
                print("Inside notifier")
                break


except IndexError:
    print("Invalid input type :(")
