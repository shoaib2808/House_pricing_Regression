from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    with open(file_path,"r") as f:
        requirements=f.readlines()
        for i in range(len(requirements)):
            requirements[i].replace("\n","")

        if(HYPEN_E_DOT in requirements):
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(

    name ="RegressorProject",
    version="0.0.1",
    author="Shoaib khan",
    author_email="sk582511@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)