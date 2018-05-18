import setuptools
import glob
import os

required = [
    "requests",
    "pandas",
    "arrow",
    "socketIO-client-nexus"
]

setuptools.setup(name='iex-api-python',
                 version="0.0.3",
                 description='Fetch data from the IEX API',
                 long_description=open('README.md').read().strip(),
                 author='Daniel E. Cook',
                 author_email='danielecook@gmail.com',
                 url='http://www.github.com/danielecook/iex-api-python',
                 packages=['iex'],
                 install_requires=required,
                 keywords=['finance', 'stock', 'market', 'market-data', 'IEX', 'API'],
                 license='MIT License',
                 zip_safe=False)
