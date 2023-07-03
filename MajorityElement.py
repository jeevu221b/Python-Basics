def majorityElement(array, size):
    new_arr = []
    majorityElement = {"element": " ", "repetion":-1}
    length = size / 2
    print(length, "length")
    duplicateCount = 0

    for x in range(size):
        for y in range(x + 1, size):
            if array[x] == array[y]:
                new_arr.append(array[y])
    print(new_arr)
    # for z in range(len(new_arr)):

    # return (new_arr)


output = majorityElement([2, 3,2], 2)
# print(output)
