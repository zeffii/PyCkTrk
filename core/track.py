class Track:
    
    def __init__(self, machine_instance):

        # ticks will contain a key/value pair of {tick_num: pattern (x of machine y), ...}
        self.ticks = {}

        # there can only be one machine used per track 
        self.owner = machine_instance

    def place_pattern_on_tick(self, tick, pattern):
        # must be a pattern owned by the machine_instance
        self.ticks[tick] = pattern

    def remove_pattern_on_tick(self, tick, pattern):
        self.ticks[tick].pop()

