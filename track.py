class Track():
    def __init__(self, length):
        self.length = length
        self.racers = []

    def add_spaceship(self, racer):
        self.racers.append(racer)

    def start_race(self):
        fastest = sorted(self.racers, key=lambda racer: racer.get_speed(), reverse=True)[0]
        self.winner_stats = {"name": fastest.get_name(),
                             "time": round(self.length/fastest.get_speed(), 2)}

    def who_wins(self):
        return print(f"{self.winner_stats['name']} l'emporte avec un temps de {self.winner_stats['time']}")