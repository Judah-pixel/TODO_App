import json

class Task:
    def __init__(self, id, title, info):
        self.id = id
        self.title = title
        self.info = info
        self.status = False

class TaskManager:
    def __init__ (self):
        self.storage = []

    def addTask(self, title, info):
        id = len(self.storage) + 1       
        self.storage.append(Task(id, title, info))

    def viewTask(self):
        if self.storage == []:
            print("You haven't created a task")
        else:
            for x in self.storage:
                print(f"\n------------\n{x.id}. {x.title}\nDescription: {x.info}\nStatus: {x.status}")

    def delTask(self, id):
    
        found = False

        for x in self.storage:
            if x.id == id:
                self.storage.remove(x)
                print(f"Task {x.id} has been removed")
                found = True
                break

        if found == False:
            print("Id doesn't exist")
            return

        for number, x in enumerate(self.storage, start=1):
            x.id = number
    
    def completeTask(self,id):
        found = False
        for x in self.storage:
            if x.id == id:
                x.status = True
                found = True
                print("it is done")
                self.viewTask()
                break

        if found == False:
            print("There is no task like that")

    def saveTask(self):
        savedict = []
        for task in self.storage:
            task_data = {
                "id" : task.id,
                "Title" : task.title,
                "Info" : task.info,
                "Status" : task.status
            }
            savedict.append(task_data)
                    
        saves = open("task.json", "w")
        json.dump(savedict, saves)
        saves.close()

    def loadTask(self):
        load = open("task.json", "r")
        yam = json.load(load)
        
        
        for x in yam:
            id = x["id"]
            title = x["Title"]
            info = x["Info"]
            status = x["Status"]
            new_task = Task(id,title, info)
            
            new_task.status = status
            self.storage.append(new_task)
            load.close()
        
# class User:
#     def __init__(self, name):
#         self.name : name
#         self.tskman = TaskManager()


# john = User('john')
# john.tskman.addTask('jb0', 'jb')
# john.tskman.viewTask()

 
