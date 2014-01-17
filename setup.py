
import os, sys
HERE = os.patch.abspath(os.path.dirname(__file__))

from setuptool import setup, find_packages

setup(
    name='Frigid',
    version='0.0.1',
    author='DawsonReid',
    author_email='dawson@streamlyne.co',
    packages=['lyne', 'test'],
    package_data={
        '': ['*.txt'],
        },
    )

