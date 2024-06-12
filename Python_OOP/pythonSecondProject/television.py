class Television:
    def __init__(self):
        self.on_off = False
        self.channel = 1

    def check_on_off(self):
        return self.on_off

    def turn_on(self):
        self.on_off = True

    def turn_off(self):
        self.on_off = False

    def current_channel(self):
        return self.channel

    def next_channel(self):
        self.channel += 1

    def to_channel(self, channel_number):
        self.channel = channel_number

    def previous_channel(self):
        self.channel -= 1
