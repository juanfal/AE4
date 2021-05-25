# setup.py
# juanfc 2021-05-18

from setuptools import setup

setup(name='ae4',
    version='0.028',
    description='Evolutionary automaton',
    url='https://github.com/juanfal/AE-4',
    author='Javier Falgueras, Juan Falgueras, Andrés Moya',
    author_email='juanfc@uma.es',
    # license='MIT',
    packages=['ae4'],
    install_requires=[
        'argparse',
        'datetime',
        'functools',
        'matplotlib',
        'numpy',
        'pathlib',
        'subprocess',
        'urllib'
        'xlsxwriter'
    ],
    zip_safe=True
)

