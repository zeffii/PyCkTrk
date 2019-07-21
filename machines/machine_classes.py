# gpl3

class MachineUtils:

    def get_pattern_scheme(self):
        return self.scheme.split()


class Tempo(MachineUtils):
    def __init__(self):
        self.scheme = ".. .."


class DrumMK1(MachineUtils):
    def __init__(self):
        self.scheme = "... .. .. .. .. .. .."


class Syn1(MachineUtils):
    def __init__(self):
        self.scheme = "... .. .. .. .."
