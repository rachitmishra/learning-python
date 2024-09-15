from battleship.GameBoard import *
from battleship.Ships import *


class Player(object):
    def __init__(self, name):
        self.name = name
        self.game_board = GameBoard()
        self.firing_board = FiringBoard()
        self.ships = [Destroyer(), Submarine(), Battleship(), Carrier(), Cruiser()]
        self.has_lost = False

    def has_lost(self):
        has_lost = True
        for ship in self.ships:
            has_lost = ship.get_is_sunk()

        return has_lost
