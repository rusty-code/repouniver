# Генерация неубывающего списка целых чисел размерности <200 
# Рандомное число дублируется рандомное число раз

import random

file = open("input_sort13.txt", 'w')

the_var = random.randint(-100, 100)
count_var = random.randint(1, 200)
print(f"This var: {the_var}")
print(f"Number this var: {count_var + 1}")
array = [int(it) for it in range(-101, the_var-count_var)]+[the_var]*count_var+[int(it) for it in range(the_var, 101-count_var)]
print(f"Lenght arrays nums: {len(array)}")

for it in array:
    file.write(f"{it} ")

file.write('\n\n\n')
file.write(f"This var: {the_var}\n")
file.write(f"Number this var: {count_var+1}\n")
file.write(f"Lenght of array nums: {len(array)}")

file.close()