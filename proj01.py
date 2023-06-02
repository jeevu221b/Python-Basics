# arrr = [1,2,2,3,4,3,2]
#ind_of_duplicates = [2,5,6]
# unique_arr = [1,2,3,4]
index = []
arr = [1,2,2,2]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            index.append(j)
            
            
            
print(index)