# Имеется три вида фигур: квадрат, круг, отрезок
# Фигура имеет атрибуты: цвет, размер
# Пользователь создаёт определяемое им кол-во фигур
# Эти фигуры записываются в бинарный файл и выводятся в структурированном виде на экран

# (каждый класс определяет конструктор переопределить метод __str__) 

from pickle import load, dump
import simple_term_menu as stm

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  data_type = 'float'): # Verefed input
    while True:
        try:

            tmp = input(txt)
            if data_type == 'int':
                if (int(tmp) > 0):
                    return int(tmp)
            elif data_type == 'float':
                if (float(tmp) > 0):
                    return float(tmp)
        except ValueError:
            print(invalid_txt)


class GEOMETRY_OBJECT:
    """A basic geometry class"""
    _sets = dict()
    def __init__(self, sets : dict):
        self._sets = sets
    
    def append(self, filed : str, value):
        if ( not (self._sets.get(filed) is None) ):
            self._sets[filed] = value

    def update(self, filed : str, value):
        self._sets[filed] = value

    def getkeys(self):
        return self._sets.keys()
    
    def get(self, field : str):
        if ( field in self._sets.keys() ):
            return self._sets[field]
        return None


class SQUARE(GEOMETRY_OBJECT):
    
    def __init__(self, color : str, size : int):
        super().__init__(
            {
                "color" : color,
                "side" : size
            }
        )

    def __str__(self):
        return f"Фигура: квадрат\n   Цвет: {self._sets['color']}\n   Длина стороны: {self._sets['side']}\n"

class LINE(GEOMETRY_OBJECT):
    
    def __init__(self, color : str, size : float):
        super().__init__(
            {
                "color" : color,
                "length" : size
            }
        )
    
    def __str__(self):
        return f"Фигура: отрезок\n   Цвет: {self._sets['color']}\n   Длина стороны: {self._sets['length']}\n"

class CIRCLE(GEOMETRY_OBJECT):
    
    def __init__(self, color : str, size : int):
        super().__init__(
            {
                "color" : color ,
                "radius" : size
            }
        )

    def __str__(self):
        return f"Фигура: круг\n   Цвет: {self._sets['color']}\n   Длина стороны: {self._sets['radius']}\n"

def input_figure_data():
    terminal_menu = stm.TerminalMenu(
        ["[1] квадрат", 
        "[2] круг",
        "[3] отрезок"],
        title="Выберите геометрическую фигуру для ввода данных"
        )
    terminal_menu.show()
    #  print(terminal_menu.chosen_menu_entry)
    
    if (terminal_menu.chosen_menu_entry == "отрезок"):
        return LINE(input("Введите цвет фигуры: "), valid_inpt("Введите длину отрезка вещественным числом: ", "float"))
    elif (terminal_menu.chosen_menu_entry == "квадрат"):
        return SQUARE(input("Введите цвет фигуры: "), valid_inpt("Введите длину стороны натуральным числом > 0: ", "int"))
    elif (terminal_menu.chosen_menu_entry == "круг"):
        return CIRCLE(input("Введите цвет фигуры: "), valid_inpt("Введите длину радиуса натуральным числом > 0: ", "int"))


def main():
    with open("testcases/Task1", 'wb') as binfile:
        figures = []
        for it in range(0, valid_inpt("Введите кол-во фигур: ", "int")):
            figures.append(input_figure_data())

        for figure in figures:
            dump(figure, binfile)
            print(figure)


if __name__ == "__main__":
    main()