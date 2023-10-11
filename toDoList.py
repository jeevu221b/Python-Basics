import sys
import json
  
tasks = []
commandline = sys.argv

if commandline[1] == "help":
    print("\nOptions: ")
    print("1. Add task = add space 'task' space 'task's status'")
    print("2. Delete task = delete 'index'")
    print("3. List task = list")
    print("4. Task done = done 'index'")
    print("5. Task undone = undone 'index'")
    

if commandline[1] == "add":
    with open("todo.json") as todo:
        info = json.load(todo)
        dict = {}
        add = ""
        for x in range(2, len(commandline)):
            add += " " + commandline[x] 
        stat = input("Enter the status of task: ")
        dict.update({"title":add.strip(),"status": stat})
        info.append(dict)
        with open("todo.json", "w") as file:
            json.dump(info, file)

if commandline[1] == "list":
    with open("todo.json", "r") as file:
        info = json.load(file)
        for i in range(len(info)):
            print(f"{i+1}.{info[i]['title']} ---> {info[i]['status']}")
            
if commandline[1] == "delete":
    try:
        with open("todo.json", "r") as file:
            info = json.load(file)
            info.pop(int(commandline[2]) - 1)
            print(info)        
            
        with open("todo.json", "w") as file:
                json.dump(info, file)
    except IndexError:
        print("Either index missing or out of range, try again :(")


if commandline[1] == "done":
    with open("todo.json", "r") as file:
            info = json.load(file)
            for i in range(len(info)):
                if info[i]['status'] == "done":
                    print(f"{i+1}.{info[i]['title']} ---> {info[i]['status']}")
            index_string = input("Enter the index of the task to be undone :)?")
            index = int(index_string)
            try:
                info[index - 1]["status"] = "undone"
                with open("todo.json", "w") as file:
                    json.dump(info, file)   
                                 
            except ValueError:
                print("Invalid input type, please enter only valid index :(")
            
            
            
             
if commandline[1] == "undone":
    with open("todo.json", "r") as file:
            info = json.load(file)
            for i in range(len(info)):
                if info[i]['status'] == "undone":
                    print(f"{i+1}.{info[i]['title']} ---> {info[i]['status']}")
            index_string = input("Enter the index of the task to be done :)?")
            index = int(index_string)
            try:
                info[index - 1]["status"] = "done"
                with open("todo.json", "w") as file:
                    json.dump(info, file)   
                                 
            except ValueError:
                print("Invalid input type, please enter only valid index :(")
 

        
        
       
        