#!/bin/bash

#open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg

[ ! -e "cpp_function.cpp" ] || rm "cpp_function.cpp"

find . -name "*.so" -type f -delete

python3.9 setup.py build_ext -b build

mv *.cpp low-level/