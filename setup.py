from setuptools import setup, find_packages

setup(
    name = 'catcode',
    version = '0.3.0',
    author = 'revival0728',
    description = 'A repository that prints source code in terminal prettier',
    url = 'https://github.com/revival0728/catcode',
    packages = find_packages(),
    license = 'MIT',
    install_requires = [
        'termcolor>=2.0.1'
    ],
    entry_points = {
        'console_scripts': [
            'catcode = catcode.main:CLI'
        ]
    }
)
