main = []


def read(filename):
    file = open(filename, "r")
    content = file.read()
    return content


file1 = read("ver1_users.json")
file2 = read("ver2_users.json")
file3 = read("ver3_users.json")


def append(file, data):
    file.append(data)


append(main, file1)
append(main, file2)
append(main, file3)
print(main, "INsie")
