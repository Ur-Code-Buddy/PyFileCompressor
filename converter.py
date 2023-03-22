import PySimpleGUI as sg

lable1 = sg.Text("Enter Feet")
input1 = sg.Input()

lable2 = sg.Text("Enter inches")
input2 = sg.Input()

button = sg.Button("Submit")

window = sg.Window("file converter",
                   layout= [[lable1,input1],
                            [lable2,input2],
                            [button]
                   ])

window.read()
window.close()
