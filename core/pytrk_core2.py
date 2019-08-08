# pytrk_core2.py
# gpl3


class Machine:

    def __init__(self, machine_type, num_tracks=0):
        self.internals = make_instance_of(machine_type, num_tracks)
        self.pattern_dict = {}

    def add_pattern(self):
        self.pattern_dict




class Pattern:

    def __init__(self, machine_reference):
        self.machine_reference = machine_reference

    def change_row_count(self):
        ...

    def wipe_pattern_data(self):
        ...

    def interpolate_selection(self, row_start, row_end, column_start, column_end):
        ...

