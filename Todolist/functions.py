filepath = "Todolist/tasklist.txt"

def read_file(file=filepath):
    with open(filepath,'r') as file:
        tasks = file.readlines()
    return tasks

def write_file(tasks,file=filepath):
    with open(filepath, 'w') as file:
        file.writelines(tasks)
