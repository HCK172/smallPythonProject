import FreeSimpleGUI as sg


feetLabel = sg.Text("Enter feet")
inchesLabel = sg.Text("Enter inches")
inputFeet = sg.Input(key="feet")
inputInch = sg.Input(key="inch")
convert = sg.Button("Convert")
output_label = sg.Text(key="output")

layout = [[feetLabel, inputFeet],
          [inchesLabel, inputInch],
          [convert, output_label]]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    totalInch = float(values["feet"])*12 + float(values["inch"])
    meter = totalInch*0.0254
    window["output"].update(value=f"{meter} m")

sg.WIN_CLOSE()

window.close()