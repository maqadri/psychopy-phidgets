#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='psychopy-phidgets',
    version='0.1',
    description='Psychopy plugin providing support for Phidgets',
    long_description='',
    url='https://github.com/maqadri/psychopy-phidgets',
    author='Muhammad A. J. Qadri',
    author_email='mqadri@holycross.edu',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GPL3 License',
        'Programming Language :: Python :: 3'
    ],
    keywords='psychopy phidgets',
    packages=['psychopy_rect_area'],
    install_requires=['psychopy'],
    include_package_data=True,
    entry_points={
        'psychopy.hardware': ['phidgets = psychopy_phidgets.hardware.phidgets.py'],
        'psychopy.experiment.components': ['phidgets = psychopy_phidgets.experiment.compoenents.__init__.py']
    },
    zip_safe=False)