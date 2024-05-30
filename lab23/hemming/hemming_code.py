# В текстовом файле имеется набор сообщений.
# Построить код Хемминга для данного сообщения.

from IOFILESTREEM import File

from HEMMING import process_start    

DEBUG = False

def extract(collection : list):
    global DEBUG

    def filter(instance : str):
        try:
            int(instance[0]) # exlusion provocate

            return instance[0:len(instance)-1] # cut '\n'

        except TypeError:
            if DEBUG: print(f"filter {instance}", end='')
            return None

        except ValueError:
            if DEBUG: print(f"filter {instance}", end='')
            return None

    fltr_collect = []

    for inst in collection:
        fltr_inst = filter(inst)
        if not fltr_inst is None:
            fltr_collect.append(fltr_inst)
    
    return fltr_collect


def main():
    message = File('testcases/testcase_hemming_message.txt')
    print(extract(message.get_buffer())[0])
    print(f"(ИТОГ) ", process_start(extract(message.get_buffer())[0]))



def test():
    file = File('testcases/testcase_hemming_message.txt')
    print(extract(file.get_buffer()))
    print(len(extract(file.get_buffer())[0]))

if __name__ == "__main__":
    main()
    # test()