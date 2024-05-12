# Даны 3 файла с одинаковыми последовательностями
# Создать доп файл, в котором элементы всеx поcледовательностей идут по своему порядковому номеру


# create file
add_file = open("testcases/res_File48_SC.txt", "w+")

# opens files of data
files = \
[
    open("testcases/testcase_File48_SA.txt", 'r'),
    open("testcases/testcase_File48_SB.txt", 'r'),
    open("testcases/testcase_File48_SC.txt", 'r')
]

# extract data from files
sequences = []
for fl in files:
    sequences.append(fl.readlines())


for elem in range(0, len(sequences[0])):
    add_file.write(sequences[0][elem])
    add_file.write(sequences[1][elem])
    add_file.write(sequences[2][elem])


# close files
for fl in files:
    fl.close()

# close res file
add_file.close()