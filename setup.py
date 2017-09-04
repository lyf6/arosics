#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import warnings

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['numpy', 'gdal', 'shapely', 'scikit-image', 'matplotlib', 'geopandas', 'spectral', 'geoarray>=0.5.8',
                'py_tools_ds>=0.4.2', 'plotly'
                # 'pykrige'  # conda install --yes -c conda-forge pykrige
                # 'pyfftw', # conda install --yes -c conda-forge pyfftw=0.10.4 ; \
                # 'basemap', # conda install --yes -c conda-forge basemap; \
                ]

setup_requirements = [
    # TODO(danschef): put setup requirements (distutils extensions, etc.) here
]

test_requirements = ['coverage']

setup(
    name='arosics',
    version='0.4.21',
    description="An Automated and Robust Open-Source Image Co-Registration Software for Multi-Sensor Satellite Data",
    long_description=readme + '\n\n' + history,
    author="Daniel Scheffler",
    author_email='daniel.scheffler@gfz-potsdam.de',
    url='https://gitext.gfz-potsdam.de/danschef/arosics',
    packages=find_packages(),
    include_package_data=True,
    scripts=["bin/arosics_cli.py"],
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='arosics',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)


# check for pyffw
try:
    import pyfftw
except ImportError:
    warnings.warn('You need to install pyfftw manually (see https://pypi.python.org/pypi/pyFFTW) for speeding up '
                  'the computation. It is not automatically installed.') # TODO

# check for basemap
try:
    from mpl_toolkits.basemap import Basemap
except ImportError:
    warnings.warn('You need to install basemap manually if you want to plot maps (see www./matplotlib.org/basemap). '
                  'It is not automatically installed.') # TODO

# check for pykrige
try:
    import pykrige
except ImportError:
    warnings.warn('You need to install pykrige manually if you want to interpolate tie point grids produced by AROSICS '
                  '(see https://github.com/bsmurphy/PyKrige). It is not automatically installed.') # TODO
