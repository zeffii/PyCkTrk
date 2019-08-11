# pytrk_core2.py
# gpl3

class CKProperty:
    def __init__(self, **kwargs):
        self.params = kwargs
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def name(self):
        return self.params['name']
    def dots(self):
        if self.params['kind'] == 'hex':
            return '.' * len(self.params['max'])


class MachinePrototype:
    def param_names(self):
        # return group param names, and track param names and dot representation
        # for instance   0: ("tpb", "...")
        return {
            'group': [k, (v.name, v.dots) for k, v in self.group_params.items()] if hasattr(self, 'group_params') else [],
            'track': [k, (v.name, v.dots) for k, v in self.track_params.items()] if hasattr(self, 'track_params') else []}

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
            # voice num
            # voice detune range
            # voice detune ranomize drift
        }
        self.track_params = {
            #  name    type   length/dots
            0: CKProperty(name="note", kind="note", default="C-5"),
            1: CKProperty(name="vol", kind="hex", min='00', max='80', default="80"),
            2: CKProperty(name="pan", kind="hex", min='0', max='80', default="40")
        }
        self.max_tracks = 6
        self.source_path = "ck/generators/gensyn1.ck"


class Machine:

    def __init__(self, machine_type, num_tracks=0):
        self.instance = make_instance_of(machine_type, num_tracks)
        self.pattern_dict = {}
        self.new_pattern(rows=16)

    def new_pattern(self, rows=16):
        self.pattern_dict[len(self.pattern_dict)] = Pattern(self.instance, rows)




class Pattern:

    def __init__(self, machine_instance, rows=16, name=None):
        self.machine_instance = machine_instance
        self.data = self.generate_empty_pattern(rows, name)
        self.name = name or ""
        self.colour = [0.9, 0.9, 0.9]

    def generate_empty_pattern(self, rows, name):
        data = {"group": {}, "tracks": {}}
        data['rows'] = rows
        return data

    def change_row_count(self, new_count):
        diff = self.data['rows'] - new_count
        if diff == 0:
            # do nothing
            return
        elif diff < 0:
            ... # add abs(diff) rows

        elif diff > 0:
            ... # remove abs(diff) rows

        # change bookkeeping (for now)
        self.data['rows'] = new_count

    def wipe_pattern_data(self):
        ...

    def interpolate_selection(self, selection_params):
        ...

    def transpose_selection(self, selection_params):
        ...

    def print_readable(self):
        columns_in_group = self.machine_instance.columns_in_group
        columns_in_track = self.machine_instance.columns_in_track
        num_tracks = len(self.data["tracks"])

        for row in range(self.data['rows']):
            ...

    def clone(self):
        new_pattern = Pattern(self.machine_instance, rows=self.data['rows'])
        new_pattern.data = deepcopy(self.data)
        return new_pattern
