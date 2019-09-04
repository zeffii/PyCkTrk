from tkinter import Tk, Canvas, Frame, BOTH, RIGHT


class PatternEditor(Frame):

    def __init__(self):
        super().__init__()
        self.init_pattern_editor_ui()

    def init_pattern_editor_ui(self):
        self.pack(side="top", fill="x")
        self.canvas = Canvas(self, width=750, height=300, background="#333")
        self.canvas.grid(row=0, column=1)        

