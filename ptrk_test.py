# This file is part of project PyCkTrk. It's copyrighted by the contributors
# recorded in the version control history of the file, available from
# its original location https://github.com/zeffii/PyCkTrk/commit/master
#  
# SPDX-License-Identifier: GPL3
# License-Filename: LICENSE

from machines.machine_classes import DrumMK1, Syn1, Tempo
from core.interface import SongFile, Pattern, Machine


song = SongFile()
song.add_machine("tempo", Machine(Tempo), 0)
# song.machines["synth"] = Machine(Syn1)
print(song.machines)