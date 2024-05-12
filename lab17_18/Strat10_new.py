
from structureofdata import classDoublyLinkedList as soddl
from structureofdata.valid_input import valid_inpt as vinput

import simple_term_menu as stm
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

    def __init__(self) -> None:
        self._game_field = soddl.DoublyLinkedList()

        # generate the sequence
                            # nums.append(balance_sequence([round(1/randint(1, 100), 5)]))
        numbers = []
        for it in range(0, 11):
            numbers.append(round(1/randint(1, 100), 5))
        nums = balance_sequence(numbers)

        _DEBUG = rsum(nums)


        print("Расставление чисел. Сложение происходит слева на право.") 
        print("№№ : число")

        for it in range(0, len(nums)):
            index = self.print_menu(nums)
            n = nums.pop(index)
            self._game_field.insert(data=n)
        
    def get_field(self) -> list: # return list of elemets
        fld = list()
        for it in range(0, self._game_field.get_size()):
            fld.append(self._game_field.get_node(it).get_data())
        return fld

    def print_menu(self, gamefield : None) -> int:

        # default entries
        if gamefield is None: gamefield = self.get_field() # default 

        # create list entries
        entries = []
        for it in range(0, len(gamefield)):
            entries.append(f"{it} : {gamefield[it]}")

        menu = stm.TerminalMenu(entries, title="Выберите № элемнета")
        menu.show()


        return int(menu.chosen_menu_entry.split(' ')[0]) # position elem 

    def action(self):
        mltp = 0.0
        nums = []
        # 1 2 3 4 5 6 7 8 9 10 11
        # iterate for the elements of the list
        node = self._game_field.get_first()
        while node != self._game_field.get_last().get_prev().get_prev():
            mltp = round(node.get_data() * node.get_next().get_data(), 5)

            nums.append(mltp) # save result
            node = node.get_next().get_next() # step trought one
        
        nums.append(self._game_field.get_last().get_data())

        print(*nums)

        return max(nums)

    def check(self, result):
        if result >= 0.025:
            print("ПОБЕДА")
        else:
            print("ПОРАЖЕНИЕ")



def main():
    
    game = GameField()
    game.check(game.action())


def test():
    pass


if __name__ == "__main__":
    main()
    # test