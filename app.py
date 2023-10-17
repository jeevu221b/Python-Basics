import sqlite3
import sys
from db import userInfo

# Building the connection with the database
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# Getting the input from commandLine
cmd = sys.argv
try:
    if cmd[1] == "help":
        print("Options: \n")
        print("1. Input your info into the database")
        print("2. Login")
        print("3. Show database")

    if cmd[1] == "1":
        while True:
            info = userInfo()
            res = input("Are there more users to add?(or 'q' to quit): ")
            if res == "q":
                break

    if cmd[1] == "2":
        user_email = input("Enter your email address: ")
        user_password = input("Enter the password: ")
        # for users in info:
        #     if user_email == users[2] and user_password == users[3]:
        #         print("Login succesful :)")
        #         loggedUser = users[0]
        #         print(loggedUser)
        cursor.execute(
            "SELECT * FROM users WHERE user_email = ? AND user_password = ?",
            (user_email, user_password),
        )

        user = cursor.fetchall()
        if user:
            print(f"Login succesful :)")
            r = input("Press 'y' to view your tasks: ")
            if r == "y":
                print(user)
        else:
            print("Login failed :(")

    if cmd[1] == "3":
        k = input("Enter the secret key :) ")
        if k == "123":
            cursor.execute("SELECT * FROM users")
            print(cursor.fetchall())


except IndexError:
    print("Invalid input type :(")
