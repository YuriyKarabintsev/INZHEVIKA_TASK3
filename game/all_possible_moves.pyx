from libcpp.vector cimport vector
from libcpp.utility cimport pair
from libcpp.string cimport string

cdef extern from "low-level/cpp_function.cpp" nogil:
    void get_possible_moves(
        int xchip, int ychip, const string& direction,
        int distance, vector[pair[int, int]]& result
    );

cdef get_cpp_possible_moves(
        int xchip, int ychip, const string& direction,
        int distance, vector[pair[int, int]]& result
):
    return get_possible_moves(xchip, ychip, direction, distance, result)

def cpp_get_possible_moves(int xchip, int ychip, str direction, int distance, results=None):
    cdef bytes string_ = direction.encode("utf-8")
    cdef vector[pair[int, int]] result;

    get_cpp_possible_moves(xchip, ychip, string_, distance, result)

    if results is not None:
        results.extend(result)
