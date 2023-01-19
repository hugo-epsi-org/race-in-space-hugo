from track import Track
from pilot import Pilot
from garage import Garage
from spaceship import Spaceship, Fighter, Cruiser

track1 = Track(2000)
pilot1 = Pilot("pilot1", 100)
pilot2 = Pilot("pilot2", 50)
spaceship1 = Cruiser("space1", 3)
spaceship2 = Fighter("space2", 5)
spaceship1.add_pilot(pilot1)
spaceship2.add_pilot(pilot2)
track1.add_spaceship(spaceship1)
track1.add_spaceship(spaceship2)

track1.start_race()
track1.who_wins()