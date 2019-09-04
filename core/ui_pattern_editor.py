from tkinter import Tk, Canvas, Frame, BOTH, RIGHT


# from song import Song


demo_machine = machine.make_instance_of("GenDrumSyn1")
print(demo_machine)


class PatternEditor(Frame):

    def __init__(self):
        super().__init__()
        self.init_pattern_editor_ui()

    def init_pattern_editor_ui(self):
        self.pack(side="top", fill="x")
        self.canvas = Canvas(self, width=750, height=300, background="#333")
        self.canvas.grid(row=0, column=1)        

