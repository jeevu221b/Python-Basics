import sqlite3
import sys
from requirements.usersTable import getUser
from requirements.mac import get_mac_address
from datetime import datetime
from requirements.notificationSender import notifier
import requirements.loginTable as loginTable
import requirements.help as help
from requirements.loggedUser import getCurrentUser
from requirements.writeLogs import errorsLogs
from requirements.tasksTable import getTasks

# Building the connection with the database
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
mac_address = get_mac_address()
cmd = sys.argv


try:
    if cmd[1] != "login" and cmd[1] != "signup" and cmd[1] != "help":
            loggedUser = getCurrentUser()

    if cmd[1] == "help":
        help.prompt()

    if cmd[1] == "signup":
        user_email = cmd[2]
        user_password = cmd[3]
        try:
            user_id = getUser(user_email, user_password)
        except Exception as error:
            print("Email already in the existence, try again :)")
            errorsLogs(error)
            
            
    if cmd[1] == "login":
        try:
            user_email = cmd[2]
            user_password = cmd[3]
            loginTable.logged(user_email, user_password, mac_address)
        except Exception as error:
            print("No such user in the DB :(")
            errorsLogs(str(error))
            

    if cmd[1] == "create":
        try:
            taskname = cmd[2]
            try:
                duedate = cmd[3]
                duedate = datetime.strptime(duedate, "%H:%M:%S")
                duedate = duedate.strftime("%H:%M:%S")
                print(loggedUser)
                getTasks(loggedUser, taskname, duedate)
            except ValueError as e:
                print("Invalid time format. Please enter time in hh:mm:ss format.")
                errorsLogs(e)
        except NameError as e:
            print("You're not logged in, log in first :)")
            errorsLogs(e)
            
    if cmd[1] == "list":
        try:
            print(str(loggedUser))
            cursor.execute("SELECT * FROM tasks where user_id = ?", (str(loggedUser)))
            print("task_id, user_id, task, duedate")
            print(cursor.fetchall())
        except sqlite3.OperationalError as e:
            print("No such table in existence, Please create table first :)")
            errorsLogs(e)
        except NameError as e:
            print("You're not logged in, log in first :)")
            errorsLogs(e)
            

    if cmd[1] == "users":
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())

    if cmd[1] == "logout":
        user_id = cmd[2]
        print(user_id)
        cursor.execute("DELETE FROM logged WHERE user_id = ?", (user_id))
        if conn.total_changes == 0:
            print("User id didn't match :(")
        else:
            conn.commit()
            cursor.execute("SELECT * FROM logged")
            print(cursor.fetchall())


except IndexError as e:
    print("Invalid input type :(")
    errorsLogs(e)
    
    
except sqlite3.OperationalError as e:
    print("Something went wrong :(")
    errorsLogs(e)
except Exception as e:
    print("Something went wrong :(")
    errorsLogs(f"{str(error)}\n    type = {str(type(error))}")   
    




