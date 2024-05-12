# На вход подаётся строка  c данными клиента
# В первной строке число K - id клиента
# Во второй строке целое число N - кол-во клиентов
# А дальше в каждой N-строке:
# <duration><year><month><clientID>
# Отфильтровать данные: год -> max(занятие) -> min(месяц)

# (каждый класс определяет конструктор)

DEBUG = False
invalid_txt = "Ошибка ввода... Некорретные данные"
def debugLogs(txt : str):
    if DEBUG:
        print(f"(DEBUG) {txt}")

def valid_inpt(txt): # Verefed input
    while True:
        try:
            tmp = int(input(txt))
            if (10 <= tmp <= 99):
                return tmp
            else:
                print("Некорректный код клиента... Повторите попытку")
        except ValueError: print(invalid_txt)

def extract_info(info_client : str):
    buffer = []

    if ( 9<=len(info_client) <= 10 ):
        # 4 2011 01 10
        # 15 2010 03 14
        # extract classes 
        if ( len(info_client) == 10 ): # if classes hours > 9
            buffer.append(info_client[0:2])
            buffer.append(info_client[2:6]) # extract year
            buffer.append(info_client[6:8]) # extract month
            buffer.append(info_client[8] + info_client[9]) # extract id
        elif ( len(info_client) == 9 ):
            buffer.append(info_client[0])
            buffer.append(info_client[1:5]) # extract year
            buffer.append(info_client[5:7]) # extract month
            buffer.append(info_client[7] + info_client[8]) # extract id
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
    # 3 --> 1 <= <duration> <= 30

    # unique convert to int
    try:
        for info in case:
            buffer.append(int(info))
    except ValueError:
        debugLogs(f"error from convert_info --> {info}")
        return []
    
    if (not (1 <= buffer[0] <= 30)):
        debugLogs(f"from 'convert_info' -> not in hours range")
        return []
    elif (not (2000 <= buffer[1] <= 2010)): 
        debugLogs(f"from 'convert_info' -> not in year range")
        return []
    elif (not (1 <= buffer[2] <= 12)):            
        debugLogs(f"from 'convert_info' -> not in month range")
        return []
    elif (not (10 <= buffer[3] <= 99)):      
        debugLogs(f"from 'convert_info' -> not in id range")
        return []
    else: 
        return buffer

class Client:
    """object of the data customers"""
    _clientInfo = list
    
    def get_clasess(self): return self._clientInfo[0]

    def get_year(self): return self._clientInfo[1]

    def get_month(self): return self._clientInfo[2]

    def get_clientID(self): return self._clientInfo[3]

    def get_data_ofpointer(self, pos : int): 
        if (0 <= pos <= len(self._clientInfo)):
            return self._clientInfo[pos]

    def __init__(self, info_client : list):
        self._clientInfo = info_client

    def __str__(self) -> str: # redefine print
        return f"\n1. Продолжительность занятий: {self._clientInfo[0]}\n"\
               f"2. Год: {self._clientInfo[1]}\n"\
               f"3. Месяц: {self._clientInfo[2]}\n"\
               f"4. Код клиента: {self._clientInfo[3]}\n"

class Container:
    """class for contain and management of the data customers"""
    _container = []

    def __init__(self, array = []):
        self._container = array 

    def __str__(self) -> str: # redefine print
        out = ''
        for client in range(0, len(self._container)):
            out.join(f"Номер клиента: {client}\n")
            print(self._container[client])

    def append(self, client : Client):
        self._container.append(client)
    
    def data_filter(self, filter : int, field : int) -> list:
        buffer = []
        for data in self._container:
            if (data.get_data_ofpointer(field) == filter):
                buffer.append(data)
        return buffer

    def get_container(self):
        return self._container

    def at(self, object : int):
        if (0 <= object <= len(self._container)):
            return self._container[object]
        else:
            debugLogs(f"func 'at' from <Container> -> index out of range : {object}")
            return None

def main():
    with open("testcases/testcase_ExamTaskC13.txt") as file:
        # get the data
        testcases = file.readlines()

        # download of the data for hendler
        clients = Container()
        for testcase in testcases:
            testcase = testcase.removesuffix("\n")
            contain = convert_info(extract_info(testcase))

            debugLogs(f"testcase {testcase}")
            debugLogs(f"contain {contain}\n")

            if ( not(contain == []) ): # valid to void 
                clients.append(Client(contain))
            elif (contain == []): # is void 
                debugLogs("from 'main' -> var 'contain' is void")


        if (clients.get_container() == []): # valid to void
            debugLogs("from 'main' -> var 'clients' is void")
        elif (not(clients.get_container() == [])):    
            debugLogs(f"from 'main' -> array of 'clients' {clients.at(0)}")
            
            # diplay customers id`s
            # num = 1
            # print("Доступные коды клиентов:")
            # for customer in clients.get_container():
            #     print(f"    {num}: {customer.get_clientID()}")
            #     num+=1
            
            input_id = valid_inpt("Введите код клиента: \n> ")
            client_with_id = Container(clients.data_filter(input_id, 3))

            if (client_with_id.get_container() == []): return "Данные отсутствуют"    

            print(f"Информация о клиенте с кодом: {input_id}:")
            # handle of the filter: year -> max(classes) -> min(month)

            for client in client_with_id.get_container():
                debugLogs(client)

            filtred_array = dict()
            for client in client_with_id.get_container():
                if ( filtred_array.get(client.get_year()) is None ):
                    filtred_array[client.get_year()] = \
                    {
                        'max_duration' : client.get_clasess(), 
                        'min_month' : client.get_month()
                    }
                else:
                    if (client.get_clasess() > filtred_array[client.get_year()]['max_duration']):
                        filtred_array[client.get_year()]['max_duration'] = client.get_clasess()
                    elif (client.get_clasess() == filtred_array[client.get_year()]['max_duration']):
                        filtred_array[client.get_year()]['min_month'] = \
                            min(client.get_clasess(), filtred_array[client.get_year()]['min_month'])
            
            out = ''
            for key in filtred_array.keys():
                out = out + f"{key} {filtred_array[key]['min_month']} {filtred_array[key]['max_duration']}\n"
            return out
            

if __name__ == "__main__":
    print(main())