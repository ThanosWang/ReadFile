import sys
if len(sys.argv) == 1:
    break
else:
    filenames = sys.argv[1]
    addedfiles = filenames.split(',')
    for i in addedfiles:
        assert i.endswith('.txt')
        f = open(i,'r')
        F = f.read()
        assert 1 == F.count('./n') + F.count('!/n') + F.count('?/n')