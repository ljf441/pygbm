from setuptools import setup, find_packages

setup(
    name='ljf441-pygbm',
    version='0.1.0',  # Update the version here
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'jupyter',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'pygbm=pygbm.cli:main',
        ]
    },
)
