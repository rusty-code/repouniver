# Дана строка S, если S - допустимое имя файла, то вывести True, иначе Flase

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  data_type = ''): # Verefed input
    while True:
        try:

            tmp = input(txt)
            if data_type == 'int':
                return int(tmp)
            elif data_type == 'float':
                return float(tmp)
            else:
                return str(tmp)
        except ValueError:
            print(invalid_txt)


def main(filename : str) -> bool: 

    if (filename.count('.') == 1):
        for char in ['/', ',', '?', '[', ']', '|', '\\', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '"', "'", " "]:
            if (char in filename):
                return False
        return True
    elif (filename.count('.') != 1):
        return False
    
    return None


if __name__ == "__main__":
    with open("testcases/testcase_File1.txt", 'r') as file:
        testlist = file.readlines()
        testlist.append(
            valid_inpt("Введите имя файла\n(разрешёные символы: Аа-ЯяAa-Zz0-9_-)\n(шаблон: имя_файла.расширение)\nВвод> ", "str") + '\n' 
        )
        num = 1
        for test_case in testlist:
            print(f"Тест {num}: {test_case}> ", main(test_case), end='\n')
            num += 1