from tasklist import TaskList


class UserInterface:
    def __init__(self):
        self.app=TaskList()

    def menu(self):
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
    
    def start(self):
        self.menu()
        print()
        while True:
            entry= input("Entry:")

            if entry == "0":
                self.app.close()
                break            
            elif entry == "1":
                details={}
                details['name']= input("Name of Task: ")
                details['Group']=input(f"Group for '{details['name']}'': ")
                details['Frequency']=input("Frequency: ") 
                details['interval']=9 
                details['Added On']="20.10.2020"
                self.app.add_task(details)
                
            elif entry == "2":
                self.edit_task()
            elif entry == "3":
                self.remove_task()

            elif entry == "4":
                pass
            elif entry == "5":
                self.add_entry()
            elif entry == "6":
                self.edit_entry()
            elif entry == "7":
                pass
            elif entry == "8":
                file_input=input("(M)ain or any for (T)esting file: ")
                self.app.load_file(file_input)

    def remove_task(self):
        print("\n-- Remove a task --\n")
        count=0
        for task in self.app.tasklist:
            count+=1
            print(f"{count}: {task}")
        choice=int((input("Pick a number: ")))
        if choice=="0":
            pass
        print()
        self.app.remove_task(choice)