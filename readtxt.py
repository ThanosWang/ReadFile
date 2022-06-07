import os

os.chdir('.txtfiles')

for i in os.listdir():
    f = open(i, 'r')
    F = f.read()
    print(F)
    f.close()
