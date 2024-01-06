# USED TO BUILD YOUR APPLICATION AS PACKAGE

from setuptools import find_packages,setup
from typing import List

hypenedot = '-e .'
def getRequirements(filePath:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(filePath) as fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
    if hypenedot in requirements:
        requirements.remove(hypenedot)
        

setup(
    name='MLproject',
    version='0.0.1',
    author='akash',
    packages=find_packages(),
    install_requires = getRequirements('requirements.txt')
)