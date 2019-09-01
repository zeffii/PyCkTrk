from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.caret_cell = [0, 0]
        self.cell_width = 50
        self.cell_spacer = 3
        self.line_height = 15
        self.line_length = 35

        self.init_sequencer_ui()

    def move_caret(self, direction):

        if direction in {'w','s'}:
            y = 1 if direction == 's' else -1
            x = 0
        else:
            y = 0
            x = -1 if direction == 'a' else 1

        self.caret_cell[0] += x
        self.caret_cell[1] += y

        #
        # limit caret cell to x > 0  and y > 0
        #

        print(self.caret_cell)        
        self.canvas.move(self.caret, x * (self.cell_width + self.cell_spacer), y * self.line_height)

    def init_sequencer_ui(self):

        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=400, height=400, background="#aaa")
        self.canvas.grid(row=0, column=0)

        num_tracks = 6
        x_start, y_start = [5, 15]

        for i in range(5):
            # draw row divider ( left hand )
            y_pos = y_start + (self.line_height * i)
            self.canvas.create_line(x_start, y_pos, x_start + self.line_length, y_pos, fill="#999")
            
            # draw row tick
            self.canvas.create_text(x_start, y_pos, anchor='nw', text=str(int(i * 16)), fill="#333")
            
            # draw individual cells
            for track in range(num_tracks):
                rc_x1 = x_start + self.line_length + (track * self.cell_width) + (self.cell_spacer * track)
                rc_y1 = y_pos
                rc_x2 = rc_x1 + self.cell_width
                rc_y2 = rc_y1 + self.line_height
                self.canvas.create_rectangle(rc_x1, rc_y1, rc_x2, rc_y2, outline="#bbb", fill="#ddd")

        # draw column divs
        for track in range(num_tracks):
            rc_x1 = x_start + self.line_length + (track * self.cell_width) + (self.cell_spacer * track)
            self.canvas.create_line(rc_x1 - 1, 0, rc_x1 - 1 , 200, fill="#888")

        # draw column track names
        for track in range(num_tracks):
            rc_x1 = x_start + self.line_length + (track * self.cell_width) + (self.cell_spacer * track)
            self.canvas.create_text(rc_x1, 0, text="trk:" + str(track), anchor="nw", fill="#222")

        # draw sequencer caret
        track = 0
        y_pos = y_start
        rc_x1 = x_start + self.line_length
        rc_y1 = y_pos
        rc_x2 = rc_x1 + self.cell_width
        rc_y2 = rc_y1 + self.line_height
        self.caret = self.canvas.create_rectangle(rc_x1, rc_y1, rc_x2, rc_y2, outline="#bbb", fill="#36a")

    def key_pressed(self, event):

        if event.char in {'s','a','w','d'}:
            self.move_caret(event.char)
        else:
            print(event.char, 'is unhandled')



def main():


    root = Tk()
    ex = Example()
    ex.focus_set()
    root.geometry('750x600')
    ex.bind("<Key>", ex.key_pressed)
    root.title("PyCkTrk! v.0001")
    root.mainloop()


if __name__ == '__main__':
    main()
