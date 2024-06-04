

if __name__ == "__main__":
    import CLASS_TREE as ct
else:
    import source.CLASS_TREE as ct


class Node:

    def __init__(self, data=None, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def isend(self):
        if self.left is None and self.right is None:
            return True
        return False
    
    def setleft(self, node): 
        self.left = node
    
    def setright(self, node):
        self.right = node

    def setdata(self, data):
        self.data = data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_data(self):
        return self.data
    

class ParserTree(ct.BinaryTree):
    
    # (1+2)*3 = 9 -> 123+*
    # 1+2*3 = 9 -> 231*+
    def __init__(self, data=None):
        self.head = Node(data=data)


    def append(self, left=None, right=None):
        # left and rigth is data
        # self.head must be init Node

        node = self.head
        flag = True
        while (flag):
            if node.isend():
                flag = False
            else:
                node = node.get_left()
        node.setleft(Node(data=left))
        node.setright(Node(data=right))

    def format(self, node : Node):
        if node is None: 
            return ''

        if node.get_left() is None and node.get_right() is None:
            return f'{node.get_data()}'

        if not node.get_left is None and node.get_right() is None:
            return f"({self.format(node.get_left())}){node.get_data()}"

        if not node.get_right() is None and node.get_left() is None:
            return f"{node.get_data()}({self.format(node.get_right())})"
        
        return f"({ self.format(node.get_left())}){node.get_data()}({self.format(node.get_right())})"


def cut(expr : list):
    return [expr[it] for it in range(1, len(expr)-1)]

def redef(term : str):
    if term == "+": return -1
    elif term == "-": return -2
    elif term == "*": return -3
    else: return int(term)

def calculate(node : Node, result=0):

    if node.isend():
        return node.get_data()    

    if node.get_data() == -1:
        return calculate(node.get_left()) + node.get_right().get_data() 
    elif node.get_data() == -2:
        return calculate(node.get_left()) - node.get_right().get_data() 
    elif node.get_data() == -3:
        return calculate(node.get_left()) * node.get_right().get_data() 
    else:
        # print(f"(ERROR) invaid data : {node.get_data()}")
        print("(ERROR) invalid format")
        return None

# ( 1 + 2 - ( 3 * 2 ) ) * 3
# 1. 32*
# 2. 12+
# 3. 1232*+
# 4. 31232*+*



def parser(expr):
    
    # build term tree
    leters = [redef(expr[lit]) for lit in range(0, len(expr)-1)]
    pars = ParserTree(redef(expr[-1]))

    while leters != []:
        pars.append(left=leters[-1], right=leters[0])
        leters = cut(leters)
    print(f"Parser tree : {pars.format(pars.head)}")
    return calculate(pars.head)

    

if __name__ == "__main__":
    # parser('(1+2)*3') # (1+2) * 3 = 9 
    print(parser('123*+')) # 1+2 * 3 = 7
    