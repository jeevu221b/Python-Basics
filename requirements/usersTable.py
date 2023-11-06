import sqlite3

# Building the connection with the database, creating the database if not
# already in the existence
conn = sqlite3.connect("app.db")
cursor = conn.cursor()


def getUser(email, password):
    # Creating the users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users
        (
            user_id INTEGER PRIMARY KEY,
            user_email TEXT UNIQUE,
            user_password TEXT
        )
        """
    )
    cursor.execute(
        "INSERT INTO users(user_email, user_password) VALUES (?,?)",
        (email, password),
    )
    fKey = cursor.lastrowid
    conn.commit()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    conn.close()
    return fKey
