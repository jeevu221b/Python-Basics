def getAge():
    while True:
        age = input("Enter your age: ")
        if age.isnumeric():
            age = int(age)
            if age >= 1 and age <= 100:
                return age
