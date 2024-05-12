# На вход подаётся строка  c данными клиента
# В первной строке числа N
# А дальше в каждой N-строке
# <customerID><year><mouth><duration of classes>

# (каждый класс определяет конструктор)

DEBUG = False
invalid_txt = "Ошибка ввода... Некорретные данные"
def debugLogs(txt : str):
    if DEBUG:
        print(f"(DEBUG) {txt}")

def extract_info(info_client : str):
    buffer = []
    
    if ( 9<=len(info_client) <= 10 ):
        # 10 2011 01 4
        buffer.append(info_client[0:2]) # extract id
        buffer.append(info_client[2:6]) # extract year
        buffer.append(info_client[6:8]) # extract mounth

        # extract classes 
        if ( len(info_client) == 10 ): # if classes hours > 9
            buffer.append(info_client[8]+info_client[9])
        elif ( len(info_client) == 9 ):
            buffer.append(info_client[8])
    else:
        debugLogs("Неверный формат данных. Повторите попытку")

    return buffer

def convert_info(case : list) -> list:
    if (case == []):
        return []
    buffer = []

    # 0 --> 10 <= <customerID> <= 99
    # 1 --> 2000 <= <year> <= 2010
    # 2 --> <mouth> = 2 (like 01, 02, 03, ..., 11, 12)
    # 3 --> 1 <= <duration of classes> <= 30

    # unique convert to int
    try:
        for info in case:
            buffer.append(int(info))
    except ValueError:
        debugLogs(f"error from convert_info --> {info}")
        return []
    
    if (not (10 <= buffer[0] <= 99)):
        debugLogs(f"from 'convert_info' -> not in id range")
        return []
    elif (not (2000 <= buffer[1] <= 2010)): 
        debugLogs(f"from 'convert_info' -> not in year range")
        return []
    elif (not (1 <= buffer[2] <= 12)):            
        debugLogs(f"from 'convert_info' -> not in mounth range")
        return []
    elif (not (1 <= buffer[3] <= 30)):      
        debugLogs(f"from 'convert_info' -> not in hours range")
        return []
    else: 
        return buffer
    

class Client:

    _clientInfo = list

    def __init__(self, info_client : list):
        self._clientInfo = info_client

    def get_clientID(self): return self._clientInfo[0]
    def get_year(self): return self._clientInfo[1]
    def get_mounth(self): return self._clientInfo[2]
    def get_clasess(self): return self._clientInfo[3]


def main():
    with open("testcases/testcase_ExamTaskC1.txt") as file:
        
        testcases = file.readlines()
        clients = []

        for testcase in testcases:
            contain = convert_info(extract_info(testcase))

            debugLogs(f"testcase {testcase}")
            debugLogs(f"contain {contain}")

            if ( not(contain == []) ): # valid to void 
                clients.append(Client(contain))
            elif (contain == []): # is void 
                debugLogs("from 'main' -> var 'contain' is void")

        if (clients == []): # valid to void
            debugLogs("from 'main' -> var 'clients' is void")
        elif (not(clients == [])):    
            debugLogs(f"from 'main' -> array of 'clients' {clients[0]}")
            # search min classes
            client = clients[0]
            for customer in clients:
                if (customer.get_clasess() <= client.get_clasess()):
                    client = customer

            # output about client
            print(f"Информация о клиенте: {client.get_clientID()}")
            print(f"    1. Продолжительность: {client.get_clasess()}")
            print(f"    2. Год: {client.get_year()}")
            print(f"    3. Месяц: {client.get_mounth()}")


if __name__ == "__main__":
    main()