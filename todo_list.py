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
        