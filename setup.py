from setuptools import setup, find_packages

from typing import List

REQUIREMENT_FILE_NAME = 'requirements.txt'
HYPHEN_E_DOT = "-e ."
def get_requirements():
    pass

setup(
    name = "sensor",
    version="0.0.1",
    author="vaibhavthapli",
    author_email="hellovaibt@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)