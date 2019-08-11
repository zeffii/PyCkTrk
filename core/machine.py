"""
this file describes the inner workings of Machine
"""


from .pattern import Pattern

class Machine:

    def __init__(self, machine_type, num_tracks=0):
        self.instance = make_instance_of(machine_type, num_tracks)
        self.pattern_dict = {}
        self.new_pattern(rows=16)

    def new_pattern(self, rows=16):
        self.pattern_dict[len(self.pattern_dict)] = Pattern(self.instance, rows)

