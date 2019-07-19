"""Setup file contains package metadata information"""

from setuptools import setup, find_packages

VERSION = '0.0.1'

with open('README.md', 'r') as file:
    long_description = file.read()

with open('requirements.txt') as file:
    requirements = file.read().splitlines()

with open('LICENSE') as file:
    license_text = file.read()

setup(
    name='aic',
    version=VERSION,
    author='Lorrx',
    author_email='',
    description='The Avery Image Compiler (AIC) allows that images can be prepared as '
                'Avery-Zweckform labels without loss of quality.',
    long_description=long_description,
    url='https://github.com/lorrx/avery-image-compiler',
    packages=find_packages(),
    install_requires=requirements,
    license=license_text,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
