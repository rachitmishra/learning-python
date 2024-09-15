from battleship import OccupationType


class Ship(object):
    def __init__(self):
        self.name = ""
        self.width = None
        self.hits = None
        self.occupation_type = None

    def get_is_sunk(self):
        return self.hits > self.width


class Destroyer(Ship):
    def __init__(self):
        super(Destroyer, self).__init__()
        self.name = "Destroyer"
        self.width = 2
        self.occupation_type = OccupationType.DESTROYER


class Submarine(Ship):
    def __init__(self):
        super(Submarine, self).__init__()
        self.name = "Submarine"
        self.width = 3
        self.occupation_type = OccupationType.SUBMARINE


class Cruiser(Ship):
    def __init__(self):
        super(Cruiser, self).__init__()
        self.name = "Cruiser"
        self.width = 3
        self.occupation_type = OccupationType.CRUISER


class Battleship(Ship):
    def __init__(self):
        super(Battleship, self).__init__()
        self.name = "Battleship"
        self.width = 4
        self.occupation_type = OccupationType.BATTLESHIP


class Carrier(Ship):
    def __init__(self):
        super(Carrier, self).__init__()
        self.name = "Carrier"
        self.width = 5
        self.occupation_type = OccupationType.CARRIER
