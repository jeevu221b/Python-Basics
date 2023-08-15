def getPassword():
    # Get the password from the user
    while True:
        password = input("Enter the password: ")
        if len(password) > 4:
            return password
        else:
            continue
