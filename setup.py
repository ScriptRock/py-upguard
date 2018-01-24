#!/usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-upguard',
    version='1.0.0',
    description='Python wrapper around the UpGuard API',
    long_description=long_description,
    url='https://github.com/ScriptRock/py-upguard',
    author='UpGuard Customer Success Team',
    author_email='support@upguard.com',
    license='MIT',
    classifiers=[
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='python upguard api',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
