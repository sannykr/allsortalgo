from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='allsortalgo',
    version='0.0.1',
    description='Python package containing implementation of all sorting algorithms',
    long_description=readme,
    author='Sanny Kumar',
    author_email='sanny.iitkgp@gmail.com',
    url='https://github.com/sannykr/allsortalgo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

