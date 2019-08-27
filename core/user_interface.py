import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from tkinter import filedialog

# [ ] start new songfile
# [ ] save songfile
# [ ] load existing songfile
# [ ] add machine to song
# [ ] add machine to track
# [ ] create pattern for selected machine
# [ ] place pattern in track
# [ ] edit pattern

# pylint: disable=E1101
# pylint: disable=C0301

 
window = Tk()
window.title("PyCkTrk! v.0001")
window.geometry('550x600')
 

def clicked():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    print("pressed demo", file)
 


cv1 = Canvas(window, width=400, height=400, background="#aaa")
cv2 = Canvas(window, width=200, height=200, background="orange")
cv3 = Canvas(window, width=200, height=200, background="yellow")
cv4 = Canvas(window, width=200, height=200, background="green")

cv1.grid(row=0, column=0)
cv2.grid(row=0, column=1)
cv3.grid(row=1, column=0)
cv4.grid(row=1, column=1)

# btn = Button(cv1, text="demo", command=clicked)
# btn.grid(column=0, row=0) 
num_tracks = 6
line_length, line_height = 20, 15
cell_width = 50
cell_spacer = 3

for i in range(5):
    x_start, y_start = [5, 5]
    y_pos = y_start + (line_height * i)
    cv1.create_line(x_start, y_pos, x_start + line_length, y_pos, fill="#999")
    cv1.create_text(x_start, y_pos, anchor='nw', text=str(int(i * 16)), fill="#333")
    for track in range(num_tracks):
        rc_x1 = x_start + line_length + (track * cell_width) + (cell_spacer * track)
        rc_y1 = y_pos
        rc_x2 = rc_x1 + cell_width
        rc_y2 = rc_y1 + line_height
        cv1.create_rectangle(rc_x1, rc_y1, rc_x2, rc_y2, outline="#bbb", fill="#ddd")

for track in range(num_tracks):
    rc_x1 = x_start + line_length + (track * cell_width) + (cell_spacer * track)
    cv1.create_line(rc_x1 - 1, 0, rc_x1 - 1 , 200, fill="#888")

window.mainloop()




