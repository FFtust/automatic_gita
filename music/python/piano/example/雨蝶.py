music_table1 = \
(
    ("0=1",),
    # 1
    ("0=3/8", "1+:3:7=1/8"),
    ("6=3/4",),
    ("0=1/4", "0=1/8", "1+:3:7=1/8"),
    ("6=3/4",),

    # 5
    ("0=3/8", "6:1+:5=1/8"),
    ("4+=3/8", "0=1/4", "6=1/8"),
    ("5,2=1/4", "0=1/8", "5+,5=1/4", "3+=1/8"),
    ("6+,6=1/2", "0:1+=1/8"),

    #9
    ("6=3/8", "1++,1+:3+,3:7+,7=1/8"),
    ("6+,6=3/8", "0=1/4", "7-=1/8"),
    ("6-=1/8", "0=1/4", "1++,1+:3+,3:7+,7=1/8"),
    ("6+,6=3/8", "0=1/4", "7-=1/8"),

    # 13
    ("6-=1/8", "0=1/4", "6+,6:1++,1+:5++,5+=1/8"),
    ("4++,4+=3/8", "4++,4+:3++,3+:4++,4+=1/8"),
    ("5++,2++,5+=1/4", "0=1/8", "5++,5+:3++,3+:5++,5+=1/8"),
    ("6++,6+=1/2", "0:3=1/8"),

    #17
    ("6=3/8", "0:1+:7=1/8"),
    ("6=1/4", "5=1/8", "6=1/4", "5=1/8"),
    ("6:6:5=1/8", "6=1/4", "1+=1/8"),
    ("2+:2+:1+=1/8", "2+=1/4", "1+=1/8"),

    #21
    ("6=3/8", "0:1+:2+=1/8"),
    ("3+:3+:3+:3+:2+:1+=1/8",),
    ("3+:3+:3+:3+:2+:1+=1/8",),
    ("3+=3/4",),

    #25
    ("0=1/2", "1+:7,7-=1/8"),
    ("6=1/4", "5=1/8", "6=1/4", "5=1/8"),
    ("6:6:5=1/8", "6=1/4", "1+=1/8"),
    ("2+:2+:2+:2+:6=1/8","3+=1/4"),

    #29
    ("2+=3/8", "1+:2+=1/8"),
    ("3+:3+:3+:3+:2+:1+=1/8",),
    ("3+:3+:3+:3+:2+:1+=1/8",),
    ("3+=3/4",),

    #33
    ("5+,3+,7=1/4", "0=1/8", "3+,7:5+,3+,7:3+,7=1/8"),
    ("6+,4+,1+=1/4", "5+,2+,7:6+,4+,1+:5+,3+,7:2+,7=1/8"),
    ("3+,1+,5=3/8", "3+,7:5+,3+,7:3+,7=1/8"),
    ("6+,4+,1+=1/4", "5+,2+,7:6+,4+,1+:5+,3+,7:2+,7=1/8"),

    #37
    ("3+,1+,5=3/8", "6:1+,6:6=1/8"),
    ("3+=1/4", "2+:2+:1+:6=1/8"),
    ("5+,3+,7=1/4", "5+:5+:3+:2+=1/8"),
    ("3+,1+=1/4", "3+:3+:2+:1+=1/8"),

    #41
    ("1+,6=1/4", "0:3+,7:5+,3+,7:3+,7=1/8"),
    ("6+,3+,1+=1/4", "5+,2+,7:6+,4+,1+:5+,3+,7:2+,7=1/8"),
    ("3+,1+,5=3/8", "3+,7:5+,3+,7:3+,7=1/8"),
    ("1++,6+,4+=1/4", "1++,6+,4+:1++,6+,4+:6+,2+:5+,1+"),

    #45
    ("3+,1+,5=3/8", "6:1+,6:6=1/8"),
    ("3+,7,5=1/4", "2+,6,4:2+,6,4:1+,5,3:6,3,1=1/8"),
    ("5+,3+,7=1/4", "5+,3+,7:5+,3+,7:3+,7,5=1/8", "5+,2+,7=1/4"),
    ("6+,3+,1+=1/4", "0=1/4", "1,6-,4-=1/8"),

    #49
    ("1,6,4=3/8", "1++,1+:7+,7:5+,5=1/8"),
    ("6+,4+,1+,6=1/4", "5+:6+,4+:5+:2+=1/8"),
    ("3+:1+=3/8", "3+:5+:3+=1/8"),
    ("6+,4+,1+=1/4", "5+,2+,7:6+,4+,1+:5+,3+,7:2+,7=1/8"),

    #53
    ("3+,1+,5=3/8", "6:1+,6:6=1/8"),
    ("3+=1/4", "2+:2+:1+:6=1/8"),
    ("5+,3+,7=1/4", "5+:5+:3+:2+=1/8"),
    ("3+,1+=1/4", "3+:3+:2+:1+=1/8"),
)

music_table2 = \
(
    ("0=1",),

    # 1
    ("0=3/4",),
    ("6--:3-:7-:3,1:3-=1/8", "7-=1/2"),
    ("0=1/4", "5--=1/8"),
    ("4--:1-:5-=1/8", "3,1=3/8"),

    #5
    ("6-=3/8", "0=1/4", "3--=1/8"),
    ("2--:6--:4-=1/8", "4,1=1/8", "0=1/4"),
    ("3--:7--:5-=1/8", "0=3/8"),
    ("4--:1-:5-:6-:1:0=1/8",),

    #9
    ("0=3/8", "3-,7--=1/4", "3-,7--,3--=1/8"),
    ("6--,6---:3-:7-:3,1:3-:6--,6---=1/8", ),
    ("6--,6---:3-:7-:3,1:3-:5--,5---=1/8",),
    ("4--,4---:1-:4-:1,6-:4-:4--,4---",),

    #13
    ("4--,4---:1-:4-:1,6-:4-:3--,3---=1/8",),
    ("2--,2---:6--:4-:4,1:4-:4--,4---=1/8",),
    ("3--,3---:7--:5-:2,7-:5-:5--,5---=1/8",),
    ("4--,4---:1-:5-:6-:1:4--,4---=1/8",),

    #17
    ("4--,4---=1/2", "0=1/4"),
    ("6--:3-:6-:1:6-:3-=1/8",),
    ("6--:3-:6-:1:6-:3-=1/8",),
    ("2--:2-:4-:6-:4-:2-=1/8",),

    #21
    ("2--:2-:4-:6-:4-:2-=1/8",),
    ("1--:3-:5-:1:5-:3-=1/8",),
    ("5--:3-:5-:1:5-:3-=1/8",),
    ("3--:7--:3-:5-:3-:7--,3--=1/8",),

    #25
    ("3--:0:2-:3-:5-:3--=1/8",),
    ("6---:3-:6-:1:6-:3-=1/8",),
    ("6---:3-:6-:1:6-:3-=1/8",),
    ("2--:2-:4-:6-:4-:2-=1/8",),

    #29
    ("2--:2-:4-:6-:4-:2-=1/8",),
    ("1--:3-:5-:1:5-:3-=1/8",),
    ("5--:3-:5-:1:5-:3-=1/8",),
    ("3--:7--:3-:5-:3-:7--,3--=1/8",),



)


import sys
sys.path.append('../../')
sys.path.append('../../../../')
if __name__ == "__main__":
    import piano.music_translate2 as music_translate
    music_parse = music_translate.music_trans([music_table], beat = 96)
    music_parse.music_to_play_table()
    music_parse.play_music()