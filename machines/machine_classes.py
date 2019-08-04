# This file is part of project PyCkTrk. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/zeffii/PyCkTrk/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE

repeat_dots = lambda n: "." * n

def prop(**kwargs):
    param = lambda: None
    for k, v in kwargs.items():
        setattr(param, k, v)
    param.stored_prop_names = [name for name in kwargs.keys()]
    return param

class MachineUtils:

    def get_row_repr(self, kind):
        return ' '.join([repeat_dots(k[2]) for k in self.scheme[kind]["columns"].keys()])

    def get_param_names(self, kind):
        return ' '.join([k[0] for k in self.scheme[kind]["columns"].keys()])


    def get_pattern_scheme(self, kind=None):

        getter_func = self.get_row_repr if not kind else self.get_param_names

        scheme_dict = {}
        for section in ["group", "track"]:
            if self.scheme[section]:
                scheme_dict[section] = gett_func(section)
        return scheme_dict



class Tempo(MachineUtils):
    def __init__(self):
        self.scheme = {
            "group": {
                "name": "params",
                "description": "bpm and tpb",
                "columns": {
                    #  name    type   length/dots
                    0: ("bpm", "hex", 3),
                    1: ("tpb", "hex", 2)
                }},
            "track": None
        }

class DrumMK1(MachineUtils):
    def __init__(self):
        self.scheme = {
            "group": {
                "name": "params",
                "description": "drum parameters",
                "columns": {
                    #  name    type   length/dots
                    0: ("thump", "hex", 2),
                    1: ("volume", "hex", 2),
                    2: ("attack", "hex", 2),
                    3: ("decay", "hex", 2),
                    4: ("sustain", "hex", 2),
                    5: ("release", "hex", 2),
                    6: ("adsr speed", "hex", 2),
                    7: ("click", "bool", 1),
                }},
            "track": {
                "name": "track",
                "description": "note track",
                "columns": {
                    #  name    type   length/dots
                    0: ("note", "note", 3),
                    1: ("vol", "hex", 2),
                    2: ("pan", "hex", 2)
                }},
            "max tracks": 1
        }


class Syn1(MachineUtils):
    def __init__(self):
        self.scheme = {
            "group": {
                "name": "params",
                "description": "synth params",
                "columns": {
                    #  name    type   length/dots
                    0: ("osc 1", "enum", 1),
                    1: ("osc 2", "enum", 1),
                    2: ("osc 3", "enum", 1),
                    3: ("mix 1", "hex", 2),
                    4: ("mix 2", "hex", 2),
                    5: ("mix 3", "hex", 2),
                    6: ("attack", "hex", 2),
                    7: ("decay", "hex", 2),
                    8: ("sustain", "hex", 2),
                    9: ("release", "hex", 2),
                    10: ("adsr speed", "hex", 2),
                }},
            "track": {
                "name": "track",
                "description": "note track",
                "columns": {
                    #  name    type   length/dots
                    0: ("note", "note", 3),
                    1: ("vol", "hex", 2),
                    2: ("pan", "hex", 2)
                }},
            "max tracks": 6
        }

