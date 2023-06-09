arr = [1, 2, 4, 6, 8,9]
new_arr = []

for i in range(len(arr)):
    if i == 0 or (arr[i] - arr[i-1]) != 1:
        new_arr.append(arr[i])

print(new_arr)
