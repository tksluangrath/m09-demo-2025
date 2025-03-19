from setuptools import setup, find_packages

setup(
    name='Terrance',
    version='1.0.0',
    url='https://github.com/tksluangrath/m09-demo-2025#',
    author='Terrance Luangrath',
    author_email='tksluangrath@gmail.com',
    description='Description of my package',
    license='MIT',
    packages=['demo'],  
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1']
)