from TODO import *
import sys

user = TaskManager()

user.loadTask()
app = True
while app:

    welcome = int(input("\nWelcome to your ToDo app.\nWhat do you wish to do\n1. view tasks\n2. Add task \n3. Delete task \n4. Change status \n5. Exit \nWhich one: "))
    if welcome == 1:
        user.viewTask()
        continue

    elif welcome == 2:
        title = input("What is the name of the task: ")
        info = input("Enter the task description: ")
        user.addTask(title, info)
        user.saveTask()
        continue
        
    elif welcome == 3:
        id = int(input("Enter task id: "))
        user.delTask(id)
        user.saveTask()
        continue
        
    elif welcome == 4:
        id = int(input("Enter task id: "))
        user.completeTask(id)
        user.saveTask()
        continue
        
    elif welcome == 5:
        
        sys.exit("Thanks for turning in (●'◡'●)")

    else:
        continue


# jane.loadTask()
# jane.viewTask()
# jane.addTask("tam","iji")
# jane.addTask("tom","irei")
# jane.addTask("tyydyg","irebfgbi")
# jane.viewTask()
# jane.delTask(2)
# jane.viewTask()
# jane.completeTask(2)

# jane.saveTask()
