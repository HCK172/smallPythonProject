## pip install FreeSimpleGUI -- third-party modules
import functions 
import FreeSimpleGUI as sg

#sg.theme_previewer(); theme_name_list = sg.theme_list() print(theme_name_list)
## layout expect list of lists


### create instance of the element
sg.theme("LightBlue3") #Sandy Peach
label = sg.Text("Enter in a To-Do Item")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
listBox = sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

layout = [[label],[input_box, add_button], [listBox,edit_button]]

### create a window instance
window = sg.Window('My To-Do App',layout, 
                   font =('Helvetica', 20))
while True:
    event, values= window.read()
    match event:

        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(value=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
window.close() #close the program 

