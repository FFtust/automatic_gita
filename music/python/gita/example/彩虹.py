import time
from chord import *
time.sleep(1)

from note import note
from chord import *

while True:
    note.play_note("3", 1 / 4)
    note.play_note("3", 1 / 8)
    note.play_note("3", 1 / 8)
    note.play_note("4", 1 / 8)
    note.play_note("4", 1 / 8)
    note.play_note("4", 1 / 8)
    note.play_note("5", 1 / 8)

    note.play_note("5", 1 / 8)
    note.play_note("1_u", 1 / 8)
    note.play_note("1_u", 1 / 2)
    note.play_note("1", 1 / 8)
    note.play_note("2", 1 / 8)
 
    note.play_note("3", 1 / 8)
    note.play_note("3", 1 / 8)
    note.play_note("3", 1 / 8)
    note.play_note("3", 1 / 8)
    note.play_note("3", 1 / 8)
    note.play_note("6", 1 / 8)
    note.play_note("7", 1 / 8)
    note.play_note("2", 1 / 8)