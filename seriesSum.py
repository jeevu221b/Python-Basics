def seriesSum(n):
    sum = 0
    for x in range(1, n + 1):
        sum = sum + x
    return sum


output = seriesSum(5)
print(output)
