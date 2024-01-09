from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name='MathsScorePredictor',
    version='0.0.1',
    author='Vidit',
    author_email='vidit01purohit@gmail.com',
    packages=find_packages(),
    intall_requires=get_requirements('requirements.txt'),
)