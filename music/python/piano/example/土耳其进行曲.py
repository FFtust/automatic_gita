music_table = \
(
 	("0", "-", "-", "-"),
 	("{'COPY_START':0}",),
    ("0=1/4", "7:6:5#:6=1/16"),
    ("1+:0=1/8", "2+:1+:7:1+=1/16",),
    ("3+:0=1/8", "4+:3+:2+#:3+=1/16"),
    ("7+:6+:5+#:6+:7+:6+:5+#:6+=1/16",),

    ("1++=1/4", "6+:1++=1/8",),
    ("5+:6+=1/64", "7+=6/64", "6+,4+#:5+,3+:6+,4+#=1/8"),
    ("5+:6+=1/64", "7+=6/64", "6+,4+#:5+,3+:6+,4+#=1/8"),
    ("5+:6+=1/64", "7+=6/64", "6+,4+#:5+,3+:6+,4+#=1/8"),

    # 9
    ("3+=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),
    ("3+,1+:4+,2+=1/8",),
    ("5+,3:5+,3=1/8", "6+:5+:4+:3+=1/16"),
    ("2+,7:5:3+,1+:4+,2+=1/8",),

    # 13
    ("5+,3:5+,3=1/8", "6+:5+:4+:3+=1/16"),
    ("2+,7=1/4", "1+,6:2+,7=1/8"),
    ("3+,1+:3+,1+=1/8", "4+:3+:2+:1+=1/16"),
    ("7,5:3:1+,6:2+,7=1/8",),

    # 17
    ("3+,1+:3+,1+=1/8", "4+:3+:2+:1+=1/16"),
    ("7,5#=1/4", "7:6:5:6=1/16"),
    ("1+:0=1/8", "2+:1+:7:1+=1/16"),
    ("3+:0=1/8", "4+:3+:2+#:3+=1/16"),

    # 21
    ("7+:6+:5+#:6+:7+:6+:5+:6+=1/16",),
    ("1++=1/4", "6+:7+=1/8"),
    ("1++:7+:6+,5+#=1/8",),
    ("6+:3+:4+:2+=1/8",),

    # 25
    ("1+=1/4", "7=3/16", "6:7=1/32",),
    ("6=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    ("{'MOVING':-3}",),
    ("1++,1+:2++,2+=1/4",),
    ("3++,3+=1/4", "1++,1+:2++,2+=1/8"),

    # 29
    ("3++,3+:2++,2+:1++,1+:7+,7=1/8",),
    ("6+,6:7+,7:1++,1+:2++,2+=1/8",),
    ("7+,7:5+,5:1++,1+:2++,2+=1/8",),
    ("3++,3+=1/4", "1++,1+:2++,2+=1/8",),

    # 33
    ("3++,3+:2++,2+:1++,1+:7+,7=1/8",),
    ("6+,6:2++,2+:7+,7:5+,5=1/8",),
    ("1++,1+=1/4",),

 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    ("3++:4++,3++:2++=1/16",),

    # 37
    ("1++:2++,1++:7+:6+:1++:7+:6+=1/16",),
    ("5+#:5+#,7+:5+#:3+:4+#:5+#:3+=1/16",),
    ("6+:5+#,5+#:7+:1++:7+:1++:2++=1/16",),
    ("3++:2++#,3++:3++:3++:4++:3++:2++=1/16",),

    # 41
    ("1++:2++,1++:7+:6+:1++:7+:6+=1/16",),
    ("5+:6+,7+:5+:3+:4+#:5+:4+=1/16",),
    ("4+#:5+,6+:4+:2+#:3+:4+:2+=1/16",),
    ("3+=1/4",),

 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    # 45
    ("5+:4+:3+:2+=1/16",),
    ("1+:2+:3+:4+:5+:6+:7+:1++=1/16",),
    ("1++:7+:6+:5+:5+:4+:3+:2+=1/16",),
    ("1+:2+:3+:4+:5+:6+:7+:1++=1/16",),

    # 49
    ("1++#:2++=1/8", "5+:4+:3+:2+=1/16"),
    ("1+:2+:3+:4+:5+:6+:7+:1++=1/16",),
    ("1++:7+:6+:5+:5+:4+:3+:2+=1/16",),
    ("3+:5+:1+:3+:2+:4+:7:2+=1/16",),

    # 53
    ("1+=1/4","3++:4++:3++:2++=1/16",),
    ("1++:2++:1++:7+:6+:1++:7+:6+=1/16",),
    ("5+#:5+#:7+:5+#:3+:4+#:5+#:3+=1/16",),
    ("6+:5+#:5+#:7+:1++:7+:1++:2++=1/16",),

    # 57
    ("3++:2++#:3++:2++#:3++:2++#:3++:1++#=1/16",),
    ("4++:3++:4++:3++:4++:3++:4++:3++=1/16",),
    ("4++:3++:2++:1++:7+:1++:2++:7+=1/16",),
    ("1++:2++:3++:6+:5+#:6+:7+:5+=1/16",),

    # 61
    ("6+=1/4",),

 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    ("1++,1:2++,2=1/4"),
    ("3++,3+=1/4", "1++,1+:2++,2+=1/8"),
    ("3++,3+:2++,2+:1++,1+:7+,7=1/8",),

    # 65
    ("6+,6:7+,7:1++,1+:2++:2+=1/8",),
    ("7+,7:5+,5:1++,1+:2++:2+=1/8",),
    ("3++,3=1/4", ":1++,1+:2++:2+=1/8",),
    ("3++,3+:2++,2+:1++,1+:7+,7=1/8",),

    # 69
    ("6+,6:2++,2+:7+7:5+,5=1/8",),
    ("1++,1+=1/4",),
 	
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    ("7:6:5#:6=1/16",),
    ("1+:0=1/8", "2+:1+:7:1+=1/16"),

    # 73
    ("3+:0=1/8", "4+:3+:2+#:3+=1/16"),
    ("7+:6+:5+#:6+:7+:6+:5+:6+=1/16",),
    ("1++=1/4", "6+:1++=1/8"),
    ("5+:6+=1/64", "7+=6/64", "6+,4+#:5+,3+:6+,4+=1/8"),

    # 77
    ("5+:6+=1/64", "7+=6/64", "6+,4+#:5+,3+:6+,4+=1/8"),
    ("5+:6+=1/64", "7+=6/64", "6+,4+#:5+,3+:6+,4+=1/8"),
    ("3+=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    ("3+,1+:4+,2+=1/8",),

    # 81
    ("5+,3+:5+,3+=1/8", "6+:5+:4+:3+=1/16"),
    ("2+,7:5:3+,1+:4+,2+=1/8",),
    ("5+,3+:5+,3+=1/8", "6+:5+:4+:3+=1/16"),
    ("2+,7=1/4","1+,6:2+,7=1/8"),

    # 85
    ("3+,1+:3+,1+=1/8", "4+:3+:2+:1+=1/16"),
    ("7,5#:3:1+,6:2+,7=1/8",),
    ("3+,1+:3+,1+=1/8", "4+:3+:2+:1+=1/16"),
    ("7,5#:3:1+,6:2+,7=1/8",),

    # 89
    ("1+:0=1/8", "2+:1+:7:1+=1/16"),
    ("3+:0=1/8", "4+:3+:2+#:3+=1/16"),
    ("7+:6+:5+#:6+:7+:6+:5+:6+=1/16",),
    ("1++=1/4", "6+:7+=1/8"),

    # 93
    ("1++:7+:6+:5+#=1/8",),
    ("6+:3+:4+:2+=1/8",),
    ("1+=1/4", "7+=3/16", "6:7=1/32"),
    ("6=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

    # 97
    ("1+:1++:2+:2++=1/16",),
    ("3+:3++=1/16", "0=1/8", "1+:1++:2+:2++=1/16"),
    ("3+:3++:2+:2++:1+:1++:7:7+=1/16",),
    ("6:6+:7:7+:1+:1++:2+:2++",),

    # 101
    ("7:7+:5:5+:1+:1++:2+:2++=1/16",),
    ("3+:3++=1/16", "0=1/8", "1+:1++:2+:2++=1/16"),
    ("3+:3++:2+:2++:1+:1++:7:7+=1/16",),
    ("6:6+:2+:1++:7:7+:5:5+",),

    # 105
    ("1++,1+=1/4", ),
 	("{'COPY_STOP':0}",),

    ("1++,1+=1/4", "3++:3+=3/16", "3++=1/16",),
    ("3++,1++,5+,3+=2/4",),
    ("3++,1++,5+,3+=2/4",),

    # 109
    ("4++:3++:2++:3++:4++:3++:2++:3++=1/16",),
    ("4++,1++,6+:=2/4", ),
    ("4++=1/64", "3++,1++,5+=3/64", "4++=1/64", "3++,1++,5+=3/64", "4++=1/64", "3++,1++,5+=3/64", "4++=1/64", "3++,1++,5+=3/64",),
    ("2++,7+,5+=3/8", "5++=1/8"),

    # 113
    ("3++,1++,5+,3+=2/4",),
    ("3++,1++,5+,3+=2/4",),
    ("4++:3++:2++:3++:4++:3++:2++:3++=1/16",),
    ("4++,1++,6+:=2/4", ),

    # 117
    ("4++=1/64", "3++,1++,5+=31/64"),
    ("4++=1/64", "2++,7+,5+=3/64", "4++=1/64", "2++,7+,5+=3/64", "4++=1/64", "2++,7+,5+=3/64","4++=1/64", "2++,7+,5+=3/64"),
    ("1++=1/4", "5+:1++=1/64", "2++=11/64", "3++=1/16"),
    ("5+:1++=1/64", "3++=31/64"),

    # 121
    ("5+:1++=1/64", "3++=31/64"),
    ("4++:3++:2++:3++:4++:3++:2++:3++=1/16", ),
    ("4++=1/2",),
    ("4++=1/64", "3++=3/64","4++=1/64", "3++=3/64","4++=1/64", "3++=3/64","4++=1/64", "3++=3/64"),

    # 125
    ("2++=3/8", "5++=1/8"),
    ("3++,1++,5+,3+=2/4",),
    ("3++,1++,5+,3+=2/4",),
    ("4++:3++:2++:3++:4++:3++:2++:1++=1/16", ),

    # 129
    ("4++,1++,6+=2/4",),
    ("4++=1/64", "3++,1++,5+=31/64"),
    ("3++=1/64", "2++,7+,5+=3/64", "3++=1/64", "2++,7+,5+=3/64", "3++=1/64", "2++,7+,5+=3/64",),
    ("1++,5+,3+,1+=3/8", "3++,3+=1/8"),

    # 133
    ("1++,1+=3/8", "5++,5+=1/8"),
    ("1++,1+=3/8", "3++,3+=1/8"),
    ("1++,1+:3++,3+:1++,1+:5++,5+=1/8",),
    ("1++,1+=1/4", "1++,5+,3+,1+=2/4", "0=1/4"),



)

music_table_left = \
(
 	("0", "-", "-", "-"),
 	("{'COPY_START':0}",),
 	("0:0=1/4",),
 	("6-:3,1:3,1:3,1=1/8",),
 	("6-:3,1:3,1:3,1=1/8",),
 	("6-:3,1:3,1:3,1=1/8",),

 	("6-:3,1:3,1:3,1=1/8",),
 	("3-:3,7-:3,7-:3,7-=1/8",),
 	("3-:3,7-:3,7-:3,7-=1/8",),
 	("3-:3,7-:7-:7-=1/8",),

 	# 9
 	("3-=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),
 	("0=1/4",),
 	("1-:1:3-:3=1/8",),
 	("5-:0=1/4",),

 	# 13
 	("1-:1:3-:3=1/8",),
 	("5-:0=1/4",),
 	("6--:6-:1-:1=1/8",),
 	("3-:0=1/4",),

 	# 17
 	("6--:6-:1-:1=1/8",),
 	("3-:0=1/4",),
 	("6-:3,1:3,1:3,1=1/8",),
 	("6-:3,1:3,1:3,1=1/8",),

 	# 21
 	("6-:3,1:3,1:3,1=1/8",),
 	("4-:2#,6-:2,6-:2,6-=1/8",),
 	("3-:3,6-:2-:7-,4-=1/8",),
 	("1-:6-,3-:2-:7-,4-=1/8",),

 	# 25
 	("6-,3-:6-,3-:5-#,3-:5-#,3-=1/8",),
 	("6-,6---=1/4",),

 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

 	("0=1/4",),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 29
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("6--:1-=1/64", "4-=7/64", "4-=1/8", "6--:1-=1/64", "4-=7/64", "4-=1/8"),
 	("5-:5-=1/64", "5-=7/64", "5-:5-:5-=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 33
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("6--:1-=1/64", "4-=7/64", "4-=1/8", "7--:2-=1/64", "5-=7/64", "5-=1/8"),
 	("1-=1/4",),
 	
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

 	("0=1/4",),

 	# 37
 	("6-:3,1:3,1:3,1=1/8",),
 	("7-:3,2:3,2:3,2=1/8",),
 	("6-:3,1:3,1:3,1=1/8",),
 	("5-#:3,7-:3,7-:3,7-=1/8",),

 	# 41
 	("6-:3,1:3,1:3,1=1/8",),
 	("7-:5,3:5,3:5,3=1/8",),
 	("7-:6,4#:6,4#:6,4#=1/8",),
 	("5,3=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

 	# 45
 	("0=1/4",),
 	("1:5,3:5,3:5,3=1/8",),
 	("2:5,4:5,4:5,4=1/8",),
 	("1:5,3:5,3:5,3=1/8",),

 	# 49
 	("5-:4,7-:4,7-:4,7-=1/8",),
 	("1:5,3:5,3:5,3=1/8",),
 	("2:5,4:7-:5,4=1/8",),
 	("1:6-:4-:5-=1/8",),

 	# 53
 	("1-:1=1/8", "0=1/4"),
 	("6-:3,1:3,1:3,1=1/8",),
 	("7-:3,2:3,2:3,2=1/8",),
 	("6-:3,1:3,1:3,1=1/8",),

 	# 57
 	("3-:3,7-:3,7-:3,7-=1/8",),
 	("2-:2,6-:2,6-:2,6-=1/8",),
 	("2-:2,7-:2,7-:2,7-=1/8",),
 	("3-:1,6-:3-:1,6-=1/8",),

 	# 61
 	("6-=1/4",),
 	
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

 	("0=1/4",),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 65
 	("6--:1-=1/64", "4-=7/64", "4-=1/8","6--:1-=1/64", "4-=7/64", "4-=1/8"),
 	("5-:5-=1/64", "5-=7/64", "5-:5-:5-=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 69
 	("6--:1-=1/64", "4-=7/64", "4-=1/8","7--:2-=1/64", "5-=7/64", "5-=1/8"),
 	("1-=1/4",),
 	
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

 	("7:6:5#:6=1/16",),
 	("1+:0=1/8", "2+:1+:7:1+=1/16"),

 	# 73
 	("6-:3,1:3,1:3,1=1/8",),
 	("6-:3,1:6-:3,1=1/8",),
 	("6-:3,1:3,1:3,1=1/8",),
  	("3-:3,7-:3,7-:3,7-=1/8",),

  	# 77
  	("3-:3,7-:3,7-:3,7-=1/8",),
  	("3-:3,7-:7-:7-=1/8",),
  	("3-=1/4",),
 	
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

  	("0=1/4",),

  	# 81
  	("1-:1:3-:3=1/8",),
  	("5-:0:=1/4",),
  	("1-:1:3-:3=1/8",),
  	("5-:0:=1/4",),

  	# 85
  	("6--:6-:1-:1=1/8",),
  	("3-:0=1/4",),
  	("6--:6-:1-:1=1/8",),
  	("3-:0=1/4",),

  	# 89
  	("6-:3,1:3,1:3,1=1/8",),
  	("6-:3,1:3,1:3,1=1/8",),
  	("6-:3,1:3,1:3,1=1/8",),
  	("4-:2#,6-:2#,6-:2#,6-=1/8",),

  	# 93
  	("3-:3,6-:2-:7-,4-=1/8",),
  	("1-:6-,3-:2-:7-,4-=1/8",),
  	("6-,3-:6-,3-:5-#,3-:5-#,3-",),
  	("6-,6--=1/4",),
 	("{'COPY_STOP':0}",),
 	("{'COPY_START':0}",),

  	# 97
  	("0=1/4",),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("6--:1-=1/64", "4-=7/64", "4-=1/8","6--:1-=1/64", "4-=7/64", "4-=1/8"),

 	# 101
 	("7--:2-=1/64", "5-=7/64", "5-:5-:5-=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("6--:1-=1/64", "4-=7/64", "4-=1/8","7--:2-=1/64", "5-=7/64", "5-=1/8"),

 	# 105
 	("1++,1+=1/4",),
 	("{'COPY_STOP':0}",),

 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 109
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("6--:1-=1/64", "4-=7/64", "4-:4-:4-=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("7--:2-=1/64", "5-=7/64", "5-:5-:5-=1/8"),

 	# 113
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("6--:1-=1/64", "4-=7/64", "4-:4-:4-=1/8"),

	# 117
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("7--:2-=1/64", "5-=7/64", "5-:5-:5-=1/8"),
    ("1:5:3:5:1:5:3:5=1/16",),
    ("1:5:3:5:1:5:3:5=1/16",),

    # 121
    ("1:5:3:5:1:5:3:5=1/16",),
    ("1:5:3:5:1:5:3:5=1/16",),
    ("1:6:4:6:1:6:4:6=1/16",),
    ("1:5:3:5:1:5:3:5=1/16",),

    # 125
    ("5-:5:2:5:5-:5:2:5=1/16",),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 129
 	("6--:1-=1/64", "4-=7/64", "4-:4-:4-=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("7--:2-=1/64", "5-=7/64", "5-:5-:5-=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),

 	# 133
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1=1/8","3-:5-=1/64", "1=7/64", "1=1/8"),
 	("3-:5-=1/64", "1=7/64", "1:1:1=1/8"),
 	("1-=1/4", "1,5-,3-,1-=2/4", "0=1/4"),
)
import sys
sys.path.append('C:\\work\\automatic_gita\\music\\python\\piano')

import music_translate2 as music_translate
music_parse = music_translate.music_trans([music_table, music_table_left], beat = 120, move=0)
music_parse.music_to_play_table()
music_parse.play_music()

