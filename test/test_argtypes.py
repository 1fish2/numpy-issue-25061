import unittest
import testcase as tc

MAX_CINT = int(2**31 - 1)
MAX_CLONG = int(2**63 - 1)


class TestArgTypes(unittest.TestCase):
    def test_func_int(self):
        """func_int() accepts a Python int or float that fits in a C int"""
        assert tc.func_int(13) == 13
        assert tc.func_int(-37) == -37
        assert tc.func_int(MAX_CINT) == MAX_CINT

        assert tc.func_int(13.0) == 13
        assert tc.func_int(13.9) == 13

        with self.assertRaises(OverflowError):
            tc.func_int(MAX_CINT + 1)

        with self.assertRaises(OverflowError):
            tc.func_int(MAX_CLONG)

    def test_func_Py_ssize_t(self):
        """func_Py_ssize_t() accepts a C long, never a float."""
        assert tc.func_Py_ssize_t(13) == 13
        assert tc.func_Py_ssize_t(-37) == -37
        assert tc.func_Py_ssize_t(MAX_CLONG) == MAX_CLONG

        with self.assertRaises(TypeError):
            assert tc.func_Py_ssize_t(13.0)

        with self.assertRaises(OverflowError):
            tc.func_Py_ssize_t(MAX_CLONG + 1)

    def test_func_npy_intp(self):
        """func_npy_intp() accepts a C long, maybe a float depending on Cython
        & numpy versions and maybe other factors."""
        assert tc.func_npy_intp(13) == 13
        assert tc.func_npy_intp(-37) == -37
        assert tc.func_npy_intp(MAX_CLONG) == MAX_CLONG

        with self.assertRaises(TypeError):
            assert tc.func_npy_intp(13.0)

        with self.assertRaises(OverflowError):
            tc.func_Py_ssize_t(MAX_CLONG + 1)
