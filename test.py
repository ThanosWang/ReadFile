import sys
filenames = sys.argv[1]
addedfiles = filenames.split(',')
for i in addedfiles:
    assert i.endswith('.txt')
    f = open(i,'r')
    F = f.read()
    print(F)