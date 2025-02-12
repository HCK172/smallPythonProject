import FreeSimpleGUI as sg
from zipcreator import make_archive

# element 
input1_label = sg.Input()
input2_label = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
choose_button2 = sg.FolderBrowse("Choose", key= "folder")
compress_button =sg.Button('Compress')
output_label= sg.Text(key="output", text_color="red")
# layout of the window
layout  = [
    [sg.Text('Select files to compress:'), input1_label, choose_button1],
    [sg.Text('Select destination folder: '), input2_label, choose_button2],
    [compress_button, output_label] 
]

window = sg.Window ('File Compressor',layout)

while True:

    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression complete!")

window.close()