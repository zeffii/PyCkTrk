"""
this file describes the inner workings of Machine
"""

from . pattern import Pattern
from . machines import demo_machines

def make_instance_of(machine_type):
    """factory function to obtain a class instance of a machine type
    """

    class_ = getattr(demo_machines, machine_type)
    return class_()



class Machine:

    def __init__(self, machine_type, num_tracks=0):
        self.instance = make_instance_of(machine_type)
        self.num_tracks = num_tracks
        self.pattern_dict = {}
        self.new_pattern(rows=16)

    def new_pattern(self, rows=16):
        self.pattern_dict[len(self.pattern_dict)] = Pattern(self.instance, rows)
