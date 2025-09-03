# Regular.ly

# Objective: 
# Add tasks and set a frequency to get tasks done

# Example: Haircut, every 14 days.

# - send a notification to reminder after a task is completed.
# - if task not completed within timeframe, add task for the next day as a reminder
# - when task completed, record date and days since last completed and store frequency.

# UI
# Method
# 1. Add a task
#  - name
#  - frequency(# of days, day of the week/month/year)
#  - category 

# 2. Edit a task
#  - pick task and change it's details 
#  - change task category 
#  - update competition date
#  - update frequency 

# 3. Share statistics
#  - based on task.
#  - most consistent task
#  - most productive day of the week

##### IMPORT MODULES
from datetime import datetime,timedelta
import json
import requests

##### DEFINITIONS

### ADD TASK- adds a new task, checks if name/task is in the tasklist, if not, 
###           date added, frequency(d,w,bw,m,y,c), group
###           frequency will assign values to timedelta in days required.

def add_task(taskList):
    def frequency(list):
        str=list[name]['Frequency']
        if str == "D":
            value=1
        elif str == "W":
            value=7
        elif str == "BW":
            value=14
        elif str == "M":
            value=30
        elif str == "A":
            value=365
        elif str == "C":
            count=int(input("Enter custom duration: "))
            value=count
        elif str == "I":
            value=0        
        list[name]['interval']=value

        return list
    
    name= input("Enter a task name:")

    if name not in taskList:
        taskList[name]={}
        taskList[name]['Frequency']= input("Frequency- (Choose from Daily, Weekly, BiWeekly, Monthly, Annual, Custom): ").upper()     
        taskList=frequency(taskList)
        taskList[name]['Group']="Personal" #input("Which group: ")
        taskList[name]['Added On']=datetime.strftime(datetime.now(), '%d.%m.%Y')
        taskList[name]['completions']=[]
        # taskList['Next Date']=
        print(f"{name} added on {taskList[name]['Added On']}, frequency: {taskList[name]['Frequency']}")
    else:
        print("Task Exists")

    return taskList
### WRITE TO JSON- on exit, write the dictonary to "todo.json" file.

def write_file(taskList,fileName):
    with open(fileName, "w") as doc:
        json.dump(taskList, doc)


### LOAD JSON- on launch, write the "todo.json" file to dictonary data struct.

def load_file():
    entry=""
    entry=input("Loading...Main or Testing?:").upper()
    if entry == "M":
        fileName="main_todo.json"
    else:
        fileName="todo.json"
    try:
        with open(fileName, "r") as doc:
            jsonfile=json.load(doc)
            print("Loaded JSON file")        

    except FileNotFoundError:
            print(f"No file named '{fileName} exists.")    
    return jsonfile,fileName

def edit_task(list):
    count=0
    print("Edit List\n")
    items={}

    for item in list:
        count+=1
        print(f"[{count}] {item}")
        items[count]=item

    entry= int(input(f"Which task would you like to edit? (less than {len(list)}): "))
    print(f"You have entered {entry} which is {items[entry]}")
    newName=input("Name the task selected: ")

    confirm=input(f"Old Item Name:{items[entry]} | New Entry:{newName}  Correct? Y/N").upper()

    if confirm == "Y":
        list[newName]=list.pop(items[entry])
        list[newName]['name']=newName
        print(f"\n Done! \n")

def task_stats():
    pass

def remove_task(list):
    count=0
    remove=[]
    for item in list:
        count+=1
        try:
            completions=len(list[item]['completions'])
        except KeyError:
            completions=0
        remove.append(item)
        print(f"[{count}] {item}, {completions} entries")

    
    entry=input(f"Enter choice (less than {len(list)}, or E to skip): ").upper()
    if entry == "E":
        return list
    else:
        entry=int(entry)-1
        print(f"Your choice is {remove[entry]}")

# add a confirmation line here.
        print("Removing..")
        del list[remove[entry]]

        print("Done!")

        return list

