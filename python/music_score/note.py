from chord import *
import time
note_table = \
{
    "-"  : (),
    "5_u": (1, 3),
    "4_u": (1, 1),
    "3_u": (1, 0),
    "2_u": (2, 3),
    "1_u": (2, 1), 
    "7":   (2, 0),
    "6":   (3, 2),
    "#5":  (3, 1),
    "5":   (3, 0),
    "#4":  (4, 4),
    "4":   (4, 3),
    "3":   (4, 2),
    "2":   (4, 0),
    "1":   (5, 3),
    "7_d": (5, 2),
    "6_d": (5, 0),
    "#5_d": (6, 4),
    "5_d": (6, 3),
    "#4_d" : (6, 2),
    "4_d": (6, 1),
    "3_d": (6, 0),
}

class note_control():
    def __init__(self):
        self.grade_pizz_interval = 0.1
        self.tempo = 60
        self.second_per_beat = 2.5

    def play_note(self, note, beats = None):
        if note in note_table:
            chrod_id = note_table[note][0]
            grade = note_table[note][1]
            chords[chrod_id].set_grade(grade, True)
            time.sleep(self.grade_pizz_interval)
            chords[chrod_id].pizz(True)

        if beats != None:
            time.sleep(self.second_per_beat * beats - self.grade_pizz_interval)

    def get_interval(self):
        return self.grade_pizz_interval

    def play_music_score(self, ms):
        interval = (60 / self.tempo) / ms[tab] # unit: second
        for item_sec in ms:
            for notes in item_sec:
                pass


note = note_control()

example_ms = \
{
    "tab": 3,
    "ms_info":\
    (
        (0, 0, ("5", "5")),
        ("6", "5", "1_u"),
        ("7", "-", ("5", "5")),
        ("6", "5", "2_u"),
        ("1_u", "-", ("5", "5")),
    )
}