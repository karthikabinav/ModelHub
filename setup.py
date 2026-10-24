"""ModelHub package setup.

Original setup for the ModelHub research project.
"""

from setuptools import find_packages, setup

setup(
    name="modelhub",
    version="0.1.0",
    description="A simple framework to run LLMs",
    packages=find_packages(),
    python_requires=">=3.10",
)
