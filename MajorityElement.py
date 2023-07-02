def majorityElement(array, size):
    new_arr = []
    length = size/2
    print(length, "length")
    duplicateCount = 0

    for x in range(size):
        for y in range(x+1, size):
            if array[x] == array[y]:
                new_arr.append(array[y])
    print(new_arr)
    # for z in range(len(new_arr)):


    # return (new_arr)


output = majorityElement([2, 3, 5, 2, 4, 3], 6)
# print(output)
