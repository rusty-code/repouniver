# Найти наибольший отрезок в файле по данным координатам

file = open('thetri1.otr', 'r')
N = int(file.readline())

# (x2 - x1) ** 2 ...
def lenOtr(list):
    # по формуле длины вектора 
    xx = (list[0] - list[2])**2
    yy = (list[1] - list[3])**2
    return ( xx + yy ) ** (1/2)

mx = 0
l1st = [0] * 4
#print("N: ", N)
for it in range(0, N): # итерация по строкам в файле
    out = 0
    for it1 in file.readline().split(): # чтение строки и  итерация по ней
        try: 
            #print(out, it1)
            l1st[out] = int(it1)
            out += 1
        except ValueError:
            #print("error: ", out)
            out += 1
    #print(l1st, lenOtr(l1st))
    if mx < lenOtr(l1st):
        mx = lenOtr(l1st)

print("Максимальная длина: ", round(mx, 3))

file.close()