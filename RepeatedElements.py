users = {}

# users["john"] = {"age": 20}
# if users["john"]:
#     users["john"] = {"address": {"pincode": 0}}
# print(users)

while True:
    Name = input("Enter your name:")
    ask = input("Are there more users")
    if Name in users:
        users[Name]["attendance"] += 1
    else:
        users[Name] = {"attendance": 1}
    print(users)

    if ask != "yes":
        break
print(users)
