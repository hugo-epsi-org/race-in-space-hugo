class SpaceShip():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed  

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed


class Track():
    def __init__(self, length):
        self.length = length
        self.racers = []

    def AddSpaceShip(self, racer):
        self.racer = racer
        self.racers.append(racer)

    def StartRace(self, racers):
        print(self.racers)
        fastest = 0
        for i in racers:
            if racers[i].get_speed() > fastest:
                fastest = racers[i].get_name()
        return fastest


track1 = Track(2000)
spaceship1 = SpaceShip("space1", 5)
spaceship2 = SpaceShip("space2", 6)
spaceship3 = SpaceShip("space3", 3)
spaceship4 = SpaceShip("space4", 8)
spaceship5 = SpaceShip("space5", 2)

track1.AddSpaceShip(spaceship2)