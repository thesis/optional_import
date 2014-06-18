from ez_setup import use_setuptools
use_setuptools()

from os.path import join, dirname
from setuptools import setup


setup(
    name='optional_import',
    version='1.0',
    py_modules=['optional_import'],
    description='Optional imports in Python',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    url='https://github.com/cardforcoin/optional_import',
    license='MIT',
    test_suite='nose.collector',
    tests_require=[
        'nose==1.3.3',
        'sure==1.2.7',
        # workaround for https://github.com/gabrielfalcao/sure/pull/60
        # undeclared requirements of `sure`
        'mock',
        'six',
    ],
)
