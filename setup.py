# coding=utf-8
# :bc: Not importing unicode_literals because in Python 2 distutils,
# some values are expected to be byte strings.
from __future__ import absolute_import, division, print_function

from codecs import StreamReader, open
from os.path import dirname, join, realpath

from setuptools import setup

cwd = dirname(realpath(__file__))

##
# Load long description for PyPi.
with open(join(cwd, 'README.rst'), 'r', 'utf-8') as f: # type: StreamReader
    long_description = f.read()


##
# Certain dependencies are optional depending on Python version.
dependencies = [
    'filters',
    'iso3166',
    'language_tags',
    'py-moneyed',
]


##
# Off we go!
setup(
    name        = 'filters-iso',
    description = 'Adds filters for interpreting ISO codes.',
    url         = 'https://filters.readthedocs.io/',

    version = '1.0.0',

    packages = ['filters_iso'],

    # Install package filters into the global registry.
    entry_points = {
        'filters.extensions': [
            'iso = filters_iso',
        ],
    },

    long_description = long_description,

    install_requires = dependencies,

    test_suite    = 'test',
    test_loader   = 'nose.loader:TestLoader',
    tests_require = [
        'nose',
    ],

    data_files = [
        ('', ['LICENSE']),
    ],

    license = 'MIT',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
    ],

    keywords = 'data validation',

    author          = 'Phoenix Zerin',
    author_email    = 'phoenix.zerin@eflglobal.com',
)

