# Дан файл с более чем 50 целыми числами. Удалить конечные так, чтобы в результате
# осталось 50 первых чисел чисел


def main():
    pass


if __name__ == "__main__":
    file_dyn = open("testcases/testcase_File29_dynamic.txt", "r")
    seq1 = file_dyn.readline().split(" ")
    file_dyn.close()
    file_dyn = open("testcases/testcase_File29_dynamic.txt", "w")

    for wd in range(0, 50):
        num = int(seq1[wd])
        print(num, end=' ')
        file_dyn.write(f"{num}\n")

    #file_dyn.write("\n\n\nreCount nums 50")

    file_dyn.close()
    