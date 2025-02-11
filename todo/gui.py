## pip install FreeSimpleGUI -- third-party modules
import functions 
import FreeSimpleGUI as sg

### create instance of the element
sg.theme("LightBlue3") #Sandy Peach
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

### create a window instance
window = sg.Window('My To-Do App', layout=[[label],[input_box, add_button]])
window.read() #display window on the screen
window.close() #close the program 

#sg.theme_previewer(); theme_name_list = sg.theme_list() print(theme_name_list)
## layout expect list of lists