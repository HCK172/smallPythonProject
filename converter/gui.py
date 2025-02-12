import FreeSimpleGUI as sg


feetLabel = sg.Text("Enter feet")
inchesLabel = sg.Text("Enter inches")
inputFeet = sg.Input()
inputInch = sg.Input()
convert = sg.Button("Convert")

layout = [[feetLabel, inputFeet],
          [inchesLabel, inputInch],
          [convert]]

window = sg.Window("Convertor", layout)
window.read()
window.close()