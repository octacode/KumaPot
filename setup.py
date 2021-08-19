from setuptools import setup

def readme_file():
    return "SIMPLE TCP LOGGER"

setup(
    name='kumaPot',
    version='1.0.0',
    description='Simple TCP logger HoneyPot',
    long_description=readme_file(),
    author='octacode',
    author_email='kshashwat@usf.edu',
    license='MIT',
    packages=['kumapot'],
    # scripts=['bin/kumapot', 'bin/nanopot.bat']
    zipsafe = False,
    install_requires=[]
)