class Garage():
    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size
        self.spaceships = []
        
    def add_spaceship(self, spaceship):
        if len(self.spaceships) < self.max_size:
            self.spaceships.append(spaceship)
        else:
            print("Le garage est déjà plein!")

    def search(self, looking_for):
        results = []
        for ship in self.spaceships:
            if ship == looking_for:
                results.append(ship)
        return results