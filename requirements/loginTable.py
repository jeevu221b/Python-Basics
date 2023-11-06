import sqlite3
import time

# Building the connection with the database, creating the database if not
# already in existence
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

def is_user_logged_in(user_id):
    try:
        cursor.execute("SELECT * FROM logged WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None
    except sqlite3.OperationalError: 
        return None

def logged(user_email, user_password, mac_address):
    cursor.execute(
        "SELECT * FROM users WHERE user_email = ? AND user_password = ?",
        (user_email, user_password),
    )
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        if not is_user_logged_in(user_id):
            print(f"Login successful :)")
            current_time = int(time.time())

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
                "INSERT INTO logged(user_id, lastlogin, mac) VALUES (?,?,?)",
                (user_id, current_time, mac_address),
            )

            conn.commit()
            cursor.execute("SELECT * FROM logged")
            print(cursor.fetchall())
        else:
            print("User is already logged in.")
    else:
        print("Invalid credentials")

# Call the `logged` function with user email, password, and mac address
# to simulate a login.
