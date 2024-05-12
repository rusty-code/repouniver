
# Даны две непустые очереди
# Объединить их в одну и выввести начальный и конечные элементы

import structreofdata.classQueue as sodq
from structreofdata.valid_input import valid_inpt as vinput



def main():

    queue1 = sodq.Queue()
    queue1.push(1)
    queue1.push(3)
    queue1.push(5)

    print("Первая очередь:")
    print(queue1)

    queue2 = sodq.Queue()
    queue2.push(2)
    queue2.push(4)
    queue2.push(6)
    
    print("Вторая очередь:\n", queue2, end='\n')

    queue = sodq.merge(queue1, queue2)
    print(f"result:\n{queue}")
    # queue1.merge_queues(queue2)

    # print("Объединение очередей:") 
    # print(queue1)

if __name__ == "__main__":
    main()