import sys

import os

if len(sys.argv) == 1:
    # If no file added, just finish the check
    sys.exit()
else:
    # Find names of added files
    filenames = sys.argv[1]
    addedfiles = filenames.split(',')
    print('Your added Files are:')
    print(addedfiles)    

    # Find path of added files
    path = os.path.dirname(os.path.realpath(addedfiles[0]))

    # Lead to the directory of added files
    os.chdir(path)

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

    print('Your model contains neccessary files for UFO Model. Uploading succeeded. Thank you!')
    