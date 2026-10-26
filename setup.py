from setuptools import find_packages, setup

setup(
    name="modelhub",
    version="0.1.0",
    description="ModelHub: a simple framework to run any LLMs",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["torch"],
)
