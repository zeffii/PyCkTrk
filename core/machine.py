"""
this file describes the inner workings of Machine
"""


from . pattern import Pattern

def make_instance_of(machine_type, num_tracks):
    """factory function to obtain a class instance of a machine type
    """

    # import importlib
    # module = importlib.import_module(module_name)
    # class_ = getattr(module, class_name)
    # instance = class_()

    return




class Machine:

    def __init__(self, machine_type, num_tracks=0):
        self.instance = make_instance_of(machine_type, num_tracks)
        self.pattern_dict = {}
        self.new_pattern(rows=16)

    def new_pattern(self, rows=16):
        self.pattern_dict[len(self.pattern_dict)] = Pattern(self.instance, rows)

