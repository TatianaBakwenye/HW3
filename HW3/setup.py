try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import HW3


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='HW3',
    version=HW3.__version__,
    description='Example library',
    author='Arianna_Vanessa_Tatiana',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/icedgarr/bse-demo-2023',
    classifiers=[
        'Programming Language :: Python :: 3.10.7'
    ]
)
