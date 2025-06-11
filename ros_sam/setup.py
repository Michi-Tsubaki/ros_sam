#!/usr/bin/env python3

from setuptools import setup, find_packages
from pathlib import Path

with open(Path(__file__).parent / "requirements.txt") as f:
    pip_dependencies = [line.strip() for line in f if line.strip()]

setup(
    name='ros_sam',
    version='0.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=pip_dependencies,
)
