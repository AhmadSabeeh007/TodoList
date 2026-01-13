def add_task():
    tasks = []
    num_task = int(input("Enter the number of tasks: "))
    for i in range(0, num_task):
        new_task = str(input("Enter the task: "))
        tasks.append(new_task)
    return tasks 

def delete_task(tasks):
    while True:
        print("Current Tasks: ",tasks)
        delete_item_name = str(input("Enter the Item to delete: "))
        if delete_item_name == 'exit' :
            break
        elif delete_item_name in tasks:
            tasks.remove(delete_item_name)
            print("Item removed")
        else:
            print("No item found")
def done_task(tasks,delete_item_name):
    #in this i will add all the recent task which are done 
    recent_task = []
    recent_task.append(delete_item_name)
    
def see_task(tasks):
    print("your tasks left: ",tasks)
    
    
    
tasks = add_task()
delete_task(tasks)
done_task(recent_task)
see_task(tasks)
