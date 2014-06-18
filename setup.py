from setuptools import setup


def long_description():
    from os.path import join, dirname
    import re
    text = open(join(dirname(__file__), 'README.rst')).read()
    return re.split('\n\.\. pypi [^\n]*\n', text, 1)[1]


setup(
    name='optional_import',
    version='1.1',
    py_modules=['optional_import'],
    description='Import something if it exists.',
    long_description=long_description(),
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
