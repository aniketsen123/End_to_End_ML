from setuptools import find_packages,setup
from typing import List

HYPEN='-e .'
def get_requiremtns(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN in requirements:
         requirements.remove(HYPEN)

setup(
    name="mlprojects",
    version='0.0.1',
    author="Aniket",
    author_email="aniketdgp5@gmail.com",
    packages=find_packages(),
    install_requires=get_requiremtns('requirements.txt'),

)