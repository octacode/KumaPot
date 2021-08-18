from setuptools import setup

def readme_file():
    with open('Readme.rst') as readme_file:
        data = readme_file;
    return data

setup(
    name='KumarPot',
    version='1.0.0',
    description='Simple TCP logger HoneyPot',
    long_description=readme_file(),
    author='octacode',
    author_email='kshashwat@usf.edu',
    license='MIT',
    packages=[]
)