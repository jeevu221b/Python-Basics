def majorityElement(array, size):
    users = {}
    length = size / 2
    for x in range(size):
        if str(array[x]) in users:
            users[str(array[x])]["repetition"] += 1
            # print(x, "inside if")
        else:
            users[str(array[x])] = {"repetition": 1}
            # print(x, "inside else")
    # print(users)
    for x in users:
        if users[x]["repetition"] > length:
            return x
        else:
            return 0


output = majorityElement([1, 2, 3], 3)
print(output, "Is the Majority Element")
