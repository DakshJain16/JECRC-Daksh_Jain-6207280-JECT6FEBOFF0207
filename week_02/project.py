import time

class TODO:
    todos = []
    
    def add_todo(self, desc):
        self.todos.append({'id' : int(time.time()),
                 'desc' : desc,
                 'is_completed' : False})
        
         
    def remove_todo(self, id):
        if len(self.todos) == 0: return

        for i in self.todos:
            if i['id'] == id:
                self.todos.remove(i)
    
    def display_todos(self):
        if len(self.todos) == 0: return

        for i in self.todos:
            if i['is_completed']:
                print(f'--> {i["desc"]}, {i["id"]}, (Completed)')
            else:
                print(f'--> {i["desc"]}, {i["id"]}, (incomplete)')
    
    def update_todo(self, id, new_desc):
        if len(self.todos) == 0: return

        for i in self.todos:
            if i['id'] == id:
                i['desc'] = new_desc
    
    def toggle_mark_as_completed(self, id):
        if len(self.todos) == 0: return

        for i in self.todos:
            if i['id'] == id:
                i['is_completed'] = True
    
    def completed_todos(self):
        if len(self.todos) == 0: return
        
        for i in self.todos:
            if i['is_completed']:
                print(f'---> {i["desc"]}')
    
    def incompleted_todos(self):
        if len(self.todos) == 0: return
        
        for i in self.todos:
            if i['is_completed'] == False:
                print(f'---> {i["desc"]}')
    
obj = TODO()
# obj.add_todo('Washing clothes')
# obj.add_todo('Homework')
# obj.add_todo('Cleaning')
# obj.add_todo('Dusting')
# print(obj.todos)

# obj.remove_todo(1772874308)