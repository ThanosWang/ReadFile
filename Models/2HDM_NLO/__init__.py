# This is a sample script based on different models

# Import necessary files of UFO model
import particles
import couplings
import lorentz
import parameters
import vertices
import coupling_orders
import function_library
import write_param_card

all_particles = particles.all_particles
all_couplings = couplings.all_couplings
all_lorentz = lorentz.all_lorentz
all_parameters = parameters.all_parameters
all_vertices = vertices.all_vertices
all_orders = coupling_orders.all_orders
all_functions = function_library.all_functions

# Try to import optional files 
try:
    import propagators
except ImportError:
    pass
else:
    all_propagators = propagators.all_propagators

try:
    import decay
except ImportError:
    pass
else:
    all_decays = decay.all_decays

try:
   import form_factors
except ImportError:
   pass
else:
   all_form_factors = form_factors.all_form_factors

try:
    import CT_vertices
except ImportError:
    pass
else:
    all_CTvertices = CT_vertices.all_CTvertices

try:
    import CT_parameters
except ImportError:
    pass
else:
    all_CTparameters = CT_parameters.all_CTparameters

gauge = [0, 1]

__author__ = 'C. Duhr, M. Herquet, C. Degrande'
__date__ = '12. 10. 2015'
__version__ = '1.2'