def add_entry(list):
    count=1
    tasks={}
    print("\n ****Edit Menu**** \n")

    for task in list:
        print(f"[{count}] for '{task}'")
        tasks[count]=list[task]
        tasks[count]['name']=task
        count+=1

    task_entry= int(input("Pick a number: "))
    if task_entry in tasks:
        print(f"Found '{tasks[task_entry]['name']}'")
        for item in tasks[task_entry]:
            if item == "completions":
                print("Completions Verification: Passed")
                break
        else:
            print("Verification failed: Added Completions")
            tasks[task_entry]['completions']=[]

    compDate=input("Enter date of completion, DD.MM.YY: \n (T) for Today \n (C) for Other Date\nEntry:").upper()

    if compDate == "T":
        value=datetime.now()
        tasks[task_entry]['completions'].append(datetime.strftime(value, '%d.%m.%Y'))
        print(f"Added entry for {datetime.strftime(value,'%d.%m.%Y')}")
    elif compDate == "C":
        custom=input("Enter Date:")
        value=datetime.strptime(custom, '%d.%m.%Y')
        tasks[task_entry]['completions'].append(datetime.strftime(value, '%d.%m.%Y'))
        print(f"Added entry for {datetime.strftime(value,'%d.%m.%Y')}")

### RUN FUNCTION- runs each item in taskList recursively, checks [interval] and today's date, 
###               boolean returns if duration is <=> duration.

def run_function(list):
    if len(list)==0:
        print("No Tasks loaded")
    for name in list:
        if len(list[name]['completions']) == 0:
            print("No entries in completions")
        else:
            compDates=sorted([datetime.strptime(date, '%d.%m.%Y') for date in list[name]['completions']])
            duration=timedelta(days=list[name]['interval'])
            nextDate=compDates[-1]+duration
            list[name]['next reminder']=datetime.strftime(nextDate,'%a %d.%m.%Y')

            lastDate=datetime.strftime(compDates[-1],'%d.%m.%Y')
            print(f"\nTask: {name:}\nNext Scheduled Task: {list[name]['next reminder']}")            
            output=datetime.strptime(lastDate, '%d.%m.%Y')+duration > datetime.today()
            print(f"Last Completed Date: {lastDate}")
            if output == False:
                timeSince=datetime.today()-datetime.strptime(lastDate,'%d.%m.%Y')
                print("Task Due!")
                print(f"{list[name]['name']}:\nLast Completed On: {lastDate}, {timeSince.days} days ago")

                # requests.post("https://ntfy.olav.pw/todos",
                # data=f"{list[name]['name']}:\nLast Completed On: {lastDate}, {timeSince.days} ago",
                # headers={
                #     "Title": "To-Dos Update",
                #     "Priority": "low",
                #     })

### Start Menu- Navigation.

def start(taskList,fileName):
    entry=""
    while entry != 0:
        print("\nRegularly MENU\n")
        print("Choose Option from Below:")
        print("1. Add a Task:")
        print("2. Edit a Task:")
        print("3. Remove Task")
        print("4. Task Stats:")
        print("5. Add Entry:")
        print("6. Edit Entry:")
        print("7. Run Function")
        print("8. Load New File")

        print("0 to EXIT\n")
    
        entry=input("Entry:")
        print()

        if entry == "0":
            write_file(taskList,fileName)
            break
        elif entry == "1":
            taskList=add_task(taskList)
        elif entry == "2":
            edit_task(taskList)
        elif entry == "3":
            remove_task(taskList)
        elif entry == "4":
            task_stats()
        elif entry == "5":
            add_entry(taskList)
        elif entry == "6":
            edit_task(taskList)
        elif entry == "7":
            run_function(taskList)
        elif entry == "8":
            taskList,fileName=load_file()
##### PROGRAM EXECUTION

taskList,fileName=load_file()   
start(taskList,fileName)

    
