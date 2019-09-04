# pylint: disable=c0301
# pylint: disable=c0103

# from core.song import SongFile
from core.ui_pattern_editor import PatternEditor
from core.ui_sequence_editor import Sequencer



def main():

    # new_song = SongFile()
    # new_song.set_name("wooop")
    # new_song.add_machine("GenDrumSyn1")
    # machine = list(new_song.machines)[0]
    # new_song.attach_machine_to_track(machine, 0)
    # machine.new_pattern(rows=12)

    # print(machine.pattern_dict[0])


    root = Tk()
    root.geometry('750x600')
    root.title("PyCkTrk! v.0001")

    sequencer = Sequencer()
    sequencer.focus_set()
    sequencer.bind("<Key>", sequencer.key_pressed)

    pattern_editor = PatternEditor()
    
    root.mainloop()


if __name__ == '__main__':
    main()
