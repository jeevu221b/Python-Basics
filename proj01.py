users = [{"name": "John", "age": 36, "country": "Norway", "phone": [1234567890, 9876543210, 33333333333]},
        {"name": "Logan", "age": 22, "country": "Germany", "phone": [1234567888, 00000000]},
        {"name": "Joe", "age": 20, "country": "USA", "phone": [1234567888, 000000000]},
        {"name": "Kurt", "age": 29, "country": "Greece", "phone": [1234567888, 000000000]}]
new_arr = []
for i in range(len(users)):
    for j in range(len(users[i]["phone"])):
        user = {"first_name":users[i]["name"], "year":users[i]["age"], "Number":users[i]["phone"][j]}
        new_arr.append(user)
    

print(new_arr)
       


   



