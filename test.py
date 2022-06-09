import sys

import os

if len(sys.argv) == 1:
    sys.exit()
else:
    filenames = sys.argv[1]
    addedfiles = filenames.split(',')
    for i in addedfiles:
        assert i.endswith('.txt')
        path = os.path.dirname(os.path.realpath(i))
        print(path)
        f = open(i,'r')
        F = f.read()
        assert 1 == F.count('.\n') + F.count('!\n') + F.count('?\n')