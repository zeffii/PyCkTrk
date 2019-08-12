# pylint: disable=E1101
# pylint: disable=C0301

from .machine import Machine

class SongFile:
    
    def __init__(self):
        self.name = "untitled"
        self.machines = set()

    def set_name(self, new_name):
        self.name = new_name

    def add_machine(self, machine_type):
        self.machines.add(Machine(machine_type)) 




