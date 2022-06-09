import sys

import os

if len(sys.argv) == 1:
    sys.exit()
else:
    filenames = sys.argv[1]
    addedfiles = filenames.split(',')
    path = os.path.dirname(os.path.realpath(addedfiles[0]))
    os.chdir(path)
    for i in os.listdir():
        print(i)