# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='helloworld',
    version='0.1',
    description='A very boring Python package',
    long_description=readme,
    author='Swaathi Kakarla',
    author_email='swaathi@skcript.com',
    url = 'https://github.com/swaathi/redmon',
    download_url = 'https://github.com/swaathi/redmon/tarball/0.1.2',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
