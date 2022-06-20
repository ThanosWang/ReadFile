import os
import sys

os.chdir('Models')

for folder in os.listdir():

    folderpath = os.getcwd()

    os.chdir(folder)
    
    modelpath = os.getcwd()

    sys.path.insert(0,modelpath)

    import object_library

    import particles

    print('%s contains ' %(modelpath))

    for i in [item for item in dir(particles) if not item.startswith("__")]:
        item = getattr(particles,i)
        if type(item) == (object_library.Particle):
            print('Particle %s with pdg code %i ' %(item.name, item.pdg_code))

    os.chdir(folderpath)
