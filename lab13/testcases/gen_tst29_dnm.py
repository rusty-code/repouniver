import random

file = open("testcases/testcase_File29_dynamic.txt", "w+") 


sequence_len = random.randint(51, 100)
sequence = []

for it in range(0, sequence_len):
    sequence.append(random.randint(-100, 100))

for num in sequence:
    file.write(f"{num} ")

file.write(f'\n\n\nCount nums: {sequence_len}')

print(len(sequence), sequence_len)

file.close()