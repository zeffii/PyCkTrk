class MachinePrototype:

    def param_names(self):
        # return group param names, and track param names and dot representation
        # for instance   0: ("tpb", "...")
        group_param_info = [(v.name, v.dots) for k, v in self.group_params.items()] if hasattr(self, 'group_params') else []
        track_param_info = [(v.name, v.dots) for k, v in self.track_params.items()] if hasattr(self, 'track_params') else []
        return dict(group=group_param_info, track=track_param_info)
