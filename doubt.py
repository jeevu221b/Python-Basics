obj = {"Name": [{"name": ["name1"]}, "YIe"], "Age": 19, "Gender": "MALE"}
names = obj["Name"]
n1 = names[0]
n2 = n1["name"]
# print(n2[0])
# print(obj["Name"][0]["name"][0])

testAery = [
    1,
    2,
    [1, 2, [2, {"name": "logan", "address": ["address1", {"zip": "address2"}]}, 3], 3],
    4,
    5,
]
print(testAery[2][2][1]["address"][1]["zip"])

# name = obj["Name"[0]["name"][0
