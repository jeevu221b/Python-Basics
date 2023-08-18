# array = [{"jeevu": 4}, {"punk": 3}, {"logan": 1}]

# for dictionary in array:
#     # Iterate through each dictionary in the list
#     for value in dictionary.values():
#         # Inside each dictionary, directly access the values
#         print(value)

# # length = len(array)
# for x in range(length):
#     for y in range(x+1, length):
#         if array[x] > array[y]:
#             temp = array[x]
#             print(temp, "-->", "temp")
#             array[x] = array[y]
#             print(array[x], "array[x]", "---->", x)
#             array[y] = temp
#             print(array[y], "array[y]", "---->", y)


# print(array)
# arr = []
# obj = {"name": "jeevu", "age": 19, "roll": 23}
# arr.append(obj)

# arr = []
# obj = {"name": "jeevu", "age": 19, "roll": 23}

# # Append specific keys to different indexes of the array
# arr.append(obj["name"])
# arr.append(obj["age"])
# arr.append(obj["roll"])


# arr = [{"jeevu": 2}, {"punk": 3}]
# print(arr[0])

arr = [{"jeevu": 3}, {"punk": 2}]

# Iterate over the list
for dictionary in arr:
    print(arr)
    # Iterate over the key-value pairs in each dictionary
    for key, value in dictionary.items():
        print(value, "sduhd")
