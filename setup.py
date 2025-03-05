'''
The setup.py file is an essential part of packaging anddistributing python projects.
 It is used by setuptools to drfine the configuration 
of your project, such as its metadata, dependencies and more.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements

    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from the file
            lines = file.readlines()

            #process each line
            for line in lines:
                requirement=line.strip()

                #ignore empty line and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('Requirements file not found')

    return requirement_list

setup(
    name = 'Network Security Application',
    version = '0.0.1',
    author = 'Allu Sudharshan Rao',
    author_email = 'allusudharshanrao@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)

