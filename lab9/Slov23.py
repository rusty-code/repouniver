
# Имеется БД сотрудников и их ДР
#   а) Определить самого молодого сотрудника
#   б) Самого старшего сотрудника
#   в) Получить список сотрудников, родившихся весной

DEBUG = False
def INFO_LOG(s : str, end_str = ' '):
    if DEBUG:
        print(f"#DEBUG: ({s})", end=end_str)
    return DEBUG

EMPLOYEES = \
{
    "Батраков Ярослав" :\
    {
        "дата рождения" :\
        {
            "день": 12,
            "месяц": 3,
            "год" : 2005
        } 
    },
    "Крючков Алксандр" :\
    {
        "дата рождения" :\
        {
            "день": 11,
            "месяц": 6,
            "год" : 2004
        }
    },
    "Тактов Ураз" :\
    {
        "дата рождения" :\
        {
            "день": 3,
            "месяц": 10,
            "год" : 2005
        }
    },
    "Легков Владимир" :\
    {
        "дата рождения" :\
        {
            "день": 24,
            "месяц": 6,
            "год" : 2006
        }
    },
    "Шатунов Виктор" :\
    {
        "дата рождения" :\
        {
            "день": 15,
            "месяц": 2,
            "год" : 2003
        }
    },
    "Полынин Тимур" :\
    {
        "дата рождения" :\
        {
            "день": 19,
            "месяц": 2,
            "год" : 2003
        }
    },
    "Карамзина Анна" :\
    {
        "дата рождения" :\
        {
            "день": 22,
            "месяц": 8,
            "год" : 2003
        }
    },
    "Петрова Арина" :\
    {
        "дата рождения" :\
        {
            "день": 3,
            "месяц": 3,
            "год" : 2005
        }
    },
    "Фаеева Анастасия" :\
    {
        "дата рождения" :\
        {
            "день": 31,
            "месяц": 12,
            "год" : 2007
        }
    },
    "Рыжкова Ярослава" :\
    {
        "дата рождения" :\
        {
            "день": 29,
            "месяц": 5,
            "год" : 2007
        }
    },
}


zoomers = {} # array of the youngest employees
boomers = {} # array of the oldest employees



# accessing to the dict of the dict 
def access_to(name_key : str, day_or_month_or_year : str):
    return EMPLOYEES.get(name_key).get('дата рождения').get(day_or_month_or_year)




# output full data abouot employee
def about_employee(key : str):
    print(f"Имя {key}")
    print(f"    Дата рождения:")
    print(f"        1. День: {access_to(key, 'день')}")
    print(f"        2. Месяц: {access_to(key, 'месяц')}")
    print(f"        3. Год: {access_to(key, 'год')}")


def get_yong_byField(structure : dict(), start_data, field : str):
    var = start_data
    for obj in structure.keys():
        if var < access_to(obj, field):
            var = access_to(obj, field)
    return var


def get_oldest_byField(structure : dict(), start_data, field : str):
    var = start_data
    for obj in structure.keys():
        if var > access_to(obj, field):
            var = access_to(obj, field)
    return var
     
def filling_byField(structure : dict(), field : str, data):
    tmp_db = dict()
    for obj in structure.keys():
        if access_to(obj, field) == data:
            tmp_db.setdefault(obj, structure.get(obj))
    return tmp_db

def get_name(tst):
    ans = ''
    trfl = False
    for wd in tst:
        if wd == "'" and trfl == False:
            trfl = True
        elif wd == "]":
            trfl = False
        if trfl:
            ans += wd
    return ans


# search the yongest and oldest years
yongest_year = get_yong_byField(EMPLOYEES, 0, "год")
oldest_year = get_oldest_byField(EMPLOYEES, access_to("Батраков Ярослав", "год"), "год")

# filtering by year
zoomers = filling_byField(EMPLOYEES, "год", yongest_year)
boomers = filling_byField(EMPLOYEES, "год", oldest_year)

if INFO_LOG("zoomers"): print(zoomers)
if INFO_LOG("boomers"): print(boomers)

# search the yongest and oldest months
yongest_month = get_yong_byField(zoomers, 0, "месяц")
oldest_month = get_oldest_byField(boomers, access_to("Батраков Ярослав", "месяц"), "месяц")

# filtering by month
zoomers = filling_byField(zoomers, "месяц", yongest_month)
boomers = filling_byField(boomers, "месяц", oldest_month)

if INFO_LOG("zoomers"): print(zoomers)
if INFO_LOG("boomers"): print(boomers)

# search the yongest and oldest days
yongest_day = get_yong_byField(zoomers, 0, "день")
#oldest_day = get_yong_byField(boomers, 0, "день")
oldest_day = get_oldest_byField(boomers, access_to("Батраков Ярослав", "день"), "день")

# filtering by day
zoomers = filling_byField(zoomers, "день", yongest_day)
boomers = filling_byField(boomers, "день", oldest_day)

if INFO_LOG("zoomers"): print(zoomers)
if INFO_LOG("boomers"): print(boomers)


print(f"Самый молодой сотрудник компании: {get_name(str(zoomers.keys()))}")
print(f"Самый старший сотрудник компании: {get_name(str(boomers.keys()))}")

print()
print("Список сотрудников, родившихся весной:")
for name in EMPLOYEES.keys():
    if 2 < access_to(name, "месяц") < 6:
        print(name)
