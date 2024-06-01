
def search(liters : list, pos : int):
    pass

# 
def convert(liters):
    """
        Convert math expression from infix to postfix forms
    """
    # search max priority operand 
    left = 0
    while liters[left] != '(':
        left+=1
    
    right = -1
    while liters[right] != ')':
        right-=1
    
    right = len(liters) + right

    print(*liters[left+1:right])

    return 
        
        


def test(expr : str):
    print("------")
    liters = [lit for lit in expr]
    print(*liters)
    convert(liters)


if __name__ == "__main__":
    test('(1+2-(3*2))*3')
    test('1+(2-3)*2*3')