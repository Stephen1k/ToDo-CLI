import os
import json

class TodoList:
    def __init__(self,filepath):
        self.filepath = filepath
        self.tasks = self.load_tasks()
        
    def load_tasks(self):
        if not os.path.exists(self.filepath):
            self.save_tasks()
            return {}
        with open(self.filepath,'r') as f:
            return json.load(f)
    
    def save_tasks(self):
        with open(self.filepath,'w') as f:
            json.dump(self.tasks,f,indent=4)
    
    def add_task(self,task):
        new_task = {"task": task,"done":False}
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added: {task}")
    
    def list_all_tasks(self):
        if not self.tasks:
            return "Nothing in your To Do list!"
        for i,task in enumerate(self.tasks,1):
            print(f"{i}. {task['task']}")
    
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save_tasks()
            print(f"Task marked as done: {self.tasks[index]['task']}")
        else:
            print("Invalid task number.")   