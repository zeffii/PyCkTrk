"""
this file contains a few demo machines to allow UI coding to take place

"""


from PyCkTrk.core.properties import CKProperty
from PyCkTrk.core.machine_prototype import MachinePrototype

# pylint: disable=C0301
# pylint: disable=R0903

class GenTempo(MachinePrototype):
    """
    This machine represents:
    - bpm (beats per minute)
    - tpb (ticks per beat)
    """
    def __init__(self):
        self.group_params = {
            0: CKProperty(name='bpm', kind='hex', min='000', max='200', default='090'),
            1: CKProperty(name='tpb', kind='hex', min='00', max='20', default='08')
        }

class GenDrumSyn1(MachinePrototype):
    """
    A primitive drummachine example
    """
    def __init__(self):
        self.group_params = {
            0: CKProperty(name='volume', kind='hex', min='000', max='200', default='090'),
            1: CKProperty(name='thump', kind='hex', min='00', max='20', default='08'),
            2: CKProperty(name='attack', kind='hex', min='00', max='20', default='02'),
            3: CKProperty(name='decay', kind='hex', min='00', max='60', default='28'),
            4: CKProperty(name='sustain', kind='hex', min='00', max='60', default='48'),
            5: CKProperty(name='release', kind='hex', min='00', max='50', default='18'),
            6: CKProperty(name='speed adsr', kind='hex', min='00', max='80', default='10'),
            7: CKProperty(name='click', kind='hex', min='00', max='01', default='01')
        }
        self.track_params = {
            0: CKProperty(name="note", kind="note", default="C-5"),
            1: CKProperty(name="vol", kind="hex", min='00', max='80', default="80"),
            2: CKProperty(name="pan", kind="hex", min='0', max='80', default="40")
        }
        self.max_tracks = 1
        self.source_path = "ck/generators/drumsyn1.ck"

class GenSynth1(MachinePrototype):
    """
    gen synth 1 will contain the first elaborate demo
    - num voices per note
    - voice detunes max
    - voice detune travel rate
    """
    def __init__(self):
        self.group_params = {
            0: CKProperty(name="osc 1", kind="enum", default="SAW", enums=["SAW", "SIN", "TRI", "NOISE"]),
            1: CKProperty(name="osc 2", kind="enum", default="SAW", enums=["SAW", "SIN", "TRI", "NOISE"]),
            2: CKProperty(name="osc 3", kind="enum", default="SAW", enums=["SAW", "SIN", "TRI", "NOISE"]),
            3: CKProperty(name="mix 1", kind="hex", min='0', max='80', default='80'),
            4: CKProperty(name="mix 2", kind="hex", min='0', max='80', default='00'),
            5: CKProperty(name="mix 3", kind="hex", min='0', max='80', default='00'),
            6: CKProperty(name="attack", kind="hex", min='0', max='80', default='04'),
            7: CKProperty(name="decay", kind="hex", min='0', max='80', default='40'),
            8: CKProperty(name="sustain", kind="hex", min='0', max='80', default='30'),
            9: CKProperty(name="release", kind="hex", min='0', max='80', default='20'),
            10: CKProperty(name="speed adsr", kind="hex", min='0', max='80', default='10')
        }
        self.track_params = {
            0: CKProperty(name="note", kind="note", default="C-5"),
            1: CKProperty(name="vol", kind="hex", min='00', max='80', default="80"),
            2: CKProperty(name="pan", kind="hex", min='0', max='80', default="40")
        }
        self.max_tracks = 6
        self.source_path = "ck/generators/gensyn1.ck"





