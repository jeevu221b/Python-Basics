import time
arr = []
arr1 = []
for x in range(10000, 0, -1):
    arr.append(x)
for y in range(1, 10001):
    arr1.append(y)

length = len(arr)
count = 0
doesExist = False
start = time.time()
for i in range(length):
    count = 0
    for j in range(length):
        if arr[i] != arr1[j]:
            doesExist = False
        else:
            doesExist = True
            count = count + 1
            break
        # print(doesExist)
        # print("Count", count)
    if count < 1:
        doesExist = False
        break
    else:
        doesExist = True

if doesExist:
    print("Equal")
else:
    print("Unequal")
end = time.time()
print("Execution time is: ", (end-start)*10*3, "ms")
# if count == length:
#     print("Equal")
# else:
#     print("Unequal")
