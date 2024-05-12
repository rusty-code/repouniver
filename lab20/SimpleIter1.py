# Написать класс-итератор
# На вход подаётся коллекция занчений произвольного типа
# Позволяет просматривать колекцию в обратном порядке


class Iterator:
    """Iterator-interface"""

    def __init__(self, lst) -> None:
        self.collection = lst
        self.current = len(lst) - 1

    def to_end(self): # set current to collection end
        self.current = 0

    def to_start(self): # set current to begin collection 
        self.current = len(self.collection) - 1

    def to_current(self, carrete): # user set current
        if carrete >= (len(self.collection)) or carrete < 0:
            print("(ERROR) carrete out of range")
        else:
            self.current = carrete
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= 0:
            result = self.collection[self.current]
            self.current -= 1 # move to next

            return result
        raise StopIteration
    


def main():
    collection = ["a", 2, 4, "arae", 11, 1]
    for it in Iterator(collection):
        print(it)


if __name__ == "__main__":
    main()