#TO DO LIST APP
#Adding task
#Viewing
#Removing
#External history(WIP)


tasks = []
tasks.clear()

#Saving files function
def Save(tasks : list):
    task_saving = open("Tasks.txt" , "w")
    for t in tasks:
        task_saving.write(t + "\n")
    task_saving.close()
    print("SAVED")

#Loading files function
def Read(tasks : list):
    try:
        task_reading = open("Tasks.txt" , "r")
        for line in task_reading:
            tasks.append(line.strip())
        task_reading.close()
        print("LOADED HISTORY")
    except FileNotFoundError:
        print("History not available")

#Defining Add task function
def AddTask(tasks : list):
    while True:
        task = input("\nPlease enter a task:   ")
        while True:
            priority = input("\n Please choose the priority(High/mid/low):   ")
            if priority.lower() not in ["high", "mid", "low"]:
                print("Unavailable priority")
                print("Please try again")
                continue
            break
        comptask = task + " : " + priority
        tasks.append(comptask)
        again = input("Another one?(yes/no):   ")
        if again.lower() != "yes":
            break

#defining view task functions
def ViewTask(tasks : list):
    if not tasks:
        print("No tasks found\n")
        return
    else:
        print("\nYour tasks are: \n")
        for n, tas in enumerate(tasks , start=1):
            print(f"{n}- {tas}")
    
#defining task remover
def RemoveTask(tasks : list):
    if not tasks:
        print("\nNo tasks to remove")
        return
    while True:
            ViewTask(tasks)
            try:
                remove = int(input("Choose what task to remove ")) -1 
                if remove < 0 or remove >= len(tasks):
                    print("Tasks inexistent")
                    continue

                removed = tasks.pop(remove)
                print(f"Removed : {removed}")

            except:
                print("Invalid input.")
                continue

            again = input("\nAnother ??(yes/no):   ")
            if again.lower() == "no":
                break    
            elif again.lower() == "yes":
                if not tasks:
                    print("\nNo tasks to remove")
                    break
print("LOADING HISTORY")
Read(tasks)

#Defining App menu
def TaskMenu():
    print("\n===========================")
    print("         TO DO APP          ")
    print("===========================\n")
    while True:
        try:
            menuchoice = int(input("""Select your next activity:
                                    [1]Add Tasks
                                    [2]View Tasks
                                    [3]Remove Tasks
                                    [4]Exit:   """))
            if menuchoice ==1:
                print("\n=== ADD TASKS ===\n")
                AddTask(tasks)
                Save(tasks)
            elif menuchoice == 2:
                print("\n=== VIEW TASKS ===\n")
                ViewTask(tasks)
            elif menuchoice == 3:
                print("\n=== REMOVE TASKS ===\n")
                RemoveTask(tasks)
                Save(tasks)
            elif menuchoice == 4:
                exitchoice = input("Are you sure??(yes or no):   ")
                if exitchoice.lower() == "yes":
                    print("\nGoodbye...")
                    Save(tasks)
                    break
        except:
            print("\nINVALID ENTRY\n")
            print("Please try again")
            continue
