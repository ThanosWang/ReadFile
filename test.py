import sys

import os

if len(sys.argv) == 1:
    # If no file added, just finish the check
    sys.exit()
else:
    # Find names of added files
    filenames = sys.argv[1]
    addedfiles = filenames.split(',')
    
    # Find path of added files
    path = os.path.dirname(os.path.realpath(addedfiles[0]))

    # Lead to the directory of added files
    os.chdir(path)
    
    # Show all files in the model
    ModelFiles = os.listdir()
    print('Your model contains')
    print(ModelFiles)

    # Feedback if missing necessary files
    NeccessaryFiles = ['__init__.py', 'object_library.py', 'function_library.py', 'write_param_card.py', 'particles.py', 'parameters.py', 'vertices.py', 'couplings.py', 'coupling_orders.py']
    MissingFiles = [i for i in NeccessaryFiles if i not in ModelFiles]
    if MissingFiles != []:
        print('Your model lacks these files:')
        print(MissingFiles)
        print('Sorry, your upload fails since your model is short of some necessary files.')

    # Check required files for UFO Models
    assert os.path.exists('__init__.py')

    assert os.path.exists('object_library.py')

    assert os.path.exists('function_library.py')

    assert os.path.exists('write_param_card.py')
    
    assert os.path.exists('particles.py')

    assert os.path.exists('parameters.py')
    
    assert os.path.exists('vertices.py')

    assert os.path.exists('couplings.py')

    assert os.path.exists('lorentz.py')
    
    assert os.path.exists('coupling_orders.py')

    print('Your model contains neccessary files for UFO Model. Upload succeeded. Thank you!')
    