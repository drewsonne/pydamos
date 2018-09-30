from setuptools import setup, find_packages

setup(
    name='pydamos',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/drewsonne/pydamos',
    license='LGPLv3',
    author='Drew J. Sonne',
    author_email='drew.sonne@gmail.com',
    description='Python library to interact with DĀMOS ',
    install_requires=[
        'requests',
        'jsonstruct'
    ],
    python_requires='>3.6',

)
