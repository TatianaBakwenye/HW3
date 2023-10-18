try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import HW3_library


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='HW3_library',
    version=HW3_library.__version__,
    description='HW3_library',
    author='Arianna_Vanessa_Tatiana',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/TatianaBakwenye/HW3.git',
    classifiers=[
        'Programming Language :: Python :: 3.10.7'
    ]
)
