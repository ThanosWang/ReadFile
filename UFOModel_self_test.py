#This is a test which you can use to test your completeness of model before you upload your model to GitHub repository
#Please use the four model-independent files provided in the GitHub repository 

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
for i in [item for item in dir(parameters) if not item.startswith("__")]:    
    item = getattr(parameters,i)
    if type(item) == (object_library.Parameter):
        params.append(item.name)

if len(params) == 0:
    raise Exception('There should be parameters defined in you parameters.py.')

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
names = []
for i in [item for item in dir(particles) if not item.startswith("__")]:
    item = getattr(particles,i)
    if type(item) == (object_library.Particle):
        names.append(item.name)

if len(names) == 0:
    raise Exception('There should be particles defined in you particles.py.')

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
for i in [item for item in dir(lorentz) if not item.startswith("__")]:    
    item = getattr(lorentz,i)
    if type(item) == (object_library.Lorentz):
        lorentz_tensor.append(item.name)

if len(lorentz_tensor) == 0:
    raise Exception('There should be lorentz tensors defined in you lorentz.py.')

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
for i in [item for item in dir(coupling_orders) if not item.startswith("__")]:
    item = getattr(coupling_orders,i)
    if type(item) == (object_library.CouplingOrder):
        coupling_order.append(item.name)

if len(coupling_order) == 0:
    raise Exception('There should be coupling orders defined in you couplings.py.')




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
for i in [item for item in dir(couplings) if not item.startswith("__")]:
    item = getattr(couplings,i)
    if type(item) == (object_library.Coupling):
        coupling_tensor.append(item.name)

if len(coupling_tensor) == 0:
    raise Exception('There should be coupling tensors defined in you couplings.py.')


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
for i in [item for item in dir(vertices) if not item.startswith("__")]:
    item = getattr(vertices,i)
    if type(item) == (object_library.Vertex):
        vertex.append(item.name)

if len(vertex) == 0:
    raise Exception('There should be vertices defined in you vertices.py.')



