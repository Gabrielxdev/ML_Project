from setuptools import find_namespace_packages, setup 
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file:
        return file.readlines()

setup (
    name="ML_Project",
    version="0.0.1",
    packages=find_namespace_packages(),
    author="Gabriel",
    author_email="leucides123@gmail.com",
    install_requires=get_requirements("requirements.txt")
)