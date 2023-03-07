#!/bin/bash

[ ! -e "cpp_function.cpp" ] || rm "cpp_function.cpp"

find . -name "*.so" -type f -delete

python3.10 setup.py build_ext -b build

mv *.cpp low-level/