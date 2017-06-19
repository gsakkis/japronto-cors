# -*- coding: utf-8 -*-
"""
    setup
    ~~~~
    Japronto-CORS is a simple extension to Japronto allowing you to support cross
    origin resource sharing (CORS) using a simple decorator.

    :copyright: (c) 2017 by George Sakkis (based on sanic-cors by Ashley Sommer
        and flask-cors by Cory Dolphin).
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'japronto_cors/version.py'), 'r') as f:
    exec(f.read())

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='Japronto-Cors',
    version=__version__,
    url='https://github.com/gsakkis/japronto-cors',
    license='MIT',
    author='George Sakkis',
    author_email='george.sakkis@gmail.com',
    description="A Japronto extension adding a decorator for CORS support. "
                "Based on sanic-cors by Ashley Sommer and flask-cors by Cory Dolphin.",
    long_description=open('README.rst').read(),
    packages=['japronto_cors'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
