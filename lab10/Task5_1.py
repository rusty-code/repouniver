# Дана СЛАУ
# Решить её!!1!!111


import numpy as np


matrix_A = np.array([ # left part with only mod`s
    [1.5, -0.8, 4.25],
    [1.2, 7.18, -3.2],
    [0.5, -1.5, 7.1 ]
])


matrix_B = np.array([ # right part of uravneniy
        5.1,
        4.2,
        -1.2
])


print("СЛАУ имеет вид: ")
print(f"1.5x1 - 0.8x2 + 4.25x3 = 5.1")
print(f"1.2x1 + 7.18x2 - 3.2x3 = 4.2")
print(f"0.5x1 - 1.5x2 + 7.1x3 = -1.2")
print()
print("Решение этой СЛАУ: ")
solve = np.linalg.solve(matrix_A, matrix_B) # array of x1, x2, x3
print(f"x1 = {solve[0]}")
print(f"x2 = {solve[1]}")
print(f"x3 = {solve[2]}")

print(f"1.5x1 - 0.8x2 + 4.25x3 = {round(1.5*solve[0] - 0.8 * solve[1] + 4.25 * solve[2], 5)} = 5.1")
print(f"1.2x1 + 7.18x2 - 3.2x3 = {round(1.2*solve[0] + 7.18 * solve[1] - 3.2 * solve[2], 5)} = 4.2")
print(f"0.5x1 - 1.5x2 + 7.1x3 = {round(0.5*solve[0] - 1.5 * solve[1] + 7.1*solve[2], 5)} = -1.2")