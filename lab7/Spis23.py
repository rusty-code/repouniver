# Дана поcледовательномть чисел. Определить, какие элементы нужно добавить и их минимальное кол-во, чтобы она стала симметр.

DEBUG = True # for output debugging info

def valid_convert(num): # valid.: element must be a num!
    try:
        return int(num)
    except ValueError:
        print(f'Из ввода было исключено: {num}') # if not a num, then return 'None'

def debug_log(str_end = " "):
    if DEBUG:
        print("#DEBUG_MES: ", end = str_end)
    return DEBUG

def compare_subarrays(fullarray, subleft, subright):
    if debug_log(): print(subleft)
    if debug_log(): print(subright)

    mas = [] # for read elements of answer
    mn = len(cspis) # store count elem. of answer
    action = ''

    if len(subleft) > len(subright):

        tl1 = [subleft[elem] for elem in range(0, len(subright))] # create subarray of right tail with size of right array 

        if tl1 == subright:
            if mn > len(subleft) - len(subright): # find minimal len of lackig elements
                mn = len(subleft) - len(subright)    
                mas = [subleft[elem] for elem in range(len(subleft)-1, len(subleft) - len(tl1) - 2, -1) ]
                action = "дописать"

            if debug_log(): print(f"Нужно дописать {len(subleft) - len(subright)} элементов: {[subleft[elem] for elem in range(len(subleft)-1, len(subleft) - len(tl1) - 2, -1) ]}")
    
    elif len(subright) > len(subleft):

        tl2 = [subright[elem] for elem in range(0, len(subleft))] # create subarray of left tail with size of left array

        if tl2 == subleft:
            if mn > len(subright) - len(subleft): # find minimal len of lackig elements
                mn = len(subright) - len(subleft)
                mas = [subright[elem] for elem in range(len(subright)-1, len(tl2)-1, -1) ]
                action = "приписать"

            if debug_log(): print(f"Нужно приписать {len(subright) - len(subleft)} элементов: {[subright[elem] for elem in range(len(subright)-1, len(tl2)-1, -1) ]}")

    elif len(subleft) == len(subright):

        if subleft == subright:        
            print("Список симметричен...")
            mn = 0 # is 

        else:
            if mn > len(fullarray)-1:
                mn = len(fullarray)-1
                mas = [fullarray[elem] for elem in range( len(fullarray)-2, -1, -1 ) ]
                action = "дописать"

            if debug_log(): print(f"Нужно дописать {len(fullarray)-1} элементов { [fullarray[elem] for elem in range( len(fullarray)-2, -1, -1 ) ] }")

    return [mn, mas, action]

# ( 1 + 2 ) /3
#  list = [] <- ( 1 + 2 ) /3
# [(,  , , /.....]  
#
TEST_CASES = open('testcase_forspis23.txt', 'r').readlines()

print('#LIST OF TEST CASES: ')
print(TEST_CASES)


for enumerate in TEST_CASES: 
    spis = enumerate.split() # list(input("Введите список элементов через пробел: ").split()) # Создание списка под элнменты ввода 

    cspis = list() # list of cleaning input
    for it in range(0, len(spis)):
        conv = valid_convert(spis[it])
        if conv != None: # if elem. is num, then push him into list 
            cspis.append(valid_convert(spis[it]))

    print("\n#####################################################\n")

    print("Очищенный список: ", cspis)

    # (EXPERIMENTAL):
    ANSWER = [[], len(cspis), '']
    if debug_log(): print(ANSWER)


    if len(cspis) == 1: # default case
        print("Эта последовательность симметрична..")
    elif len(cspis) == 2: # simple case
        if cspis[0] != cspis[1]:
            mn = 1
            mas = [cspis[0]]
    else:
        # case 0: len % 2 != 0
        # 1 2 [3] 2 [1] 2 -> middle: 3; 1 
        step = 0 # ident from the middle
        for here in range(1, len(cspis) - 1): # enumeration of a middle elements
            if here - step >= 0: # check to not out of range
                if cspis[here - 1] == cspis[here + 1]: # Middle element was finded

                    if debug_log(): print(f"Middle element {cspis[here]}")

                    # splitting into right and left subarrays of relative middle
                    tail1 = [cspis[elem] for elem in range(here-1, -1, -1)] # is left
                    tail2 = [elem for elem in cspis[here+1:]] # is right

                    ANSWER = compare_subarrays(cspis, tail1, tail2)
                    if debug_log(): print("# -- ", ANSWER[0], ANSWER[1])
            step += 1


        # case 1: len % 2 == 1
        # and middle is pair elems : 1 3 2 2 3 1 --> 2 2
        step = 0 # ident from middle pair
        for here in range(1, len(cspis)-2): # start enumreting of pair
            next = here+1 # is second element of the pair
            if here - step >= 0: # check out of range
                if cspis[here] == cspis[next]: # if pair may be middle
                    if cspis[here - 1] == cspis[next + 1]: # middle pair was finded

                        if debug_log(): print(f"Middle pair {cspis[here]} - {cspis[next]}")

                        # splitting into right and left subarrays of relative middle pair
                        tail1 = [cspis[elem] for elem in range(here-1, -1, -1)] # is left
                        tail2 = [elem for elem in cspis[next+1:]] # is right

                        ANSWER = compare_subarrays(cspis, tail1, tail2)
                        if debug_log(): print(ANSWER)
                        if ANSWER[2] == "дописать":
                            tmp = ANSWER[1][:-1]
                            if debug_log(): print("# -- ", tmp, ANSWER[0], ANSWER[1]) # why ANSWER[0] and ANSWER[1] swithes!??!?!
                            ANSWER[0] = tmp
            step += 1



    # (EXPEREMENTAL):
    if ANSWER[0] == [] and ANSWER[1] == len(cspis):
        if debug_log(): print("Nothig wasn`t finded...")
        ANSWER[1] -= 1
        ANSWER[2] = "дописать"
        ANSWER[0] = [ cspis[elem] for elem in range(len(cspis)-2, -1, -1) ]

    # Output answer
    print()
    print(f"Кол-во недостающих чисел, которые нужно {ANSWER[2]} состоит из {ANSWER[0]} элементов, таких как: {ANSWER[1]}", end = '')
    # if ANSWER[0] != []:
    #     print(ANSWER[1], end='\n')

print()