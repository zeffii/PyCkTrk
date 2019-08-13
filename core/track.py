class Track:
    
    def __init__(self, machine_instance):
        self.ticks = {}
        self.owner = machine_instance

    def place_pattern_on_tick(self, tick, pattern):
        # must be a pattern owned by the machine_instance
        self.ticks[tick] = pattern

    def remove_pattern_on_tick(self, tick, pattern):
        self.ticks[tick].pop()

