from setuptools import setup, find_packages

setup(
    name='pygbm',
    use_scm_version=True,  # Use setuptools_scm to manage versioning
    setup_requires=['setuptools>=42', 'setuptools_scm'],  # Ensure setuptools_scm is available
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'jupyter',
    ],
    entry_points={
        'console_scripts': [
            'pygbm=pygbm.cli:main',
        ],
    },
    description='A Python package for geometric Brownian motion simulation.',
    long_description=open('README.md').read(),  # Read the long description from your README
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    author='Laura Just Fung',
    author_email='lj441@cam.ac.uk',
    license='MIT',  # Specify your license
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Physicists',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.6',  # Specify the Python version requirement
)
