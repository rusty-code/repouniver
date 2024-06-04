
if __name__ == "__main__":
    """
        Test mode
    """
    from QUEUE import Queue
    from STACK import Stack
else:
    from source.QUEUE import Queue
    from source.STACK import Stack


class BasicLiteral:
    pass

class Expression:

    def __init__(self, expr : str):
        """
            Operator list:
                ^ : 0
                * : 1
                / : 2
                % : 3
                + : 4
                - : 5
                { : -1
                } : -2
                ( : -3
                ) : -4
                x : -5
        """

        self.liters = []
        self.convert([ lit for lit in expr])

        self.opl = \
        {
            '^' : 0,
            '*' : 1,
            '/' : 1,
            '%' : 1,
            '+' : 2,
            '-' : 2,
            '{' : -1,
            '}' : -2,
            '(' : -3,
            ')' : -4,
            'x' : -5
        }

    
    def __str__(self):
        out = ''
        for wd in self.liters:
            out = out + wd
        return out

    def convert(self, liters : list) -> list:
        if len(liters) < 2:
            print(f'(ERROR) invalid format {liters}')

        self.liters = []

        curr = 0
        while (curr+1 < len(liters)):
            print(f"curr : {curr} -> {liters[curr]}")
            # is num
            if liters[curr] in '0123456789x':
                self.liters.append('{') # {
                if liters[curr] == 'x':
                    self.liters.append('x') # append x   
                    curr += 1 
                else:
                    self.liters.append(liters[curr])
                    if liters[curr+1] in '0123456789':
                        self.liters.append(liters[curr+1])
                        curr += 2
                    else:
                        curr += 1
                self.liters.append('}') # }
            
            elif liters[curr] in '^*/%+-() ': # append check space
                if liters[curr] == '^':
                    self.liters.append('^')

                elif liters[curr] == '*':
                    self.liters.append('*')

                elif liters[curr] == '/':
                    self.liters.append('/')

                elif liters[curr] == '%':
                    self.liters.append('%')

                elif liters[curr] == '+':
                    self.liters.append('+')

                elif liters[curr] == '-':
                    self.liters.append('-')

                elif liters[curr] == '(':
                    self.liters.append('(')

                elif liters[curr] == ')':
                    self.liters.append(')')
                    
                curr+=1

        # check control different
        if len(liters) - curr == 1:
            self.liters.append('{')
            self.liters.append(liters[curr])
            self.liters.append('}')

    def _extract_number(self, ind : int): # for to_prefix
        buff = []
        print(self.liters)
        while self.liters[ind] != "}":
            buff.append(self.liters[ind])
            ind += 1
        buff.append(self.liters[ind])

        return buff
        
    def to_prefix(self):
        buffer = []

        stack = Stack
        queue = Queue

        lit = 0
        while lit < len(self.liters):
            if self.liters[lit] == '{': # append number
                for litera in self._extract_number(lit):
                    queue.push(data=self.liters[lit])
            elif self.liters[lit] == ')':
                

    def expr_liters(self):
        return self.liters

def convert(liters):
    """
        Convert math expression from infix to boberkurva postfix forms
    """
    # search max priority operand 
    left = 0
    while liters[left] != '(':
        left+=1
    
    right = -1
    while liters[right] != ')':
        right-=1
    
    right = len(liters) + right # negative to positive

    print(*liters[left+1:right])

    

def test(expr : str):   
    print("------")
    liters = [lit for lit in expr]
    print(*liters)
    convert(liters)

def test1(expr : str):
    print(expr)
    print(*Expression(expr).expr_liters())

def test2(expr):
    print(Expression(expr)._extract_number(ind=5))

if __name__ == "__main__":
    # test('(1+2-(3*2))*3')
    # test('1+(2-3)*2*3')
    test1('12+((2-4^2)-12/2)+14*x-2/x+x%3+x%2')
    # test1('12+(11-4)*3')
    # test2('12+1')