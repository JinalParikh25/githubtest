<<<<<<<<< Temporary merge branch 1
from setuptools import find_packages, setup

setup(
    name='DSSS-Exe',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
=========
from setuptools import setup

setup(
    name='DSSS-Exe',
    version='0.0.1',
    packages=[''],
    url='https://github.com/JinalParikh25/githubtest.git',
    license='',
    author='HP',
    author_email='theparikh303@gmail.com',
    description='analytics and reports'

)
>>>>>>>>> Temporary merge branch 2
