from battleship.Panel import Panel


class GameBoard(object):
    def __init__(self):
        self.panels = []

    def init_panels(self):
        for i in range(10):
            for j in range(10):
                self.panels.append(Panel(i, j))


class FiringBoard(GameBoard):
    def __init__(self):
        super(FiringBoard, self).__init__()

    def get_open_random_panels(self):
        pass

    def get_hit_neighbours(self):
        pass

    def get_neighbours(self, coordinates):
        pass
