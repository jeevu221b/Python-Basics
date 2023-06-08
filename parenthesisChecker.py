x = "()()([])"
lastIndex  = len(x)-1
balance = True    
length = len(x)
print(length)

for i in range(len(x)):
    if x[i] == "{":
        # check if } is in the string at index i+1 = false
        # check if } is present in odd indices  = false
        # if both are false, then balance = false

        if "}" not in x:
            balance = False
            break

    if x[i] == "(":
        if ")" not in x:
            balance = False
            break
    if x[i] == "[":
        if "]" not in x:
            balance = False
            break
print(balance)
    

    

    
