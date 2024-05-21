# Во входной стоке дано сообщение
# Посторить код Хаффмана для него символов


class StructNum:
    """Класс для имитации числа рассчётной таблицы"""

    def __init__(self, thisnm=None, prevnm1=None, prevnm2=None):
        self.thisnum = thisnm # data

        # before sum of this num
        self.prevnum1 = prevnm1
        self.prevnum2 = prevnm2

        self.code = ''

    def __lt__(self, right):
        return self.thisnum < right.thisnum

    def __add__(self, right):
        return self.thisnum + right.thisnum

    def __str__(self):
        return f"{self.thisnum}"

    def is_struct(self):
        if self.prevnum1 is None and self.prevnum2 is None:
            return False
        return True

    def get_thisnum(self):
        return self.thisnum

    def update_code(self, code : str):
        self.code = f"{self.code}{code}"

    def update_thisnum(self, num : float):
        self.thisnum = num

    def update_prevnum1(self, prev):
        self.prevnum1 = prev
    
    def update_prevnum2(self, prev):
        self.prevnum2 = prev


class TreeListNums:
    """Класс для имитации рассчётной дерева частот"""

    def __init__(self):
        self._head = list()
        self.frequences = list()

    def calculate(self, freqs : dict):
        tmp = list()
        for it in freqs.keys():
            tmp.append(StructNum(thisnm=freqs[it]))

        self.frequences.append(tmp)
        ### вывод первого поля рассчётной таблицы (раскомметировать для вывода)
        print()
        for it in tmp:
            print(it.get_thisnum())
        print()
        while len(tmp) > 2:

            struct_num = StructNum( \
                thisnm=tmp[0].thisnum + \
                       tmp[1].thisnum, 
                prevnm1=tmp.pop(0),
                prevnm2=tmp.pop(0)
            )

            tmp1 = [struct_num]
            for num in range(0, len(tmp)):
                tmp1.append(tmp[num])

            tmp = tmp1
            self.frequences.append(tmp.sort())
            ### вывод n-ой строки рассчётной таблицы (раскомметировать для вывода)
            print()
            for it in tmp:
                print(it.get_thisnum())
            print()

        self._head = tmp
        self.frequences = list()

        return self
    
    def output(self, nodel : StructNum, noder : StructNum):  
        # вывод дерева и кодами узлов
        print(nodel.thisnum, " : ", nodel.code)
        print(noder.thisnum, " : ", noder.code)
        print()
        if nodel.is_struct():
            self.output(nodel=nodel.prevnum1, noder=nodel.prevnum2)
        if noder.is_struct():
            self.output(nodel=noder.prevnum1, noder=noder.prevnum2)
 
    def get_ends(self, nodel : StructNum, noder : StructNum):
        # сбор конечных узлов дерева 
        if not nodel.is_struct():
            self.frequences.append(nodel)
        else:
            self.get_ends(nodel.prevnum1, nodel.prevnum2)
        
        if not noder.is_struct():
            self.frequences.append(noder)
        else:
            self.get_ends(noder.prevnum1, noder.prevnum2)

        for it in range(0, len(self.frequences)):
            current = it
            for it1 in range(it+1, len(self.frequences)):
                if self.frequences[current] > self.frequences[it1]:
                    current = it1
            tmp = self.frequences[it]
            self.frequences[it] = self.frequences[current]
            self.frequences[current] = tmp


def add_code(num1 : StructNum, num2 : StructNum, current_code = ''):
    if not num1.is_struct():
        num1.update_code(f"{current_code}0")
    else: 
        num1.update_code(f"{current_code}0")
        add_code(num1=num1.prevnum1, num2=num1.prevnum2, current_code=f"{current_code}0")
    
    if not num2.is_struct():
        num2.update_code(f"{current_code}1")
    else: 
        num2.update_code(f"{current_code}1")
        add_code(num1=num2.prevnum1, num2=num2.prevnum2, current_code=f"{current_code}1")
    

def define_words(dc : dict): # вспомогательная ф-ция
    lst = [it for it in dc.keys()]
    return lst[0]


