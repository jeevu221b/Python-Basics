  
import sys

tasks = []
commandline = sys.argv

if commandline[1] == "help":
    print("\nOptions: ")
    print("1. Add task = add 'task'")
    print("2. Delete task = delete 'index'")
    print("3. List task = list")
    print("4. Task done = done 'index'")
    print("4. Task undone = undone 'index'")
    

if commandline[1] == "add":
    add = ""
    for x in range(2, len(commandline)):
        add += " " + commandline[x]
    tasks.append(add.strip())
    with open("todo.txt", "a") as file:
        file.write(add.strip() + "\n")

if commandline[1] == "list":
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
        for index, task in enumerate(tasks):  # Use enumerate to get both index and task
            print(f"{index}. {task}")
            
if commandline[1] == "delete":
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
        tasks.pop(int(commandline[2]))
        print(tasks)
        
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

if commandline[1] == "done":
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
    with open("todo.txt", "w") as file:
         for index, task in enumerate(tasks):
            if str(index) == commandline[2]:
                file.write(f"{task} ✓ \n")
            else:
                file.write(task + "\n")

if commandline[1] == "undone":
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
    with open("todo.txt", "w") as file:
         for index, task in enumerate(tasks):
            print(f"index = {index}, task = {task}")
            if str(index) == commandline[2]:
                print("inside if of undone")
                file.write(task + "\n")
            else:
                file.write(task + "\n")

        
        
       
        
    
    
    
