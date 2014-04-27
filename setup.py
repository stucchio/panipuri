#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup(name='Panipuri',
      version='0.1',
      description='Locally cache scraped data.',
      author='Chris Stucchio',
      author_email='stucchio@gmail.com',
      url='https://github.com/stucchio/panipuri',
      packages = find_packages(),
      test_suite = "tests",
     )
