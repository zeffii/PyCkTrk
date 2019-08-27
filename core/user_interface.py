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
 
# chk_state = BooleanVar()
# chk_state.set(True) #set check state
 
# chk = Checkbutton(window, text='Choose', var=chk_state)
# chk.grid(column=0, row=0)


 
# def create_grid(event=None):
#     w = c.winfo_width() # Get current width of canvas
#     h = c.winfo_height() # Get current height of canvas
#     c.delete('grid_line') # Will only remove the grid_line

#     # Creates all vertical lines at intevals of 100
#     for i in range(0, w, 100):
#         c.create_line([(i, 0), (i, h)], tag='grid_line')

#     # Creates all horizontal lines at intevals of 100
#     for i in range(0, h, 100):
#         c.create_line([(0, i), (w, i)], tag='grid_line')


# c = tk.Canvas(window, height=1000, width=1000, bg='white')
# c.pack(fill=tk.BOTH, expand=True)
# c.bind('<Configure>', create_grid)

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
cell_width = 30

for i in range(5):
    x_start, y_start = [5, 5]
    y_pos = y_start + (line_height * i)
    cv1.create_line(x_start, y_pos, x_start + line_length, y_pos)

    for track in range(num_tracks):
        rc_x1 = x_start + line_length + (track * cell_width)
        rc_y1 = y_pos
        rc_x2 = rc_x1 + cell_width
        rc_y2 = rc_y1 + line_height
        cv1.create_rectangle(rc_x1, rc_y1, rc_x2, rc_y2, outline="#bbb", fill="#eee")

window.mainloop()




