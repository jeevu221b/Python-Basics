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
    # print(new)
    # print(arr)
    new = {}

print(arr[1])

# for a in range(len(arr)):
#     for b in range(a+1, len(arr)):
#         if arr
