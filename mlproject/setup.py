from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = "-e ."

def get_requirments(file_path:str)->list[str]:
    ''' this function will return the list of requirements '''
    requirments = []
    with open (file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

    HYPEN_E_DOT = "-e ."
    if HYPEN_E_DOT in requirments:
        requirments.remove(HYPEN_E_DOT)
    return requirments


setup(
    name="mlproject", 
    version="3.1",
    description="project for mlops",
    author="Manoj",
    author_email="chapalamanojreddy@gmail.com",
    maintainer="Manoj",
    maintainer_email="manoj@example.com",
    url="https://github.com/manoj/mlproject",
    download_url="https://github.com/manoj/mlproject/archive/v3.1.tar.gz",
    packages=find_packages(),
    ## Requirements file are listed in requirements.txt 
    ##   install_requires=["pandas","numpy", "scikit-learn","flask", "gunicorn"]  
    
    install_requires=get_requirments("requirements.txt").read().splitlines()
    
    
    )