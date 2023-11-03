#   python setup.py build_ext --inplace
#   rm -rf build

# Note from Cython docs: When using setuptools, import it before Cython.

#from setuptools import setup
from distutils.core import setup

from Cython.Build import cythonize

import numpy as np


setup(
	name = "testcase",
	ext_modules = cythonize("testcase.pyx"),
	include_dirs = [np.get_include()],
	)
