x = "[()]{}{[()()]()}"
lastIndex = len(x) - 1
balance = True
length = len(x)
match = False

print(length)
if length % 2 != 0:
    print("False h")
else:
    for i in range(len(x)):
        match = False

        if x[i] == "{":
            if x[i + 1] != "}":
                for i in range(i + 1, len(x), 2):
                    if x[i] == "}":
                        match = True
                        break
                if match != True:
                    balance = False
                    break
        if x[i] == "[":
            if x[i + 1] != "]":
                for i in range(i + 1, len(x), 2):
                    if x[i] == "]":
                        match = True
                        break
                if match != True:
                    balance = False
                    break
        if x[i] == "(":
            if x[i + 1] != ")":
                for i in range(i + 1, len(x), 2):
                    if x[i] == ")":
                        match = True
                        break
                if match != True:
                    balance = False
                    break

            # check if } is in the string at index i+1 = false
            # check if } is present in odd indices  = false
            # if both are false, then balance = false

    #         if "}" not in x:
    #             balance = False
    #             break

    #     if x[i] == "(":
    #         if ")" not in x:
    #             balance = False
    #             break
    #     if x[i] == "[":
    #         if "]" not in x:
    #             balance = False
    #

    print(balance)
    # print(match)
