# В текстовом файле дано арифметическое выражение в
# обратной польсой записи. Построить дерево этого выражения
# + -> -1
# - -> -2
# * -> -3 

from source.PARSER import parser

def vinput(txt : str):
    def valid(inpt : str):
        for it in inpt:
            if not it in '+-*1234567890':
                return False
        return True

    flag = True
    tmp = None
    while (flag):
        tmp = input(txt)
        if not valid(tmp):
            print("(WARRNING) incorrect data. Retry")
        else:
            flag = False
                
    return tmp

def main():
    # a + b * c -> bc*a+
    # (a + b) * c -> ab+c*
    # (1+2)*3 = 9
    print(parser(vinput("(ENTER): ")))



if __name__ == "__main__":
    main()