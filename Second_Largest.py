def print2largest(arr, n):
    new_arr = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    for k in range(n):
        if arr[k] not in new_arr:
            new_arr.append(arr[k])
    if len(new_arr) < 2:
        return -1
    else:
        # print("Second largest element in the array is", new_arr[1])
        return (new_arr[1])


arr = [9, 2]
n = len(arr)

largest = print2largest(arr, n)
print("Second largest =", largest)
