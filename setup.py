#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pytest-contextfixture',
    description='Define pytest fixtures as context managers.',
    long_description=read("README.rst"),
    version='0.1.1',
    author='Andreas Pelme',
    author_email='andreas@pelme.se',
    url='http://github.com/pelme/pytest-contextfixture/',
    py_modules=['pytest_contextfixture'],
    entry_points={'pytest11': ['contextfixtureprovider = pytest_contextfixture']},
    install_requires=['pytest>=2.3.4'],
    classifiers=[
        'Development Status :: 4 - Beta',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: BSD License',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Topic :: Software Development :: Testing'],
)
