from setuptools import setup, find_packages

setup(
    name='pygbm',
    version='0.1.dev1',  # Update to a version without local identifier
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'jupyter',
    ],
    entry_points={
        'console_scripts': [
            'pygbm=pygbm.cli:main',
        ]
    },
    description='A Python package for geometric Brownian motion simulation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Laura Just Fung',
    author_email='lj441@cam.ac.uk',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Physicists",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
)
