#!/usr/bin/env python

from setuptools import setup

setup(name='clitv',
      version='0.1.0',
      description="Utility for watching videos from the terminal",
      author='Michaël Malter',
      url='https://github.com/mmalter/clitv',
      packages=['clitv'],
      package_dir={'clitv': 'clitv'},
      scripts=['bin/clitv', 'bin/clitv-youtube'],
      python_requires='>=3.8'
      install_requires=["docopt", "urwid"],
      data_files=[('/etc', ['conf/clitv'])])
