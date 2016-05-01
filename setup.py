#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datahub

ver = sys.version_info

if ver.major != 3 or ver.minor < 5:
    print("You must use at least python 3.5.0.")
    print("Using a tool like 'pyenv' may be advisable if your system python is too old.")
    sys.exit(1)

try:
    from setuptools import setup, find_packages
except ImportError:
    print("You must have setuptools installed to proceed.")
    sys.exit(1)

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md', 'r') as history_file:
    history = history_file.read()

requirements = [
    'lxml',
    'tornado',
    'pyzmq'
]

test_requirements = [
    'pytest>=2.9'
]

setup(
    name='datahub',
    version=datahub.__version__,
    description="An events and data record broker application",
    long_description=readme + '\n\n' + history,
    author="Dan Sloan",
    author_email='dan@dansloan.org',
    url='https://github.com/dansdans/datahub',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'datahubctl = datahub.ctl:main',
            'dh-eventserver = datahub.eventserver:main',
            'dh-filewatcher = datahub.filewatcher:main',
            'dh-httpserver = datahub.httpserver:main'
        ]
    },
    license="ISCL",
    zip_safe=False,
    keywords='datahub data hub broker zmq events',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    tests_require=test_requirements
)
