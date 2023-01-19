from pilot import Pilot

class Spaceship():
    def __init__(self, name ='', speed = 0, color = 'white', length = 5, width = 2, brand = ''):
        self.name = name
        self.speed = speed
        self.color = color
        self.length = length
        self.width = width
        self.brand = brand

    def __repr__(self):
        return f'{self.name}: speed = {self.speed}'

    def add_pilot(self, pilot):
        self.pilot = pilot
        pilot.assign_ship()

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed * self.pilot.get_level() / 100

    def get_color(self):
        return self.color

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_brand(self):
        return self.brand

    def __eq__(self, other):
        if self.speed == other.speed:
            return True
        if self.color == other.color:
            return True
        if self.length == other.length:
            return True
        if self.width == other.width:
            return True
        if self.brand == other.brand:
            return True
        return False

class Fighter(Spaceship):
    def __init__(self, name = '' , speed = 0, color = 'white', length = 5, width = 2, brand = ''):
        super().__init__(name, speed * 1.05, color, length, width, brand)

class Cruiser(Spaceship):
    def __init__(self, name = '' , speed = 0, color = 'white', length = 5, width = 2, brand = ''):
        super().__init__(name, speed * 0.95, color, length, width, brand)