# Дан файл вещественных чисел. Найти кол-во его локальных минимумов и максимумов

import random

# Convert an elements from str to float
def convert_str_to_realnums(lst : list) -> list:
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = float(it)
        except ValueError:
            continue
        tmpLst.append(tmpNum)
    return tmpLst

# Get random sequence with random lenght
def generate_sequence() -> list:
    ret_seq = []
    for it in range(0, random.randint(3, 12)):
        ret_seq.append(round(random.random()*10, 5))

    print("The random seq: ", *ret_seq)
    return ret_seq


def main():


    with open("testcases/testcase_File20.txt") as _f:
        file = _f.readlines()
        # Extract test sequnces from file
        testcases = \
        [convert_str_to_realnums(file[it].split()) for it in range(0, len(file))] # array of the real num`s
        # User testcase
        testcases.append(generate_sequence())
        
        k = 1 # num of test case
        for testcase in testcases:
            print(f"Тест {k}:")

            if len(testcase) > 0:
                print(*testcase)
                sequnce_data = []
                for n in range(1, len(testcase)-1):
                    if testcase[n] < testcase[n-1] and \
                        testcase[n] < testcase[n+1]:
                        # element n is extremum
                        sequnce_data.append(testcase[n])
                    elif testcase[n] > testcase[n-1] and \
                        testcase[n] > testcase[n+1]:
                        # element n is extremum
                        sequnce_data.append(testcase[n])
                if len(sequnce_data) > 1:
                    print("Extrem`s:\n", *sequnce_data, '\n')
                else:
                    print(f"Test case {k} has no extremes\n")
            else:
                    print(f"Test case {k} is void\n")
            k+=1


if __name__ == "__main__":
    # test()
    main()