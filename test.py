import os

os.chdir('.txtfiles')

Alltxtfiles = os.listdir()

assert 'No1.txt' in Alltxtfiles 

assert 'No2.txt' in Alltxtfiles 

assert 'No3.txt' in Alltxtfiles 

assert 'No4.txt' in Alltxtfiles 

assert 'No5.txt' in Alltxtfiles 

assert open('No1.txt','r').read() == 'Hello!'

assert open('No2.txt','r').read() == 'I am Zijun Wang.'

assert open('No3.txt','r').read() == 'This is my first GitHub repository.'

assert open('No4.txt','r').read() == 'I will try to use continuous integration in this repository.'

assert open('No5.txt','r').read() == 'I hope I can succeed!'

assert len(Alltxtfiles) > 5

Newtxtfiles = [i for i in Alltxtfiles if i not in ('No1.txt','No2.txt','No3.txt','No4.txt','No5.txt')]

for i in Newtxtfiles:
    assert i.endswith('.txt')
    f = open(i,'r')
    F = f.read()
    assert 1 == F.count('.\n') + F.count('!\n') + F.count('?\n')