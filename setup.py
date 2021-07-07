"""Setup script for v2e."""

import setuptools
from setuptools import setup, find_packages

classifiers = """
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Software Development :: Libraries :: Python Modules
License :: OSI Approved :: MIT License
"""

setup(
    name='v2e',
    version="1.4.2",
    description='Generates synthetic DVS events from conventional video',

    author="Tobi Delbruck, Yuhuang Hu, Zhe He",
    author_email="yuhu@ini.uzh.ch",

    packages=find_packages(include=['v2ecore', 'v2e.*']),
    url='https://github.com/SensorsINI/v2e',
    scripts=["v2e.py"],
    install_requires=[
        'numpy','argparse', 'tqdm', 'opencv-python', 'h5py', 'torch', 'torchvision', 'numba', 'Gooey'
    ],
    entry_points = {
        'console_scripts': ['v2e=v2e:main']
    },

    classifiers=list(filter(None, classifiers.split('\n'))),
)
