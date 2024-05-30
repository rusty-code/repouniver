
def is_powtwo(num) -> bool:
    for pw in range(0, 64):
        powtwo = pow(2, pw)

        if powtwo > num: return False
        if num == powtwo: return True


def count_dischargs(msg):
    ctrl = -1

    for var in range(0, 32):
            exp = len(msg) + 1 + var
            pw = pow(2, var)
            if exp <= pw:
                return var
    if ctrl == -1:
        print("(ERROR) unfound countrol dischargs")

    return ctrl


def part_digit(num) -> list:
    
    def search(var):
        tmp = 1
        if tmp == var: return tmp # default case

        while (tmp <= var): 
            tmp *= 2
        return tmp//2

    num = int(num)
    digits = []

    while (num > 0):
        # valid
        res = search(num)
        digits.append(res)
        num -= res
    
    return digits

def append_args(msg, args, count_args) -> list:

    for ind in range(0, len(msg)):

        if msg[ind] != ' ':
            for ind1 in part_digit(ind+1): # get indexes for append 
                for arg in args: # append for ind1
                    if arg[0] == ind1:
                        arg.append(ind+1)

    return args

def calc_seq(msg : str, digits : list):

    def mod_sum(left : int, right : int):
        if left != right: return 1
        return 0


    res = msg[digits[1]-1]
    res = int(res)

    for it in range(2, len(digits)):
        res = mod_sum(res, int(msg[digits[it]-1]))

    return res


def process_start(msg : str):
    
    count_args = count_dischargs(msg)

    mtble_msg = ''
    crg = 0
    for ind in range(1, count_args+len(msg)+1):
        if is_powtwo(ind):
            mtble_msg = mtble_msg + ' '
        else:
            mtble_msg = mtble_msg + msg[crg]

            crg += 1

    print(f"(ПРОМЕЖУТОЧНЫЙ РЕЗУЛЬТАТ1) {mtble_msg}") 

    print(f"(ПРОМЕЖУТОЧНЫЙ РЕЗУЛЬТАТ2) проверка разбиения числа:")
    for it in range(1, 32): # PERFECT
        print(f"{it} : {part_digit(it)}")


    args = []
    for it in range(0, count_args):
        args.append([])

    # append a start nums
    pw = 1
    for aset in range(0, len(args)):
        args[aset].append(pw)
        pw *= 2

    args = append_args(mtble_msg, args, count_args)

    print(f"(ПРОМЕЖУТОЧНЫЙ РЕЗУЛЬТАТ3) проверка заполенения множеств:")
    for it in args:
        print(*it)

    ctrl_dh = []
    for seq in args:
        ctrl_dh.append(calc_seq(mtble_msg, seq))


    hemming = ''
    crg = 0
    ctrl_crg = 0
    for ind in range(1, count_args+len(msg)+1):
        if is_powtwo(ind):
            hemming = hemming + f"{ctrl_dh[ctrl_crg]}"
            ctrl_crg += 1
        else:
            hemming = hemming + msg[crg]

            crg += 1
         

    return hemming


