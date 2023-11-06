# cython: language_level=3str
# distutils: define_macros=NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION

"""
Teasing out factors for numpy issue #25061, where passing a float to Cython code
[like np.random.RandomState.multinomial()] might raise
    TypeError: 'float' object cannot be interpreted as an integer
depending whether this code is compiled with Cython==0.29 + numpy==1.25.2
vs. Cython==3.0 + numpy==1.26.1, which declare npy_intp differently.
"""

cimport numpy as np


def func_int(int length):
    """Accepts a C int or a float."""
    return length

def func_Py_ssize_t(Py_ssize_t length):
    """Accepts a C long; never a float."""
    return length

def func_npy_intp(np.npy_intp length):
    """Accepts a C long; float depends on Cython and numpy versions since they
    define npy_intp differently."""
    return length


# Test these in Python:
"""
import testcase as tc
tc.func_int(1.0)         # should be OK
tc.func_Py_ssize_t(1.0)  # should raise TypeError
tc.func_npy_intp(1.0)    # depends on Cython 0.29 vs. 3.0
"""
