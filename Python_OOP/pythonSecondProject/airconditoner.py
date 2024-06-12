class AirCondition:
    def __init__(self):
        self.is_on = False
        self.temperature = 20

    def check_on_or_off(self):
        return self.is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def check_temperature(self):
        return self.temperature

    def increase_temperature(self):
        if self.temperature < 30:
            self.temperature += 1

    def decrease_temperature(self):
        if self.temperature > 16:
            self.temperature -= 1
