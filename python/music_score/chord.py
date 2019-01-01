info_chord_C = ((2, 1), (4, 2), (5, 3))
info_chord_Dm = ((1, 1), (2, 3), (3, 2))
info_chord_Em = ((4, 2), (5, 2))
info_chord_F = ((1, 1), (2, 1), (3, 2), (4, 3), (5, 3), (6, 1))
info_chord_G = ((1, 3), (5, 2), (6, 3))
info_chord_Am = ((2, 1), (3, 2), (4, 2))
info_chord_G7 = ((1, 1), (5, 2), (6, 2))


class chord_def():
	def __init__(self, name, des, info):
		self.name = name
		self.description = des
		self.info = info


guita_string_1 = 1
guita_string_2 = 2
guita_string_3 = 3
guita_string_4 = 4
guita_string_5 = 5
guita_string_6 = 6


C  = chord_def("C", "chrod C", info_chord_C)
Dm = chord_def("Dm", "chrod Dm", info_chord_Dm)
Em = chord_def("Em", "chrod Em", info_chord_Em)
F  = chord_def("F", "chrod F", info_chord_F)
G  = chord_def("G", "chrod G", info_chord_G)
Am = chord_def("Am", "chrod Am", info_chord_Am)
G7 = chord_def("G7", "chrod G7", info_chord_G7)


