# This file is part of project PyCkTrk. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/zeffii/PyCkTrk/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE

from machines import DrumMK1, Syn1, Tempo



class Machine:

    def __init__(self, machine_class):
        self.machine_instance = machine_class()
        self.presets = dict()
        self.pattern_list = dict()
        self.pattern_list.add(Pattern(self.machine_instance, 0))
        self.num_patterns = 1

    def add_pattern(self, name=''):
        self.pattern_list.add(Pattern(self.machine_instance, self.num_patterns))
        self.num_patterns += 1

    def remove_pattern(self, pattern):
        self.pattern_list[pattern.index].clear() 

    def get_pattern_scheme(self, pattern_length=16):
        self.machine_instance.get_pattern_scheme()

    def pattern_as_str(self, index):
        print(self.machine_instance[index])

class Pattern:

    def __init__(self, machine_instance, index, name='', length=32):
        self.index = index
        self.length = length
        self.current_track_count = 1
        self.name = name or str(self.index)
        self.scheme = machine_instance.get_pattern_scheme()
        self.scheme_ids = machine_instance.get_pattern_scheme_ids()
        self.pattern_data = self.generate_empty_pattern()
    
    def generate_empty_pattern(self):
        return [self.scheme for n in range(self.length)]

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

    def delete(self):
        self.machine_instance.pattern_list.pop(self)

    def clear(self):
        # wipe all data from pattern
        ...

    def __repr__(self):
        return data


