def leader(arr):
    for i in range(length):
        isLeader = True
        for j in range(i+1, length):
            if arr[i] < arr[j]:
                isLeader = False
        if isLeader:
            leaderr.append(arr[i])
    return (leaderr)


arr = [1, 3, 10, 11, 9, 8]
length = len(arr)
leaderr = []
leader(arr)
print(leaderr)


# print(leader)
