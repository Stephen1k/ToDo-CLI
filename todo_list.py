import os
import json

class TodoList:
    def __init__(self,filepath):
        self.filepath = filepath
        self.todo = self.load_todo()
        
    def load_todo(self):
        if not os.path.exists(self.filepath):
            self.save_todo()
            return {}
        with open(self.filepath,'r') as f:
            return json.load(f)
    
    def save_todo(self):
        with open(self.filepath,'w') as f:
            json.dump(self.todo,f,indent=4)
    
    def add_todo(self,task):
        new_task = {"task": task,"done":False}
        self.todo.append(new_task)
        self.save_todo()
        print(f"Task added: {task}")
    
    def list_all_todo(self):
        if not self.todo:
            return "Nothing in your To Do list!"
        for i,task in enumerate(self.todo,1):
            print(f"{i}. {task['task']}")
       