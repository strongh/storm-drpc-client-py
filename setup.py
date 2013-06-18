#!/usr/bin/env python

import setuptools

install_requires = [
    'thrift',
    'repoze.lru'
]

setuptools.setup(
    name = 'storm-drpc-client',
    version = '0.0.3',
    license = 'Apache',
    description = '''Simple pythonic interface around thrift-generated DRPC client.''',
    author = 'Homer Strong',
    author_email = 'homer.strong@gmail.com',
    url = 'https://github.com/strongh/storm-drpc-client',
    platforms = 'any',
    packages = ['storm'],
    zip_safe = True,
    verbose = False,
    install_requires = install_requires,
    # entry_points={
    #     'console_scripts': [
    #         ''
    #     ]
    # },
)
