#!/bin/sh
# (Re)compile the Cython code.

rm *.c *.so
python setup.py build_ext --inplace
