from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirement(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(file_path)as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","")for req in requirement]

        if HYPEN_E_DOT in requirements:
            requirement.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author='Aravind',
    author_email= 'aravind.legacy.kps@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)