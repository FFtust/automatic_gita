import chord

class music_score():
    def __init__(self):
        self.version = "V0.1"
        self.tab = "3/4"
        self.base_level = "C"

    def load(self, m_s):
        if "base_level" in m_s:
            self.base_level = m_s["base_level"]

        if "tab" in m_s:
            self.base_level = m_s["tab"]

    def start(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass
