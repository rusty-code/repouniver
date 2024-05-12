
from random import randint


class GameField:

    """Decription:
            Gamefild is 20x5 array
            Two Payers:
                One step is remove NxN elements
            The Player wins if there are no moves left """
    
    def __init__(self, width = 5, lenght = 20):

        self._width = width
        self._lenght = lenght

        self._gamefield = []
        self._players_turn = randint(0, 1)

        for out in range(0, lenght):
            self._gamefield.append('#####')

    def print_field(self):
        for prt in range(0, self._lenght):
            print()



