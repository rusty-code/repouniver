

# opens files of data
files = \
[
    open("testcases/testcase_File48_SA.txt", 'w'),
    open("testcases/testcase_File48_SB.txt", 'w'),
    open("testcases/testcase_File48_SC.txt", 'w')
]

# append sequence 0, 1, 2, ... in all files
# for fl in files:
#     for num in range(0, 20):
#         fl.write(f"{num}\n")

# 1.1 2.2 3.3 | 1.4 2.5 2.6 ... 
for num in range(0, 40, 3):
    files[0].write(f"{num}\n")
    files[1].write(f"{num+1}\n")
    files[2].write(f"{num+2}\n")

# close files
for fl in files:
    fl.close()