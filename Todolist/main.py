import functions
import FreeSimpleGUI as sg


sg.theme("Brown Blue")

label = sg.Text("Enter task: ")
task_input = sg.InputText(tooltip="Enter Task", key = 'task')
add_button = sg.Button("Add")
task_list = sg.Listbox(values=functions.read_file(),key='tasks',enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout=[[label],
        [task_input,add_button],
        [task_list,edit_button,complete_button,exit_button]]

window = sg.Window("My Todo List",layout)
while True:    
    event, values = window.read()
    match event:
        case 'Add':
            tasks = functions.read_file()
            task = values['task'] + '\n'
            tasks.append(task)
            functions.write_file(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")
        case 'Edit':
            task_to_edit=values['tasks'][0]
            new_task = values['task']
            tasks = functions.read_file()
            index = tasks.index(task_to_edit)
            tasks[index]=new_task
            functions.write_file(tasks)
            window['tasks'].update(values=tasks)
        case 'tasks':
            window['task'].update(value = values['tasks'][0])
        case 'Complete':
            task_complete = values['tasks'][0]
            tasks=functions.read_file()
            tasks.remove(task_complete)
            functions.write_file(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value='')
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()