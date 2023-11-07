from setuptools import find_packages, setup

setup(
    name='DSSS-Exe',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)