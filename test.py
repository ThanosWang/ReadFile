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
        os.chdir(path)
        for i in os.listdir():
            f = open(i,'r')
            F = f.read()
            print(F)
