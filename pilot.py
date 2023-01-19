class Pilot():
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.has_ship = False

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def assign_ship(self):
        self.assign_ship = True