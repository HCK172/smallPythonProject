## pip install FreeSimpleGUI -- third-party modules
import functions 
import PySimpleGUI as sg

#sg.theme_previewer(); theme_name_list = sg.theme_list() print(theme_name_list)
## layout expect list of lists


### create instance of the element
sg.theme("LightBlue3") #Sandy Peach

enter_label = sg.Text("Enter To Do Item")
input_box = sg.InputText(key="todo")

add_button = sg.Button("Add")

listBox = sg.Listbox(values=functions.get_todos(), 
                     key="todos",
                     enable_events=True, 
                     size=[45,10])

edit_button = sg.Button("Edit")

layout = [[enter_label],[input_box, add_button], [listBox, edit_button]]

### create a window instance
window = sg.Window('My To Do List',layout, font=('Helvetica', 20))

while True:
    event, values= window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo'])
    print(4, values['todos'])

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
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
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()

#close the program 

