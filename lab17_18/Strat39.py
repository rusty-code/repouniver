
import os
import random

import structureofdata.classDoublyLinkedList as soddl
import structureofdata.classNode as cnd
import structureofdata.classQueue as sodq
import simple_term_menu as stm

from random import randint

# class Menu:

#     def __init__(self, entries : soddl.DoublyLinkedList):
#         tmp = list()
        
#         for it in range(0, len(entries)):
#             pass
#         self._menu = stm.TerminalMenu(entries)

class GameField:
    """Description:
        GameField 
            is circle of 24 units = 1
        Two players: 
            1. Player (index = 1)
            2. AI (index = 0)
        Action 
            Take two adjacent numbers and write their sum"""
    

    def __init__(self):
        self._size = 24
        self._win_sum = 4

        # initialize variables
        self._game_field = soddl.DoublyLinkedList()
        self._players_turn = int()

        # set first step
        self._current_player = randint(0, 1)

        # filling the game field
        for place in range(0, self._size):
            self._game_field.insert(1)
        
    def action(self, pl):

        act = []

        if pl == 1:
            print("ВАШ ХОД")
            entries = self.print_menu()
            # pos1 = entries[0]
            # pos2 = entries[1]
            act = [entries[0], entries[1]]

        else:
            # step of machine
            print("ХОД ОППОНЕНТА")

            act = []
            flag = True # if move has been finded

            # script1 - the win step
            it = 0
            while flag and it < self._size:
                act = []
                if self._game_field.get_node(it).get_data() == 3:
                    act.append(it)
                    if self._game_field.get_node(it-1).get_data() == 1:
                        act.append(it-1)
                        flag = False
                    elif self._game_field.get_node(it+1).get_data() == 1:
                        act.append(it-1)
                        flag = False
                it += 1

            if flag:
                it = 0
                while flag and it < self._size:
                    act = []
                    if self._game_field.get_node(it).get_data() == 2:
                        act.append(it)
                        if self._game_field.get_node(it-1).get_data() == 2:
                            act.append(it-1)
                            flag = False
                        elif self._game_field.get_node(it+1).get_data() == 2:
                            act.append(it-1)
                            flag = False
                    it += 1

            # script2 - the break opponent
            if flag:
                it = 0
                while flag and it < self._size:
                    act = []
                    if self._game_field.get_node(it).get_data() == 2 or \
                        self._game_field.get_node(it).get_data() == 3:
                        act.append(it)
                        if self._game_field.get_node(it-1).get_data() > 1:
                            act.append(it-1)
                            flag = False
                        elif self._game_field.get_node(it+1).get_data() > 1:
                            act.append(it-1)
                            flag = False
                    it += 1

            # script0 - default
            if flag:
                pos = randint(0, 23)
                act.append(pos)
                if randint(0, 1) == 1:
                    act.append(pos+1)
                else:
                    act.append(pos-1)
        

        unitsum = self._game_field.get_node(act[0]).get_data() + \
                  self._game_field.get_node(act[1]).get_data()
        minpos = min(act[0], act[1])

        # write the summ 
        self._game_field.get_node(minpos).update_data(unitsum)

        # delete after minpos position
        self._game_field.remove(max(act[0], act[1]))
        self._size -= 1
            
        self._current_player = self.switch_player() # the next player move

    def switch_player(self):
        if self._current_player == 1:
            self._current_player = 0
        else:
            self._current_player = 1
        print(self._current_player)

    def get_field(self) -> list: # return list of elemets
        fld = list()
        for it in range(0, self._size):
            fld.append(self._game_field.get_node(it).get_data())
        return fld

    def print_field(self):
        for unit in self.get_field():
            print(unit, end=' ')
        print()

    def print_menu(self) -> list: # entries - gamefield units
        gamefield = self.get_field()

        print("Дано числовое поле. За один ход игрок выбирает два числа из него и складывает.\n",
              "Побеждает тот, чьё суммирование == 4.\n",
              "Если ходов не остаётся, то объявлеятся ничья.")

        # create list entries
        entries = list()
        for it in range(0, len(gamefield)):
            entries.append(f"Позиция {it} : элемент {gamefield[it]}")

        menu = stm.TerminalMenu(entries, title="Выберите элемент игрового поля:")
        menu.show()

        choose = [
                int(menu.chosen_menu_entry.split(' ')[-1]), # element
                int(menu.chosen_menu_entry.split(' ')[1])   # pos of element
            ]

        menu = stm.TerminalMenu(
            [
                f"Позиция {choose[1]-1} : элемент {self._game_field.get_node(choose[1]-1).get_data()}",
                f"Позиция {choose[1]+1} : элемент {self._game_field.get_node(choose[1]+1).get_data()}"
            ],
            title="Выберите соседний элемент:"
        )
        menu.show()

        return [ 
                choose[1],  
                int(menu.chosen_menu_entry.split(' ')[1])   # pos of element
            ]

    # end-of-game checks
    def is_win(self, pl) -> bool:
        unit = self._game_field.get_first()

        # search for win option
        while unit != self._game_field.get_last():
            if unit.get_data() == self._win_sum:
                if pl == 0:
                    print("YOU WIN")
                else:
                    print("YOU LOSE")
                return True
            unit = unit.get_next()

        return False

    def is_draw(self):
        unit = self._game_field.get_first()

        count_unit = 0
        # if all units > win option
        while unit != self._game_field.get_last():
            if unit.get_data() > 4:
                count_unit += 1
            unit = unit.get_next()
        
        # is drawn game 
        if count_unit == self._size:
            return True
        
        return False


def main():
    game = GameField()

    player = 0
    # start event processing
    while not game.is_draw():
        if game.is_win(player):
            return None
        
        os.system("clear")
        game.print_field()
        print(game._current_player)
        game.action(player)

        if player == 1:
            player = 0
        else:
            player = 1
    print("DRAW")


def test():
    pass


    
if __name__ == "__main__":
    # test()
    main()