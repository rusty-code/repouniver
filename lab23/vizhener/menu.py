# Создать программу для де/шифрования
# последовательности символов шифром Виженера


import os
from source.vizhener import vizh

def main():

    print("CHOOSE THE ACTION:\n"+
          "   c - code\n"+
          "   e - encode\n"+
          "   x - exit prog"
        )
    act = input("(ENTER): ")
    
    while (act != 'c' and act != 'e' and act != 'x'): # valid input 
        os.system('clear')
        print("(ERROR) incorrect action\n"+
              "CHOOSE THE ACTION:\n"+
              "   c - code\n"+
              "   e - encode\n"+
              "   x - exit prog"
        )
        act = input("(ENTER): ")

    vizh(act)
    # os.system('clear')
    print("Exit..")

if __name__ == "__main__":
    main()