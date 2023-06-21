arr = [9, 2]
length = len(arr)
new_arr = []
# print(length)
for i in range(length):
    for j in range(i+1, length):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for k in range(length):
    if arr[k] not in new_arr:
        new_arr.append(arr[k])
if len(new_arr) < 2:
    print("Second largest element doesn't exist")
else:
    print("Second largest element in the array is", new_arr[1])
