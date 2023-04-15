#!/bin/bash

[ ! -e "cpp_function.cpp" ] || rm "cpp_function.cpp"

find . -name "*.so" -type f -delete

python3.9 setup.py build_ext -b build

mv *.cpp low-level/