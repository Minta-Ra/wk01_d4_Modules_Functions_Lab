
# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks=[]
    for item_in_list in list:
        if item_in_list["completed"] == False:
            uncompleted_tasks.append(item_in_list)
    return uncompleted_tasks


## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks=[]
    for item_in_list in list:
        if item_in_list["completed"] == True:
            completed_tasks.append(item_in_list)
    return completed_tasks


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    time_tasks = []
    for task in list:
        if time >= task["time_taken"]:
            time_tasks.append(task)
    return time_tasks
    

## Find a task with a given description
def get_task_with_description(list, description):
    for item_in_list in list:
        if item_in_list["description"]== description:
            return item_in_list
    return "No such task"





# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    pass

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)