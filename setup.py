from setuptools import setup

setup(
    name = 'labgeeks-horae',
    version = '1.0',
    license = 'Apache',
    url = 'http://github.com/abztrakt/labgeeks_horae',
    description = 'The schedule app for the labgeeks suite of student staff management tools.',
    author = 'Craig Stimmel',
    packages = ['labgeeks_horae',],
    install_requires = [
        'setuptools',
        'South==0.7.3',
        'labgeeks-people',
        'labgeeks-chronos',
    ],
)
