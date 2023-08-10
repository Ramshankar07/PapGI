from setuptools import setup, find_packages

setup(
    name='papGI',
    version='1.0',
    author='ram',
    author_email='picographer0214@gmail.com',
    description='Autonomous agent for extracting summaries from research papers',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'nltk',
        'beautifulsoup4',
    ],
)