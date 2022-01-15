import mido
from mido import MidiFile


# mid = MidiFile("梦中的婚礼.mid")
mid = MidiFile("晴天（钢琴巨长版）.mid")

tempo = mido.bpm2tempo(80)

play_list = []
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    play_list.append([])

    passed_time = 0
    for msg in track:
        ab_time = mido.tick2second(msg.time, mid.ticks_per_beat, tempo)
        if ab_time < 0.1:
            ab_time = 0.06
        # real_time就是每一个事件在整个midi文件中的真实时间位置
        real_time = ab_time + passed_time
        passed_time += ab_time
        if msg.type == "note_on":
            if (msg.note % 12) in [1,3,6,8,10]:
                note = msg.note + 1
            else:
                note = msg.note

            play_list[i].append([note, 1, real_time, 0])
        if msg.type == "note_off":
            if (msg.note % 12) in [1,3,6,8,10]:
                note = msg.note + 1
            else:
                note = msg.note
            play_list[i].append([note, 0, real_time, 0])



import sys
sys.path.append('../../')
sys.path.append('../../../../')
if __name__ == "__main__":
    import piano.music_translate2 as music_translate
    music_parse = music_translate.music_trans([], beat = 80)
    play_list[0].extend(play_list[1])
    music_parse.play_list = play_list[0]
    music_parse.play_list_sort()
    music_parse.play_music(mode = "midi")