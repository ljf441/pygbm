from setuptools import setup, find_packages

setup(
    name='pygbm',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Ensure no trailing commas or unmatched parentheses
        'matplotlib',
    ],  # Correct this section
    entry_points={
        'console_scripts': [
            'pygbm=pygbm.cli:main',
        ]
    },
)
