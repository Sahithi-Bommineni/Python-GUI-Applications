import functions
import FreeSimpleGUI as sg


sg.theme("Brown Blue")

label = sg.Text("Enter task: ")
task_input = sg.InputText(tooltip="Enter Task", key = 'task')
add_button = sg.Button("Add")

window = sg.Window("My Todo List",layout=[[label],[task_input,add_button]])
while True:    
    event, values = window.read()
    match event:
        case 'Add':
            tasks = functions.read_file()
            task = values['task'] + '\n'
            tasks.append(task)
            functions.write_file(tasks)
        case sg.WIN_CLOSED:
            break

window.close()