from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourseFiles = ["all_possible_moves.pyx"]

ext_modules = [
    Extension("all_possible_moves", sourseFiles)
]

setup(
    name="test cython function",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules
)