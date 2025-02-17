from setuptools import setup, find_packages

setup(
    name='FEBE1004DATASETS',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
    ],
    package_data={
        '': ['data/*.csv'],
    },
    author='Isaiah Chiraira',
    author_email='Isaiah Chiraira',
    description='A package to load different datasets as dataframes',
    url='https://github.com/yourusername/your_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',  
)
