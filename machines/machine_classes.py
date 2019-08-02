# This file is part of project PyCkTrk. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/zeffii/PyCkTrk/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE

repeat_dots = lambda n: "." * n

class MachineUtils:

    def get_row_repr(self, kind):
        return ' '.join([repeat_dots(k[2]) for k in self.scheme[kind]["columns"].keys()])

    def get_param_names(self, kind):
        return ' '.join([k[0] for k in self.scheme[kind]["columns"].keys()])


    def get_pattern_scheme(self):
        scheme_dict = {}
        for section in ["group", "track"]:
            if self.scheme[section]:
                scheme_dict[section] = self.get_row_repr(section)
        return scheme_dict

    def get_pattern_scheme_ids(self):
        scheme_dict = {}
        for section in ["group", "track"]:
            if self.scheme[section]:
                scheme_dict[section] = self.get_param_names(section)
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
        self.scheme = "... .. .. .. .. .. .."


class Syn1(MachineUtils):
    def __init__(self):
        self.scheme = "... .. .. .. .. .. .."

