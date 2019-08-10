# pytrk_core2.py
# gpl3


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
