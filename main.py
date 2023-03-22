import PySimpleGUI as sg

lable1 = sg.Text("Select the files to compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Browse")

lable2 = sg.Text("Select the Destined file")
input2 = sg.Input()
button2 = sg.FolderBrowse("Browse")

compressButton = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout = [
                       [lable1,input1, button1],
                       [lable2,input2,button2],
                   [compressButton]])
window.read()
window.close()