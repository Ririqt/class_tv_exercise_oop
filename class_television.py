# Class TV Exercise
# Creating Class for Television
class Television:
    # Making the Constructor
    def __init__(self):
        # Instance Variable
        self.channel = 1
        self.volume_level = 1
        self.on = False

    # Making Instance Methods for the functions of the Television
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        if self.on and 0 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.on and self.volume_level > 0:
            self.volume_level -= 1
