from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

    setup(
    name="mlproject",
    version="0.0.1",
    description="End-to-end ML project with MLOps practices",
    author="Manoj",
    author_email="chapalamanojreddy@gmail.com",
    url="https://github.com/manoj/mlproject",
    download_url="https://github.com/manoj/mlproject/archive/v3.1.tar.gz",

    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ##   Requirements file are listed in requirements.txt 
    ##   install_requires=["pandas","numpy", "scikit-learn","flask", "gunicorn"]  
    install_requires=get_requirements("requirements.txt"),
)
