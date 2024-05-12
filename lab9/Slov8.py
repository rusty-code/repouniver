# На вход строка, на выходе первое слово (в лекс. порядке), которое встечается реже всего

dd = dict()

st = open("testcaseSlov8.txt", 'r').readline() # input("Введите строку слов: ")

# замена знаков препинания на единый символ
tmp = ''
for it in st:
    #print(it)
    if it not in " .,!?-":
        tmp += ''.join(it)
    elif it in " .,!?-":
         tmp += ''.join("*")

# разбиение строки на слово
tmp = tmp.split("*")

st = [] # окончательная очистка ввода от пустых слов 
for it in tmp:
    if it != '':
        st.append(it)

for it in range(len(st)):
    st[it] = str(st[it]).lower()
st.sort()
#print(st)
for it in st: # создание пар ключ : значение
    dd[it] = 0
for it in st: # подсчёт кол-ва встечающихся слов
    dd[it] += 1


mn = min(dd.values()) # меньшее кол-во встреч 
this_wd = '' # певрое редкое слово
for it in dd.keys():
    if dd[it] == mn:
        this_wd = it
        break

for it in dd.keys():
    print(f"Слово \"{it}\" встречается {dd[it]} раз")

print(f"Первое в лексическом порядке слово, которое встречается реже всего: {this_wd}")