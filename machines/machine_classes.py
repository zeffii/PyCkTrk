# gpl3

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
