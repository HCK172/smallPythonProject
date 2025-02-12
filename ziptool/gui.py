import FreeSimpleGUI as sg

# element 
input1 = sg.Input()
input2 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")
choose_button2 = sg.FolderBrowse("Choose")
compress_button =sg.Button('Compress')

# layout of the window
layout  = [
    [sg.Text('Select files to compress:'), input1, choose_button1],
    [sg.Text('Select destination folder: '), input2, choose_button2],
    [compress_button] 
]

window = sg.Window ('File Compressor',layout)
window.read()
window.close()