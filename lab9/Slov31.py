# Дана база багажей пассажирова. Она имеет 3 поля: фамилия пассажира, кол-во вещей и общий вес
#   а) Найти пассажира, средний вес багажа которого отличается не более чем на m кг от среднего веса вещей всех пассажиров
#   б) Найти число пассажирова, имеющих более 2х вещей
#   в) Найти число пассажиров, кол-во вещей которых превосходит среднее кол-во вещей на одного пассажира
#   г) Найти пассажира, имеющего одну вещь весом менее m кг

import random


DEBUG = False
def INFO_LOG(s : str, end_str = ' '):
    if DEBUG:
        print(f"#DEBUG: ({s})", end=end_str)
    return DEBUG

round_p = 3

PASSAGERS = \
{ # V is passangerID
    1 :\
    {
        "фамилия" : "Батраков",
        "кол-во" : 0,
        "вес" : 0
    },
    2 :\
    {
        "фамилия" : "Крючков",
        "кол-во" : 0,
        "вес" : 0
    },
    3 :\
    {
        "фамилия" : "Тактов",
        "кол-во" : 0,
        "вес" : 0
    },
    4 :\
    {
        "фамилия" : "Легков",
        "кол-во" : 0,
        "вес" : 0
    },
    5 :\
    {
        "фамилия" : "Шатунов",
        "кол-во" : 0,
        "вес" : 0
    },
    6 :\
    {
        "фамилия" : "Полынин",
        "кол-во" : 0,
        "вес" : 0
    },
    7 :\
    {
        "фамилия" : "Карамзина",
        "кол-во" : 0,
        "вес" : 0
    },
    8 :\
    {
        "фамилия" : "Петрова",
        "кол-во" : 0,
        "вес" : 0
    },
    9 :\
    {
        "фамилия" : "Фаеева",
        "кол-во" : 0,
        "вес" : 0
    },
    10 :\
    {
        "фамилия" : "Рыжкова",
        "кол-во" : 0,
        "вес" : 0
    },
}


invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Validation the user input 
    while True:
        try:
            tmp = float(input(txt))
            if tmp > 0:
                return tmp
            else:
                print(invalid_txt)
        except ValueError:
            print(invalid_txt)

# output full data about passenger 
def about_passenger(id : int):
    print(f"ПассажирID : {id}")
    print(f"    1. Фамилия: {PASSAGERS.get(id).get('фамилия')}")
    print(f"    2. Кол-во вещей в багаже: {PASSAGERS.get(id).get('кол-во')}")
    print(f"    3. Вес багажа: {PASSAGERS.get(id).get('вес')}")

# if passangers wasn`t searched
isnt_void = False
def no_passengers():
    global isnt_void
    if isnt_void == False:
        print("По заданному критерию пассажиров не найдено...")
    isnt_void = False


# filling db
for passengerID in PASSAGERS.keys():
    PASSAGERS[passengerID]["вес"] = round(random.uniform(0.001, 20.0), round_p)
    PASSAGERS[passengerID]["кол-во"] = random.randint(1, 20)

# for tests
PASSAGERS[1]["кол-во"] = 1
PASSAGERS[1]["вес"] = 0.1

# output db
for passengerID in PASSAGERS.keys():
    about_passenger(passengerID)

# search the total weght and number of items
weight_items = 0.0
number_items = 0

for passengerID in PASSAGERS.keys():
    weight_items += PASSAGERS.get(passengerID).get("вес")
    number_items += PASSAGERS.get(passengerID).get("кол-во")
weight_items = round(weight_items, round_p)


average_weight = round(weight_items/number_items, round_p) # computing the average weihgt
number_passengers = len(PASSAGERS)
average_num_items = number_items/number_passengers


print(f"\nКол-во вещей из всех багажей: {number_items}")
print(f"Кол-во пассажиров: {number_passengers}")
print(f"Общий вес всех багажей: {weight_items}")
print(f"Среднее кол-во вещей на пассажира: {average_num_items}")
print(f"Средний вес всех багажей: {average_weight}\n")


# find ansewer for a) punct
m = valid_inpt("Для нахождения пассажира, средний вес багажа которого отличается не более чем на m кг от среднего веса вещей всех пассажиров, введите число 'm'(вещественное положительное число): ")
for passengerID in PASSAGERS.keys():
    different_weights = abs(PASSAGERS.get(passengerID).get("вес") - average_weight)
    if m >= different_weights:
        about_passenger(passengerID)
        isnt_void = True
no_passengers()

# find answer for б) punct
print("\nПассажиры, имеющие в багаже 2 вещи:")
for passengerID in PASSAGERS.keys():
    if PASSAGERS.get(passengerID).get("кол-во") == 2:
        about_passenger(passengerID)
        isnt_void = True
no_passengers()

# find answer for в) punct
print("Пассажиры, имеющие больше вещей, чем среднее кол-во вещей на пассажира:")
for passengerID in PASSAGERS.keys():
    if PASSAGERS.get(passengerID).get("кол-во") > average_num_items:
        about_passenger(passengerID)
        isnt_void = True
no_passengers()

# find answer for г) punct
m = valid_inpt("Для нахождения пассажира имеющего одну вещь весом менее m кг, введите число 'm'(вещественное положительное число): ")
for passengerID in PASSAGERS.keys():
    if PASSAGERS.get(passengerID).get("кол-во") == 1:
        if INFO_LOG("С одной вещью", "\n"): about_passenger(passengerID)
        if PASSAGERS.get(passengerID).get("вес") < m:
            about_passenger(passengerID)
            isnt_void = True
no_passengers()

