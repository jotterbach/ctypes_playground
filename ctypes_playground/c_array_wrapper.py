from ctypes.util import find_library
import numpy as np
import ctypes

print "Looking up the compiled library: "
print find_library('c_array.so')

# loading library
_func = ctypes.CDLL(find_library('c_array.so'))

# define return and argument types of shared library func
_func.get_array_ptr.restype = ctypes.POINTER(ctypes.c_int)
_func.get_array_ptr.argtypes = (ctypes.c_int, ctypes.c_int)

_func.int_return.restype = ctypes.c_int
_func.int_return.argtypes = [ctypes.c_int]


def get_array_ptr_test(low, length):
    global _func
    result = _func.get_array_ptr(ctypes.c_int(low), ctypes.c_int(length))
    return np.ctypeslib.as_array(result, shape=(length,))


def integer_return_test(x):
    global _func
    result = _func.int_return(ctypes.c_int(x))
    return int(result)

if __name__ == "__main__":
    print "\nCalling c function that returns c array and convert to numpy"
    arr = get_array_ptr_test(1, 4)
    print type(arr), arr

    print "\nCalling simple integer c function"
    print integer_return_test(4)

