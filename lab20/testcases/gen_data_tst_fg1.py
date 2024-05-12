# Генерация рандомных строк сохранение их в файл

from random import randint

try:
    with open("testcases/tst_fg1.txt", 'w') as file:
        str_count = 5
        alphabet = "zxcvbnmasdfghjklqwertyuiop"\
                    "ZXCVBNMASDFGHJKLQWERTYUIOP"
        for st in range(0, str_count):
            writeble = ''
            for it in range(0, randint(1, 45)): # rand len(str)
                writeble += alphabet[randint(0, len(alphabet)-1)]
            print(writeble)
            file.write(writeble+'\n')
except FileNotFoundError: print("File not found...")
except: print("Runtime error...")
