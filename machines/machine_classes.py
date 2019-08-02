# This file is part of project PyCkTrk. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/zeffii/PyCkTrk/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE

class MachineUtils:

    def get_pattern_scheme(self):
        return self.scheme.split()

    def get_pattern_scheme_ids(self):
        return self.scheme_ids.split()

class Tempo(MachineUtils):
    def __init__(self):
        self.scheme = ".. .."
        self.scheme_ids = "bpm tpb"


class DrumMK1(MachineUtils):
    def __init__(self):
        self.scheme = "... .. .. .. .. .. .."
        self.scheme_ids = "note vol a d s r pg"

class Syn1(MachineUtils):
    def __init__(self):
        self.scheme = "... .. .. .. .. .. .."
        self.scheme_ids = "note vol a d s r pg"
