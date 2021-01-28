#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: elfin-2020
# @Time: 2021/1/28 9:37
# project: confusion

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="confusion",
    version="1.0.0",
    description='A confusion matrix display project for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/firstelfin/Confusion",
    author='firstelfin',
    classifiers=[
        "Natural Language :: English",
        "Natural Language :: Chinese(Simplified)",
        "Natural Language :: Chinese(Traditional)",
        "Programming Language :: python :: 3",
    ],
    keywords='ConfusionMatrix, Display',
    package_dir={'': 'confusion'},
    packages=find_packages(where='confusion'),
    py_modules=["display", "__init__"],
    python_requires="~=3.6",
    install_requires=["sklearn", "matplotlib", "seaborn", "pandas"],
    entry_points={
        'console_scripts': [
            'confusionDraw=confusion.display:main'
        ],
    },
)
