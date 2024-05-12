

file = open("./testcases_forspis25.txt").readlines()

spis = [elem.split() for elem in file]

cspis = [] # store for 'cleaned' elements 

# clearing elements of punctuation marks
for elem in spis:
    for elem1 in elem:
        st = ''
        for elem2 in elem1:
            if elem2 not in "!?.,:":
               st = st + elem2
        cspis.append(st)

print(cspis)

mx_len = 0
for it in cspis:
    mx_len = max(mx_len, len(it))

print("Максимальная длина слова: ", mx_len)
print("Список слов, имеющих максимальную длину: ")
for it in cspis:
    if len(it) == mx_len:
        print(it)
