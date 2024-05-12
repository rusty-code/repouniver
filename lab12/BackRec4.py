# BSC (Batrakov Source Code) General Public License (GPL)


# В 1ой строке файла - кол-во артефактов, вес. диапазон1<=, <=вес. диапазон2
# Во 2ой строке файла - веса 1го артеф., 2го артеф., ..., Nго артеф.
# В 3ей строке файла - объёмы 1го артеф., 2го артеф., ..., Nго артеф.
#
# Методом "жадного алгоритма" найти подмножество вещей с критериями:
#       1. вес. диапазон1 <= вес всех артефактов <= вес. диапазон2
#       2. общий объём минимален


###################################FUNC`S####################################################################################

def convert_str(lst : list): # convert elem`s lst from str to int
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = float(it)
        except ValueError:
            continue
        tmpLst.append(tmpNum)
    return tmpLst


invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  data_type = 'float'): # Verefed input
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


def outputDB(db : dict, keys = None): # print database
    if keys == None:
        keys = []
        for key in db.keys():
            keys.append(key)
    
    print(f"База данных артефактов")
    for artefactID in keys:
        print(f"    $артефактID-{artefactID}:")
        print(f"    |    1. Масса: {db.get(artefactID).get('weight')}")
        print(f"    |    2. Объём: {db.get(artefactID).get('volume')}")
        print(f"    |    3. Польза: {db.get(artefactID).get('benefit')}")


###################################MAIN####################################################################################

import mergesort

file = open("./lab12/testcases/testcasesBR4/testcase3_BackRec4.txt", 'r') # str data file

data = file.readlines() # read data from file
for it in range(0, len(data)):
    data[it] = convert_str(data[it].split(' ')) # filling storage with data 

artefactDB = dict() # database for da ta (view with structure)

additional_data = list(data.pop(0)) # N, A, B
print(f"Additioanal data: {additional_data}")

for artefactID in range(0, int(additional_data[0])): # filling of artefactDB
    artefactDB.setdefault(artefactID, {
                            "weight" : data[0][artefactID], 
                            "volume" : data[1][artefactID],
                            "benefit" : round(data[0][artefactID]/data[1][artefactID], 5)
                        }
                    )

sorted_db = mergesort.mergesort(artefactDB, 'benefit') # keys of database

print("Отсортированная база по полю 'польза'")
outputDB(artefactDB, sorted_db)

# search subset of artefacts
subset = []
total_weight = 0
total_volume = 0
for artefactID in sorted_db:
    if additional_data[1] <= total_weight <= additional_data[2]:
        break
    elif total_weight <= additional_data[2]:
        total_weight += artefactDB.get(artefactID).get('weight')
        total_volume += artefactDB.get(artefactID).get('volume')
        subset.append(artefactID)
    elif total_weight > additional_data[2]:
        total_weight -= artefactDB.get(artefactID).get('weight')
        total_volume -= artefactDB.get(artefactID).get('volume')
        subset.pop(-1)

# if subset is empty
if not (additional_data[1] <= total_weight <= additional_data[2]):
    print("Невозможно составить искомое подмножество...")
else:
    print(f"\nПодмножество артефактов")
    for ID in subset:
        print(f"    $артефактID-{ID}:")
        print(f"    |    1. Масса: {artefactDB.get(ID).get('weight')}")
        print(f"    |    2. Объём: {artefactDB.get(ID).get('volume')}")
        print(f"    |    3. Польза: {artefactDB.get(ID).get('benefit')}")

    print("Общая масса артефактов: ", total_weight)
    print("Общий объём артефактов: ", total_volume)




