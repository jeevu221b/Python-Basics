import sqlite3

# Building the connection with the database, creating the database if not
# already in the existence
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

def getTasks(loggedUser, taskname, duedate):
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