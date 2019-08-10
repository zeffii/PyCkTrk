# pytrk_core2.py
# gpl3


class Machine:

    def __init__(self, machine_type, num_tracks=0):
        self.instance = make_instance_of(machine_type, num_tracks)
        self.pattern_dict = {}

    def add_pattern(self, rows):
        self.pattern_dict




class Pattern:

    def __init__(self, machine_instance, rows=16):
        self.machine_instance = machine_instance
        self.data = {"group": {}, "tracks": {}}
        self.data['rows'] = rows

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

    def interpolate_selection(self, row_start, row_end, column_identifier):
        ...

    def transpose_selection(self):
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
