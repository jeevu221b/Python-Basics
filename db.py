def userInfo():
    import sqlite3

    # Building the connection with the database, creating the database if not
    # already in the existence
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # Creating the users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users
        (
            user_id INTEGER PRIMARY KEY,
            user_name TEXT,
            user_email TEXT,
            user_password TEXT
        )
        """
    )

    # # Asking for the user info
    user_name = input("Enter the name of the user : ")
    user_email = input("Enter the email of the user : ")
    user_password = input("Enter the password of the email : ")

    # Inserting the user info inside the users table
    cursor.execute(
        "INSERT INTO users(user_name, user_email, user_password) VALUES (?,?,?)",
        (user_name, user_email, user_password),
    )

    fKey = cursor.lastrowid

    # # Commiting all the changes
    conn.commit()

    # # Creating the tasks table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks
        (
            task_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            task TEXT,
            description TEXT,
            status TEXT
        )
        """
    )

    # # Asking the for task input from the user
    while True:
        task = input("Enter your task: ")
        description = input("Enter the description of the task: ")
        status = input("Enter the status of the task: ")

        # Inserting the values in the task table
        cursor.execute(
            "INSERT INTO tasks(user_id, task, description, status) VALUES (?,?,?,?)",
            (fKey, task, description, status),
        )

        response = input("Are there any more tasks to add? (or press 'no' to exit): ")
        if response.lower() == "no":
            break

    #     # Fetching the data from the table for the current user and printing
    #     cursor.execute("SELECT * FROM tasks WHERE user_id=?", (fKey,))
    #     tasks = cursor.fetchall()
    #     print("Tasks for User ID", fKey)
    #     for task in tasks:
    #         print(task)

    conn.commit()
    # cursor.execute("SELECT * FROM users")
    # print(cursor.fetchall())
    # print()
    # cursor.execute("SELECT * FROM tasks")
    # print(cursor.fetchall())
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

    # Close the database connection
    conn.close()
