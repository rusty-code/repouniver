# Создать ф-цию-генератор
# Параметр ф-ции-генератора -- строка рандомных латинских букв
#   - рандомные латинские буквы могут быть заглавными и строчными
# Возврат ф-ции-генератора -- строка латинсиких букв
#   - латинские буквы только заглавные



def gnrt_func_read_file(path : str, mod : str):
    try:
        with open(path, mod) as file:
            lines = file.readlines() # list of strings

            for lne in lines:
                yield lne[0:len(lne)-1]

    except FileNotFoundError: print("File not found...")
    except: print("Runtime error...")


def gnrt_func_filter_string(string : str):

    for wd in string:
        if wd in "ZXCVBNMASDFGHJKLQWERTYUIOP":
            yield wd


def main():

    num_tst = 0
    for line in gnrt_func_read_file("testcases/tst_fg1.txt", 'r'): # iteration for lines

        print(f"testcase-{num_tst} : {line}")
        print("Words: ", end=' ')

        for wd in gnrt_func_filter_string(line): # iteration for words in string
            print(wd, end=' ')

        num_tst+=1
        print('\n')


def test():
    pass


if __name__ == "__main__":
    # test()
    main()