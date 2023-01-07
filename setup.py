#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
setup(name='psychopy-phidgets',
    version='0.1.1',
    description='Psychopy plugin providing support for Phidgets',
    long_description='',
    url='https://github.com/maqadri/psychopy-phidgets',
    author='Muhammad A. J. Qadri',
    author_email='mqadri@holycross.edu',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    keywords='psychopy phidgets',
    packages=['psychopy_phidgets','psychopy_phidgets.hardware','psychopy_phidgets.experiment.components.phidgets'],
    install_requires=['psychopy'],
    include_package_data=True,
    entry_points={
        'psychopy.hardware': ['PhidgetOutputComponent = psychopy_phidgets.hardware.phidgets:PhidgetOutputComponent'],
        'psychopy.experiment.components': ['PhidgetRelayComponent = psychopy_phidgets.experiment.components.phidgets.phidgets:PhidgetRelayComponent']
    },
    zip_safe=False)