import numpy as np
from sympy import *
from sympy.physics.quantum import TensorProduct
from functools import reduce
from qiskit.quantum_info import *
from scipy.optimize import minimize
from numpy.testing import assert_array_almost_equal as aae
from typing import *

def default_import(items:list = ['a', 'r', 'g', 'm', 'q']):
    
    import_statements = {'a': 'from FrozenYoghourt import *', 
                         'r': 'from FrozenYoghourt.mode import Mode as r\n', 
                         'g': 'from FrozenYoghourt.gates import Gates as g\n', 
                         'm': 'from FrozenYoghourt.maths import Maths as m\n', 
                         'q': 'from FrozenYoghourt.quantum import Quantum as q'}
    
    
    import_str = ''
    for item in items:
        import_str += import_statements[item]
        
    print(import_str)
    
def view(mat, rounding = 10):
    if type(mat) == np.ndarray:
        display(Matrix(np.round(mat, rounding)))
    else:
        display(round(mat, rounding))
        
   