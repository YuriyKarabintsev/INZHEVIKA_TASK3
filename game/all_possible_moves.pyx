cdef extern from "low-level/cpp_function.cpp" nogil:
    void get_possible_moves(int xchip, int ychip, string direction, int distance, int& result) ;

cdef get_cpp_possible_moves(int xchip, int ychip, string direction, int distance, int& result) nogil:
    return get_possible_moves(xchip, ychip, direction, result)

def cpp_get_possible_moves(int xchip, int ychip, string direction, int distance, results=None):
    cdef int result;

    with nogil:
        result = get_cpp_possible_moves(xchip, ychip, direction, distance, result)

    if results is not None:
        results.extend(result)
