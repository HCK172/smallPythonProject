import FreeSimpleGUI as sg


feetLabel = sg.Text("Enter feet")
inchesLabel = sg.Text("Enter inches")
inputFeet = sg.Input(key="feet")
inputInch = sg.Input(key="inch")
convert = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_label = sg.Button("Exit")

layout = [[feetLabel, inputFeet],
          [inchesLabel, inputInch],
          [convert, exit_label, output_label]]
          

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match 'event':
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
    try: 
        totalInch = float(values["feet"])*12 + float(values["inch"])
        meter = totalInch*0.0254
        window["output"].update(value=f"{meter} m")
    except ValueError: 
        sg.popup("Please provide two numbers")


window.close()