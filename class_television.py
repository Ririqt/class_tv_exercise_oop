class Television:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on(self):
        self.on = True
