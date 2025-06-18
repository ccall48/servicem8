from distutils.core import setup

from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()


setup(
    name='servicem8',
    version='0.0.1-dev',
    packages=find_packages(),
    url='https://github.com/ccall48/servicem8',
    license='MIT',
    author='ccall48',
    author_email='',
    maintainer='ccall48 chestm007',
    maintainer_email='',
    description='servicem8 REST API interface',
    long_description=readme,
    py_modules='servicem8',
    install_requires=[
        'certifi==2024.7.4',
        'chardet==3.0.4',
        'idna==3.7',
        'requests==2.32.4',
        'urllib3==2.5.0'
    ],
    entry_points="""
    """,
)