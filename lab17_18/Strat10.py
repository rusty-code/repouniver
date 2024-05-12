import simple_term_menu as stm
from structureofdata import classDoublyLinkedList as soddl
from random import randint

def rsum(nums):
    return round(sum(nums), 5)

def get_index_maxnum(nums : list):
    mx = 0
    for it in range(0, len(nums)):
        if nums[mx] < nums[it]:
            mx = it
    return mx

def balance_sequence(nums : list) -> list:
    sm = rsum(nums)
    if sm < 1.0:
        pos = randint(0, len(nums)-1)
        nums[pos] += 1-sm
        nums[pos] = round(nums[pos], 5)
    elif sm > 1.0:
        diff = round(rsum(nums) - 1, 5)
        # print("Diff1: ", diff) # Debug
        maxnum_index = get_index_maxnum(nums)
        diff = abs(round(diff - nums[maxnum_index], 5))
        # print("Diff2: ", diff) # Debug

        if diff == 0.0:
            diff = 1.0
        if nums[maxnum_index] == diff: # block an infinity loop 
            nums[maxnum_index] = round(nums[maxnum_index] - min(nums), 5)
        else:
            if diff < nums[maxnum_index]:
                nums[maxnum_index] = round(nums[maxnum_index] - diff, 5)
            else:
                nums[maxnum_index] = round(1.5*nums[maxnum_index] - diff, 5)

        return balance_sequence(nums)
    
    # correct trash and balance
    flag = True
    for it in range(0, len(nums)):
        if nums[it] <= 0:
            nums[it] = round(1/randint(1, 100), 5)
            flag = False
    if flag:
        return nums
    return balance_sequence(nums)    

class GameField:

    """Decription:
            Gamefild is seqeunce of 11 numbers
                0<number<1
            Two Payers:
                1. Arrays the numbers (only first move)
                2. Multiplies the numbers
            The second player wins if he gets more than 0.025"""
    
    def __init__(self):
        self._game_field = soddl.DoublyLinkedList()

        # generate seq
        numbers = list
        for it in balance_sequence([round(1/randint(1, 100), 5) for it in range(0, 11)]):
            numbers.insert(it)


        # positionary elemets
        for it in range(0, len(numbers)):
            print(f"Выберите {it} элемент:")
            for it1 in range(0, len(numbers)):
                print(f"    №{it1} :: {numbers[it1]}")
            print("Введите № элем.: ")
            self._game_field.insert()

    def aciton(self):
        posns = self.print_menu()

        # multiply of choosen numbers
        mltp = round(self._game_field.get_node(posns[0]).get_data() * \
                     self._game_field.get_node(posns[1]).get_data(), 5)
        
        self._game_field.get_node(posns[0]).update_data(mltp)
        self._game_field.remove(posns[1])

    def get_field(self) -> list: # return list of elemets
        fld = list()
        for it in range(0, self._game_field.get_size()):
            fld.append(self._game_field.get_node(it).get_data())
        return fld


    def print_menu(self) -> list: # entries - gamefield units
        gamefield = self.get_field()

        print("Дано числовое поле. За один ход игрок выбирает два числа из него и перемножает.\n",
              "Необходимо набрать в произвленение больше 0.025\n",
              "Если ходов не остаётся, то объявлеятся поражение.")

        # create list entries
        entries = list()
        for it in range(0, len(gamefield)):
            entries.append(f"Позиция {it} : элемент {gamefield[it]}")

        menu = stm.TerminalMenu(entries, title="Выберите элемент игрового поля:")
        menu.show()

        choose = [
                float(menu.chosen_menu_entry.split(' ')[-1]), # element
                int(menu.chosen_menu_entry.split(' ')[1])   # pos of element
            ]
        
        # if choose ends
        if choose[1] <= 0:
            menu = stm.TerminalMenu(
            [
                f"Позиция {choose[1]+1} : элемент {self._game_field.get_node(choose[1]+1).get_data()}"
            ],
            title="Выберите соседний элемент:"
        )
        elif choose[1] >= self._game_field.get_size()-1:
            menu = stm.TerminalMenu(
            [
                f"Позиция {choose[1]-1} : элемент {self._game_field.get_node(choose[1]-1).get_data()}",
            ],
            title="Выберите соседний элемент:"
        )
        else:
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
                float(menu.chosen_menu_entry.split(' ')[1])   # pos of element
            ]
    
    def is_draw(self):
        if self._game_field.get_size() == 1:
            if self._game_field.get_node(0).get_data() <= 0.025:
                return True

        return False

    def is_win(self):
        if self._game_field.get_size() == 1:
            if self._game_field.get_node(0).get_data() >= 0.025:
                return True

        return False
            

def main():
    game = GameField()

    while not game.is_draw():
        # game._game_field.print_list()
        if game.is_win():
            print("YOU WIN")
            return
        game.aciton()

    print("YOU LOSE")

def test():
    # Has been write a function for? balance a sequence of numbers.

    # generate seq
    numbers = []
    for it in range(0, 11):
        numbers.append(round(1/randint(1, 100), 5))
        print(numbers[it])

    print("Sum: ", rsum(numbers))
    for it in balance_sequence(numbers):
        print(it)
    print("Balace: ", rsum(balance_sequence(numbers)))


if __name__ == "__main__":
    main()
    # test()