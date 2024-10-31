from setuptools import setup, find_packages

setup(
    name='your_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Ensure no trailing commas or unmatched parentheses
        'matplotlib',
    ],  # Correct this section
)
