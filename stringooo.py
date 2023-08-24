def stringo(str):
    new = ""
    if len(str) == 7:
        for x in range(3):
            new = new + str[x]
        return new
    else:
        for x in range(4):
            new = new + str[x]
        return new
