
import os
import sys


os.chdir('Models')
models_path = os.getcwd()

for model in os.listdir():
    os.chdir(model)
    modelpath = os.getcwd()
    
    sys.path.insert(0,modelpath)

    import object_library
    import parameters
    import particles
    
    print('%s contains particles below' %(modelpath))
    for i in [item for item in dir(particles) if not item.startswith("__")]:
        item = getattr(particles,i)
        if type(item) == (object_library.Particle):
            print('Particle %s with pdg code %i' %(item.name,item.pdg_code))

    del sys.modules['object_library']
    del sys.modules['parameters']
    del sys.modules['particles']

    sys.path.remove(modelpath)

    os.chdir(models_path)

    