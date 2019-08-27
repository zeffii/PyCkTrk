from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.init_sequencer_ui()

    def init_sequencer_ui(self):
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self, width=400, height=400, background="#aaa")
        canvas.grid(row=0, column=0)

        num_tracks = 6
        line_length, line_height = 35, 15
        cell_width = 50
        cell_spacer = 3
        x_start, y_start = [5, 20]

        for i in range(5):
            # draw row divider ( left hand )
            y_pos = y_start + (line_height * i)
            canvas.create_line(x_start, y_pos, x_start + line_length, y_pos, fill="#999")
            
            # draw row tick
            canvas.create_text(x_start, y_pos, anchor='nw', text=str(int(i * 16)), fill="#333")
            
            # draw individual cells
            for track in range(num_tracks):
                rc_x1 = x_start + line_length + (track * cell_width) + (cell_spacer * track)
                rc_y1 = y_pos
                rc_x2 = rc_x1 + cell_width
                rc_y2 = rc_y1 + line_height
                canvas.create_rectangle(rc_x1, rc_y1, rc_x2, rc_y2, outline="#bbb", fill="#ddd")

        # draw column divs
        for track in range(num_tracks):
            rc_x1 = x_start + line_length + (track * cell_width) + (cell_spacer * track)
            canvas.create_line(rc_x1 - 1, 0, rc_x1 - 1 , 200, fill="#888")

        print('here')


def main():

    root = Tk()
    ex = Example()
    root.geometry('750x600')
    root.title("PyCkTrk! v.0001")
    root.mainloop()


if __name__ == '__main__':
    main()
