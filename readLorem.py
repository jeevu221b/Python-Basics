file = open("sample1.txt", "r")
content = file.read()
obj = {"343444": {"name": "dy"}, "3444": {"name": "f"}}
words = {}
str = ""
arr = []
new = {}
for x in range(len(content)):
    # print(content[x], ":letter")
    if content[x] != " " and content[x] != "\n":
        str = str + content[x]
    if content[x] == " ":
        if str in words:
            words[str] += 1
        else:
            words[str] = 1
        str = ""
# print(words)
for key in words:
    new[key] = words[key]
    arr.append(new)
    new = {}

key = []
for x in range(len(arr)):
    key = list(arr[x].keys())
    xkey = key[0]
    for y in range(len(arr)):
        key = list(arr[y].keys())
        ykey = key[0]

        if arr[x][xkey] < arr[y][ykey]:
            temp = arr[x][xkey]
            arr[x][xkey] = arr[y][ykey]
            arr[y][ykey] = temp

kesi = []
k = []
for z in range(len(arr)):
    kesi = list(arr[z].keys())
    x = kesi[0]
    k = list(arr[z].keys())
    print(k[0], "-->", arr[z][x])
