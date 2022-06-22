#This is the test used by GitHub Workflow
#Please upload one folder each time

import os,sys

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

    # Working in uploaded directory
    sys.path.insert(0,path)

    # Check the existence of model-indeoendent files
    NeccessaryFiles = ['__init__.py', 'object_library.py', 'function_library.py', 'write_param_card.py']
    MissingFiles = [i for i in NeccessaryFiles if i not in ModelFiles]
    if MissingFiles != []:
        print('Your model lacks these files below')
        print(MissingFiles)
        raise Exception('Sorry, your upload fails since your model is short of some necessary files.')

    import object_library

    # Check the completeness of parameters.py
    try:
        import parameters
    except ModuleNotFoundError:
        raise Exception('You model contains no parameters.py, please check again')
    except AttributeError:
        raise Exception('You may forget to define variables in your imported modules, please check again.')
    except NameError:
        raise Exception('You may forget to import/define some modules, please check again.')
    except TypeError:
        raise Exception('One/Some of your parameters missing required positional argument, please check again.')

    #Check if parameters.py contains parameters
    params = []
    number_of_params = 0
    for i in [item for item in dir(parameters) if not item.startswith("__")]:    
        item = getattr(parameters,i)
        if type(item) == (object_library.Parameter):
            params.append(item.name)
            number_of_params += 1

    if len(params) == 0:
        raise Exception('There should be parameters defined in you parameters.py.')

    print('You model contains %i parameters.' %(number_of_params))





    # Check the completeness of particles.py
    try:
        import particles
    except ModuleNotFoundError:
        raise Exception('You model contains no particles.py, please check again')
    except AttributeError:
        raise Exception('You may forget to define variables in your imported modules, please check again.')
    except NameError:
        raise Exception('You may forget to import/define some modules, please check again.')
    except TypeError:
        raise Exception('One/Some of your particles missing required positional argument, please check again.')

    #Check if particles.py contains particles
    particlenames = []
    number_of_particles = 0
    for i in [item for item in dir(particles) if not item.startswith("__")]:
        item = getattr(particles,i)
        if type(item) == (object_library.Particle):
            particlenames.append(item.name)
            number_of_particles += 1

    if len(particlenames) == 0:
        raise Exception('There should be particles defined in you particles.py.')

    print('You model contains %i particles below：' %(number_of_particles))
    print(particlenames)





    # Check the completeness of lorentz.py
    try:
        import lorentz
    except ModuleNotFoundError:
        raise Exception('You model contains no lorentz.py, please check again')
    except AttributeError:
        raise Exception('You may forget to define variables in your imported modules, please check again.')
    except NameError:
        raise Exception('You may forget to import/define some modules, please check again.')
    except TypeError:
        raise Exception('One/Some of your lorentz tensors missing required positional argument, please check again.')

    #Check if lorentz.py contains lorentz tensors
    lorentz_tensor = []
    number_of_lorentz_tensors = 0
    for i in [item for item in dir(lorentz) if not item.startswith("__")]:    
        item = getattr(lorentz,i)
        if type(item) == (object_library.Lorentz):
            lorentz_tensor.append(item.name)
            number_of_lorentz_tensors += 1

    if len(lorentz_tensor) == 0:
        raise Exception('There should be lorentz tensors defined in you lorentz.py.')

    print('You model contains %i lorentz tensors.' %(number_of_lorentz_tensors))





    # Check the completeness of coupling_orders.py
    try:
        import coupling_orders
    except ModuleNotFoundError:
        raise Exception('You model contains no coupling_orders.py, please check again')
    except AttributeError:
        raise Exception('You may forget to define variables in your imported modules, please check again.')
    except NameError:
        raise Exception('You may forget to import/define some modules, please check again.')
    except TypeError:
        raise Exception('One/Some of your coupling orders missing required positional argument, please check again.')

    #Check if coupling_orders.py contains orders
    coupling_order = []
    number_of_coupling_orders = 0
    for i in [item for item in dir(coupling_orders) if not item.startswith("__")]:
        item = getattr(coupling_orders,i)
        if type(item) == (object_library.CouplingOrder):
            coupling_order.append(item.name)
            number_of_coupling_orders += 1

    if len(coupling_order) == 0:
        raise Exception('There should be coupling orders defined in you couplings.py.')

    print('You model contains %i coupling orders.' %(number_of_coupling_orders))





    # Check the completeness of couplings.py
    try:
        import couplings
    except ModuleNotFoundError:
        raise Exception('You model contains no couplings.py, please check again')
    except AttributeError:
        raise Exception('You may forget to define variables in your imported modules, please check again.')
    except NameError:
        raise Exception('You may forget to import/define some modules, please check again.')
    except TypeError:
        raise Exception('One/Some of your coupling tensors missing required positional argument, please check again.')

    #Check if couplings.py contains couplings
    coupling_tensor = []
    number_of_coupling_tensors = 0
    for i in [item for item in dir(couplings) if not item.startswith("__")]:
        item = getattr(couplings,i)
        if type(item) == (object_library.Coupling):
            coupling_tensor.append(item.name)
            number_of_coupling_tensors += 1

    if len(coupling_tensor) == 0:
        raise Exception('There should be coupling tensors defined in you couplings.py.')

    print('You model contains %i coupling tensors.' %(number_of_coupling_tensors))





    # Check the completeness of vertices.py
    try:
        import vertices
    except ModuleNotFoundError:
        raise Exception('You model contains no vertices.py, please check again')
    except AttributeError:
        raise Exception('You may forget to define variables in your imported modules, please check again.')
    except NameError:
        raise Exception('You may forget to import/define some modules, please check again.')
    except TypeError:
        raise Exception('One/Some of your vertices missing required positional argument, please check again.')

    #Check if vertices.py contains vertices
    vertex = []
    number_of_vertices = 0
    for i in [item for item in dir(vertices) if not item.startswith("__")]:
        item = getattr(vertices,i)
        if type(item) == (object_library.Vertex):
            vertex.append(item.name)
            number_of_vertices += 1

    if len(vertex) == 0:
        raise Exception('There should be vertices defined in you vertices.py
    
    print('You model contains %i vertices.' %(number_of_vertices))