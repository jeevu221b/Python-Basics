arr = [1,2,3,4,2,3,1,4,5]
new_arr = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            # print("Duplicate", arr[j])
            new_arr.append(arr[j])
print(new_arr)
            
        

