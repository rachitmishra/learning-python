from battleship import OccupationType
from battleship.Coordinates import Coordinates
from battleship.OccupationType import *


class Panel(object):
    def __init__(self, rows, columns):
        self.coordinates = Coordinates(rows, columns)
        self.occupation_type = OccupationType.EMPTY

    def get_status(self):
        return self.occupation_type

    def is_occupied(self):
        return self.occupation_type == BATTLESHIP or \
               self.occupation_type == SUBMARINE or \
               self.occupation_type == CARRIER or \
               self.occupation_type == CRUISER or \
               self.occupation_type == DESTROYER

    def is_random_available(self):
        return (self.coordinates.row % 2 == 0 and self.coordinates.column % 2 == 0) or \
               self.coordinates.row % 2 == 1 and self.coordinates.row % 2 == 1
