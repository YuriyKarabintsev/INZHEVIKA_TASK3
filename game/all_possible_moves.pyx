from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.utility cimport pair

cdef extern from "low-level/cpp_function.cpp" nogil:
    void get_possible_moves(int xchip, int ychip, string direction, int distance, vector[pair[int, int]]& result) ;

cdef get_cpp_possible_moves(int xchip, int ychip, string direction, int distance, vector[pair[int, int]]& result):
    return get_possible_moves(xchip, ychip, direction, distance, result)

def cpp_get_possible_moves(int xchip, int ychip, string direction, int distance, results=None):
    cdef vector[pair[int, int]] result;

    result = get_cpp_possible_moves(xchip, ychip, direction, distance, result)

    if results is not None:
        results.extend(result)
