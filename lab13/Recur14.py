# Вывести значение целочисленного выражения заданного строкой.
# Выражение определяется при помощи форм Бэкуса-Наура

# <expression> ::= <number> | <expression> + <number> | <expression> - <number>

type_lexeme = \
{
    "OP_MINUS" : 0,
    "OP_PLUS" : 1,
    "LEFT_BRACKET" : 2,
    "RIGHT_BRACKET" : 3,
    "NUMBER" : 4
}

class Lexeme:
    lex_type : int
    lex_token : str

    def __init__(self, lex_type : int, lex_token : str):
        self.lex_type = lex_type
        self.lex_token = lex_token



def extract_token(expr : str):
    global type_lexeme
    buffer = list
    pos = 0
    while (pos < len(expr)):
        if (expr[pos] == '('): buffer.append(Lexeme(type_lexeme["LEFT_BRACKET"]), '(')
        elif (expr[pos] == ')'): buffer.append(Lexeme(type_lexeme["RIGHT_BRACKET"]), ')')
        elif (expr[pos] == '+'): buffer.append(Lexeme(type_lexeme["OP_PLUS"]), '+')
        elif (expr[pos] == '-'): buffer.append(Lexeme(type_lexeme["OP_MINUS"]), '-')
        elif (expr[pos] in '0123456789'): 
            numb = ''
            while (expr[pos] in "0123456789"):
                numb.join(expr[pos])                
        
        pos += 1



def main(expr : str):
    pass



if __name__ == "__main__":
    main(input("Введите выражение:\n> "))