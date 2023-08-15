def findPair(arr, l, n):
    isPair = False
    for x in range(l):
        for y in range(x + 1, l):
            if arr[x] - arr[y] == n or arr[x] - arr[y] == -n:
                isPair = True
                break
    return isPair


output = findPair([90, 70, 20, 80, 50], 5, 45)
print(output)
