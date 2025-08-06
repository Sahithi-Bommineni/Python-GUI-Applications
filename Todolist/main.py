import functions
import FreeSimpleGUI as sg
from fpdf import FPDF

#sg.theme("Blue")

label = sg.Text("Enter task: ")
task_input = sg.InputText(tooltip="Enter Task", key = 'task')
add_button = sg.Button("Add")
task_list = sg.Listbox(values=functions.read_file(),key='tasks',enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
pdf_button = sg.Button("Generate PDF")

layout=[[label],
        [task_input,add_button],
        [task_list,edit_button,complete_button],
        [exit_button,pdf_button]]


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
            try:
                task_to_edit=values['tasks'][0]
                new_task = values['task']
                tasks = functions.read_file()
                index = tasks.index(task_to_edit)
                tasks[index]=new_task
                functions.write_file(tasks)
                window['tasks'].update(values=tasks)
            except IndexError:
                sg.popup("Please select a task to edit")
        case 'tasks':
            window['task'].update(value = values['tasks'][0])
        case 'Complete':
            try:
                task_complete = values['tasks'][0]
                tasks=functions.read_file()
                tasks.remove(task_complete)
                functions.write_file(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value='')
            except IndexError:
                sg.popup("Please select a task to mark complete")
        case 'Generate PDF':
            pdf = FPDF(orientation="P",format="A4")
            pdf.add_page()
            tasks = functions.read_file()
            for i in range(len(tasks)):
                pdf.set_font(family="Times",size=24)
                pdf.cell(w=0,h=12,txt=f"{i+1}.{tasks[i]}",ln=1)
            pdf.output("Todolist.pdf")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()