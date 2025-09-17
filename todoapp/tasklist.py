##### THIS CLASS IS ONLY FOR APP LOGIC
##### class TaskList, will be taskList-specific activities, provide it with task attributes and methods of operation on a task from the tasklist dict.

##### add_task,remove task,run_function,load_file, close()

from fileloader import FileLoader
from task import Task
from datetime import datetime
import json

class TaskList:
    def __init__(self):
        self.tasklist={}

### ADD A TASK TO TASKLIST
    def add_task(self,dts):
        dts['interval']=9 
        dts['Added On']="20.10.2020"        
        if 'name' not in self.tasklist:
            self.tasklist[dts['name']]=Task(dts)

### REMOVE A TASK FROM TASKLIST
    def remove_task(self,input):
        count=0
        tasks={}
        for item in self.tasklist:
            tasks[count]=item
            count+=1

        del self.tasklist[tasks[input-1]]
        
        


### RECURSIVELY RUN TASKLIST TO FIND ITEMS DUE:
    def run_function(self):
        filename="main_todo.json"

### LOAD A set of TASKs TO TASKLIST
    def load_file(self,input):
        self.filename="main_todo.json"
        if input != "M":
            self.filename="todo.json"
        self.fileloader=FileLoader()
    
        tasklist_temp=self.fileloader.load_file(self.filename)
        for item,details in tasklist_temp.items():
            self.tasklist[item]=Task(details)
        return self.tasklist
    
### LOAD A set of TASKs TO TASKLIST

    def close(self):
        ct={}
        for item,values in self.tasklist.items():
            info={}
            info['Name']=values.name
            info['Added On']=datetime.strftime(values.added,'%d.%m.%Y')
            info['Frequency']=values.freq
            info['interval']=values.interval.days
            info['Group']=values.group
            comps=[]
            for i in values.completions:
                comps.append(datetime.strftime(i,'%d.%m.%Y'))
            info['completions']=comps
            ct[item]=info
        print('Closed')
        self.fileloader.close(ct)
          

