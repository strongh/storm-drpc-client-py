import setuptools

version = '0.1.0'

install_requires = [
    'thrift',
    'repoze.lru'
]

setuptools.setup(
    name='storm-drpc-client',
    version=version,
    license='LICENSE.html',
    description='Simple pythonic interface around thrift-generated DRPC client.',
    long_description=open('README.rst').read(),
    author='Homer Strong',
    author_email='homer.strong@gmail.com',
    url='https://github.com/strongh/storm-drpc-client',
    platforms='any',
    packages=['storm'],
    zip_safe=True,
    verbose=False,
    install_requires=install_requires,
)