def main():
    # входная строка с текстом 
    # outstr = "ГОСТИНАЯ АННЫ ПАВЛОВНЫ НАЧАЛА ПОНЕМНОГУ НАПОЛНЯТЬСЯ ПРИЕХАЛА ВЫСШАЯ " \
    #          "ЗНАТЬ ПЕТЕРБУРГА ЛЮДИ САМЫЕ РАЗНОРОДНЫЕ ПО ВОЗРАСТАМ И ХАРАКТЕРАМ НО " \
    #          "ОДИНАКОВЫЕ ПО ОБЩЕСТВУ В КАКОМ ВСЕ ЖИЛИ ПРИЕХАЛА ДОЧЬ КНЯЗЯ ВАСИЛИЯ КРАСАВИЦА " \
    #          "ЭЛЕН ЗАЕХАВШАЯ ЗА ОТЦОМ ЧТОБЫ С НИМ ВМЕСТЕ ЕХАТЬ НА ПРАЗДНИК ПОСЛАННИКА ОНА " \
    #          "БЫЛА В ШИФРЕ И БАЛЬНОМ ПЛАТЬЕ ПРИЕХАЛА И МОЛОДАЯ МАЛЕНЬКАЯ КНЯГИНЯ БОЛКОНСКАЯ " \
    #          "ПРОШЛУЮ ЗИМУ ВЫШЕДШАЯ ЗАМУЖ И ТЕПЕРЬ НЕ ВЫЕЗЖАВШАЯ В БОЛЬШОЙ СВЕТ ПО ПРИЧИНЕ " \
    #          "СВОЕЙ БЕРЕМЕННОСТИ НО ЕЗДИВШАЯ ЕЩЕ НА НЕБОЛЬШИЕ ВЕЧЕРА ПРИЕХАЛ КНЯЗЬ ИППОЛИТ " \
    #          "СЫН КНЯЗЯ ВАСИЛИЯ С МОРТЕМАРОМ КОТОРОГО ОН ПРЕДСТАВИЛ ПРИЕХАЛ И АББАТ МОРИО И " \
    #          "МНОГИЕ ДРУГИЕ"

    outstr = "БОБРЫ БОДРЫ И ДОБРЫ"

    words = dict()
    count = 0  # кол-во символов в тексте
    # подсчёт кол-ва сим. и кол-ва отдельных сим.
    for it in outstr:
        if words.get(it) is None:
            words[it] = 1
            count += 1
        else: 
            words[it] += 1
            count += 1
    print("Количество символов в тексте: ", count)

    for key in words.keys():
        print(key, " : ", words[key])

    print()
    print()

    # подсчёт частот отдельных сим.
    for it in words.keys():
        words[it] = [words[it], round(words[it]/count, 18)]

    for key in words.keys():
        print(key, " : ", words[key][1])

    print(len(words.keys())) ### сверка кол-ва уникальных символов
    
    print()
    print()

    # составление первого поля рассчётной таблицы
    frequences = dict()
    for it in range(0, (1+33)*33//2):
        if words == {}:
            break
        min_word = define_words(words)
        for wd in words.keys():
            if words[wd][0] < words[min_word][0]:
                min_word = wd
        frequences[min_word] = words.pop(min_word)[1]

    # print()
    # for key in frequences.keys():
    #     print(key, " : ", frequences[key])

    # words = frequences
    # frequences = list()

    cnt = 1 # вывод симоволов и их частот (раском. для вывода)
    for it in frequences.keys():
        print(cnt, " : ", it , " : ", frequences[it])
        cnt += 1

    print()
    print()

    tree = TreeListNums() # дерево частот
    print("Рассчётная таблица")
    tree.calculate(frequences) # имитация рассчётной таблицы
    add_code(tree._head[0], tree._head[1], '') # присваивание кодов для сиволов
    tree.get_ends(tree._head[0], tree._head[1])

    cnt = 0
    print("№ : символ   :      частота       :    код")
    for it in frequences.keys():
        print(cnt+1, " : ", it, " : ", tree.frequences[cnt].thisnum, " : ", tree.frequences[cnt].code)
        cnt += 1

    # рассчёт избыточности полученного кода
    print()
    summ = 0
    for it in tree.frequences:
        # print(f"{it.thisnum} : {len(it.code)}")
        summ += it.thisnum * len(it.code)
    print("Избыточность (округлено до 5 знаков после запятой): ", round(summ, 5))

    
if __name__ == "__main__":
    main()
