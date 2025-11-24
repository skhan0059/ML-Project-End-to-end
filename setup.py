from setuptools import find_packages, setup
from typing import List

hyphone = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the lists of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements = [req.strip() for req in requirements if req.strip()]
        if hyphone in requirements:
            requirements.remove(hyphone)
    return requirements


setup(
    name='mlproject',
    version='0.01',
    author='skhan',
    author_email='skhan0827779@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.12',
)