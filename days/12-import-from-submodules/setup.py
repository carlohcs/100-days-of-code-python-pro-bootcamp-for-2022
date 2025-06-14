# This file is only necessary if the python version is less than 3.3. And it needs of the `setuptools` package to be installed.

from setuptools import setup, find_packages

setup(
    name="my_package",
    packages=find_packages(),
)