import PySimpleGUI as sg

tm_number = sg.Text("Technical Manual Number:",  font=(24,24)),\
    sg.Input(key='tm_number', font=(24,24), size=(48,24))
review = sg.Text("Type of Review:         ",  font=(24,24)),\
    sg.Input(key='review', font=(24,24), size=(12,24))
pages = sg.Text("Number of Pages: ",  font=(24,24)),\
    sg.Input(key='pages', font=(24,24), size=(12,24))
submission_date = sg.Text("Date of Submission: ",  font=(24,24)),\
    sg.Input(key='submission_date', font=(24,24), size=(12,24))
writer = sg.Text("Writer's Name:       ",  font=(24,24)),\
    sg.Input(key='writer', font=(24,24), size=(12,24))
col1 = [review, submission_date]
col2 = [writer, pages]

layout = [
    [sg.Text("Writer's Submission Form", font=(48,48))],
     tm_number,
    [sg.Column(col1), sg.Column(col2)],
    [sg.Button("SUBMIT FOR REVIEW", size=(24,1), font=24)]
]

window = sg.Window("Technical Manual Engineering Review (TMER)", layout).read(close=True)
