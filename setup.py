import os
from setuptools import setup
import pyquant
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyquant",
    version = "0.0.1",
    author = "Seunghun han",
    author_email = "masa4u@gmail.com",
    description = ("."),
    license = "",
    keywords = "",
    # url = "",
    install_requires = ['colorama',
                        'enum34>=1.0.4'],
    packages=['pyquant',
              'pyquant.client',
              'pyquant.convention',
              'pyquant.patterns'
              ],
    # long_description=read('README'),
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)