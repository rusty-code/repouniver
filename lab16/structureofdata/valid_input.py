
invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  DataType = 'float'): # Verefed input
    while True:
        try:

            # tmp = input(txt)
            return DataType(input(txt))
            # if data_type == 'int':
            #     return int(tmp)
            # elif data_type == 'float':
            #     return float(tmp)
            # else:
            #     return str(tmp)
        except ValueError:
            print(invalid_txt)

DEBUG = False
def debug_print(txt):
    global DEBUG
    if (DEBUG):
        print(f"(DEBUG) {txt}")
