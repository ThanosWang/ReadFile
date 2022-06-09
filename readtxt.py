import os

os.chdir('Models')

for folder in os.listdir():
    path = os.getcwd()
    os.chdir(folder)
    for txt in os.listdir():
        files = open(txt,'r')
        Files = files.read()
        print(Files)
        files.close()
    os.chdir(path)