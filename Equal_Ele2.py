def areEqualArrays(arr, arr1):
    length = len(arr)
    doesExist = False
    for i in range(length):
        doesExist = False
        for j in range(length):
            if arr[i] == arr1[j]:
                doesExist = True
                break
        if doesExist == False:
            doesExist = False
            break
    if doesExist:
        return True
    else:
        return False


arr = [1, 0, 2]
arr1 = [2, 0, 1]
arr2 = [9, 4, "a"]
arr3 = [9, 4, "a"]
length = len(arr)
Equal = areEqualArrays(arr, arr1)
Equal1 = areEqualArrays(arr2, arr3)

if Equal:
    print("Arrays 1 and 2 are equal")
else:
    print("Arrays  1 and 2 are not equal")
if Equal1:
    print("Arrays 2 and 3 equal")
else:
    print("Arrays 2 and 3 are not equal")
