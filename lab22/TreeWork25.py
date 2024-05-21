# Дан файл тестовых случаев testcase_TreeWork25.txt.
# В каждой строке записана последовательность R-чисел
# Собрать из каждой последовательности бинарное дерево поиска

# Сформировать структурное описание дерева по шаблону:
#
#   (левый дочерний узел)родительский узел(правый дочерний узел)

from CLASS_TREE import BinaryTree

# Convert an elements from str to float
def convert_str_to_realnums(lst : list) -> list:
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = int(it)
        except ValueError:
            continue
        tmpLst.append(tmpNum)
    return tmpLst


def main():

    with open("testcases/testcase_TreeWork54.txt") as _f:
        file = _f.readlines()

        # Extract test sequnces from file
        testcases = \
        [
            convert_str_to_realnums(file[it].split()) for it in range(0, len(file))
        ]
        
        k = 1 # num of test case

        for testcase in testcases:
            print(f"Тест {k}:")
            print(f"    {testcase}")
            tree = BinaryTree()
            for node in testcase:
                tree.append(node)
            
            print(tree.format(tree._head))
                
            k+=1


def test():
    tree = BinaryTree()
    for n in [4, 1, 2, 3, 5, 10]:
        tree.append(n)
    
    print(tree.format(node=tree._head))

if __name__ == "__main__":
    # test()
    main()