def spaceRemover(name):
    new = ""
    final = ""
    for x in range(len(name)):
        if name[x] != " ":
            tracker = x
            break
    for y in range(tracker, len(name)):
        new = new + name[y]
    for z in range(len(new) - 1, -1, -1):
        if new[z] != " ":
            track = z
            break
    for l in range(track + 1):
        final = final + new[l]
    return final


output = spaceRemover("    h e e e e e l     ")
