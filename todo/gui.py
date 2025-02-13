## pip install FreeSimpleGUI -- third-party modules
import functions 
import PySimpleGUI as sg
import time
import os

#sg.theme_previewer(); theme_name_list = sg.theme_list() print(theme_name_list)
## layout expect list of lists
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file: 
        pass

### create instance of the element
sg.theme("LightBlue3") #Sandy Peach


clock = sg.Text('',key="clock")
enter_label = sg.Text("Enter To Do Item")
input_box = sg.Input(key="todo")

add_button = sg.Button("Add")

listBox = sg.Listbox(values=functions.get_todos(), 
                     key="todos",
                     enable_events=True, 
                     size=[45,10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [enter_label],
          [input_box, add_button], 
          [listBox, edit_button, complete_button],
          [exit_button]]

### create a window instance
window = sg.Window('My To Do List',layout, font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Edit':

            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                # replace the exsisting to do with new_todo
                print(todos)
                index = todos.index(todo_to_edit)
                print(index)
                todos[index] = new_todo
                print(todos[index])
                print(todos)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except:
                sg.popup("Please select an item first", font=("Helvetica", 20))
                

        case 'todos':
             window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except:
                sg.popup("Please select an item first", font=("Helvetica", 20)) 
        case 'Exit':
           break
        case sg.WIN_CLOSED:
            break
window.close()

#close the program 

