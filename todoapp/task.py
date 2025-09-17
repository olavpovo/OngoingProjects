##### THIS CLASS IS ONLY FOR APP LOGIC
##### class Task, will be task-specific activities, provide it with task attributes and methods of operation on a task from the tasklist dict.

##### edit_task,add_entry,task_stats
from datetime import timedelta,datetime

class Task():

    def __init__(self,deets):
        if 'Name' in deets:
            self.name=deets['Name']
        else:
            self.name="No Name"

        if 'completions' in deets:
            date_list=[]
            if len(deets['completions'])==0:
                self.completions=date_list
            else:
                for item in deets['completions']:
                    item=datetime.strptime(item,'%d.%m.%Y')
                    date_list.append(item)
                    self.completions=date_list
        else:
            self.completions=[]

        self.group=deets['Group']
        self.interval=timedelta(days=deets['interval'])
        self.freq=deets['Frequency']
        self.added=datetime.strptime(deets['Added On'],'%d.%m.%Y')


    def add_entry(self):
        self.group=deets['Group']
        self.interval=timedelta(days=deets['interval'])
        self.freq=deets['Frequency']
        self.added=datetime.strptime(deets['Added On'],'%d.%m.%Y')
        if 'name' in deets:
            self.name=deets['name']
        else:
            print('No Name')
    
    def edit_entry():
        pass


    def task_stats():
        pass


        
        
        