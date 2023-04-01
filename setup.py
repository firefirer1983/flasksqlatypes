#!/usr/bin/env python

"""A setuptools based setup module for auth_backend"""
import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "requirements.txt"), "r", encoding="utf-8") as requirements:
    requires = [requirement.strip() for requirement in requirements]
    
    
setup(
    name="flasksqlatypes",
    version="1.0.0",    
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    author="zhang.xuyi",
    author_email='zhang.xuyi@ikasinfo.com',
    packages=find_packages(include=['flasksqla']),
    entry_points={
        'console_scripts': [],
    },
    install_requires=requires,
    include_package_data=True,
    license="Apache Software License 2.0",
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    ext_modules=[],
    keywords='flasksqlatypes',
)
