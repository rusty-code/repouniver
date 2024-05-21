
# Дан текстовый файл.
# В строках которого записана последовательность R-чисел.
# Построить из этих числе бинарное дерево поиска.
# Вывести корень дерево


import random
from CLASS_TREE import BinaryTree        


# Convert an elements from str to float
def convert_str_to_realnums(lst : list) -> list:
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = float(it)
        except ValueError:
            continue
        tmpLst.append(tmpNum)
    return tmpLst


def main():
    tst = [ 0, 2, 1, 14, 2, 5, 6, 4, 3]
    tree = BinaryTree()
    for it in tst:
        tree.append(it)

   
def test():
    with open("testcases/testcase_TreeWork54.txt") as _f:
        file = _f.readlines()
        # Extract test sequnces from file
        testcases = \
        [convert_str_to_realnums(file[it].split()) for it in range(0, len(file))] # array of the real num`s
        
        k = 1 # num of test case
        for testcase in testcases:
            print(f"Тест {k}:")
            print(f"    {testcase}")
            tree = BinaryTree()
            for node in testcase:
                tree.append(node)
            
            print(f'    HEAD: {tree._head}')
            print(tree.format(tree._head))
            
            k+=1

        
        


if __name__ == "__main__":
    # main()
    test()