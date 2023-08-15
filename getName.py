from spaceRemove import spaceRemover


def getName(prompt):
    name = input(prompt)
    output = spaceRemover(name)
    while " " in output:
        print("Invalid name, Please Enter Again")
        name = input(prompt)
        output = spaceRemover(name)
        if " " not in name:
            return name
    return name
