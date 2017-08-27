# -*-coding:utf-8-*-

from setuptools import setup

setup(
    name='offline_sandbox',
    version='1',
    packages=['.', ],
    url='https://github.com/jadolg/offline_sandbox',
    license='MIT',
    author='Jorge Alberto Díaz Orozco',
    author_email='diazorozcoj@gmail.com',
    description='Decorator to return a default value for a function when offline',
    long_description=open("README.md", "r").read()
)
