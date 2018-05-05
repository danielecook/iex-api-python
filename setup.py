import setuptools


setuptools.setup(name='iex-api-python',
                 version=1.0,
                 description='Fetch data from the IEX API',
                 long_description=open('README.md').read().strip(),
                 author='Daniel E. Cook',
                 author_email='danielecook@gmail.com',
                 url='http://www.github.com/danielecook/iex-api-python',
                 py_modules=['iex'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='IEX API finance stock symbol')
