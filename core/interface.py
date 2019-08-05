# This file is part of project PyCkTrk. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/zeffii/PyCkTrk/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE


class Machine:

    def __init__(self, machine_class):
        self.machine_instance = machine_class()
        self.presets = dict()
        self.pattern_list = dict()
        self.num_patterns = 0
        self.pattern_list[0] = Pattern(self.machine_instance, 0)

    def add_pattern(self, name=''):
        self.num_patterns += 1
        self.pattern_list[self.num_patterns] = Pattern(self.machine_instance, self.num_patterns)

    def remove_pattern(self, pattern):
        self.pattern_list[pattern.index].clear() 

    def get_pattern_scheme(self, pattern_length=16):
        # group_part = self.machine_instance.get_group_repr
        # track_part = self.machine_instance.get_track_repr

        self.machine_instance.get_pattern_scheme()


    def pattern_as_str(self, index):
        print(self.machine_instance[index])


class Pattern:

    def __init__(self, machine_instance, index, name='', length=4):
        self.ui_color = (0.7, 0.7, 0.7)
        self.index = index
        self.length = length
        self.current_track_count = 0
        self.name = name or str(self.index)
        
        self.scheme = machine_instance.get_pattern_scheme()
        self.scheme_ids = machine_instance.get_pattern_scheme("ids")
        self.pattern_data = self.generate_empty_pattern()
    
    def generate_empty_pattern(self):

        data = ""
        group = self.scheme['group']
        track = self.scheme['track'] if 'track' in self.scheme else ''
        row_template = group if not track else group + ' || ' + ((track + '|') * self.current_track_count)
        for row in range(self.length):
            data = data + (row_template + '\n')
        return data

    def resize_length(self, new_length):
        
        size_difference = new_length - self.length
        
        if size_difference > 0:
            self.pattern_data.extend([self.scheme for n in range(size_difference)])
        elif size_difference < 0:
            for n in range(abs(size_difference)):
               self.pattern_data.pop()

    def resize_tracks(self, num_tracks):
        ...

    def duplicate(self):
        ...

    def clear(self):
        # wipe all data from pattern
        ...

    def __repr__(self):
        return self.pattern_data


class SongFile:

    def __init__(self):
        # hold references to machines
        self.machines = {}

        # hold the visual location of machines in the sequence editor
        # also hold the pattern insertion points per machine track.
        # here we can separate the machines (tracks) columnar position, 
        # from the patterns on those tracks
        self.sequence_data = {"tracks": {} }   # = { "tracks": {}, "trk 1": {}....}

        # list of paths / wavetable data / or wavetable functions
        self.sample_pool = {}

        self.documentation = ""
        self.song_version = 0.0

        self.changes_detected = False

    def load_songfile(self, path):
        ...

    def save_songfile(self, path):
        ...

    def add_machine(self, name, machine_reference, column_index=-1):
        self.machines[name] = machine_reference

    def remove_machine(self):
        ...