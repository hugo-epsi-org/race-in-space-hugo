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
        self.winner = ""

    def AddSpaceShip(self, racer):
        self.racer = racer
        self.racers.append(racer)

    def StartRace(self):
        fastest = 0
        for i in range(len(self.racers)):
            if self.racers[i].get_speed() > self.racers[fastest].get_speed():
                fastest = i
        self.winner = self.racers[fastest].get_name()

    def WhoWins(self):
        return print(f'{self.winner} l''emporte')


track1 = Track(2000)
spaceship1 = SpaceShip("space1", 5)
spaceship2 = SpaceShip("space2", 6)
spaceship3 = SpaceShip("space3", 3)
spaceship4 = SpaceShip("space4", 1)
spaceship5 = SpaceShip("space5", 2)

track1.AddSpaceShip(spaceship1)
track1.AddSpaceShip(spaceship2)
track1.AddSpaceShip(spaceship3)
track1.AddSpaceShip(spaceship4)
track1.AddSpaceShip(spaceship5)

track1.StartRace()
track1.WhoWins()