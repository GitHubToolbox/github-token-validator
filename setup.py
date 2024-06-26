# setup.py

"""Setup script."""

from setuptools import setup

with open('requirements.txt', 'r', encoding='UTF-8') as f:
    required: list[str] = f.read().splitlines()

with open("README.md", 'r', encoding='UTF-8') as f:
    long_description: str = f.read()

setup(
    name='wolfsoftware.github-token-validator',
    version='0.1.3',
    packages=['wolfsoftware.github_token_validator'],
    entry_points={
        'console_scripts': [
            'gtv=wolfsoftware.github_token_validator.main:main',
        ],
    },
    author='Wolf Software',
    author_email='pypi@wolfsoftware.com',
    description='A tool to validate GitHub Tokens.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/GitHubToolbox/github-token-validator',
    project_urls={
        ' Source': 'https://github.com/GitHubToolbox/github-token-validator',
        ' Tracker': 'https://github.com/GitHubToolbox/github-token-validator/issues/',
        ' Documentation': 'https://github.com/GitHubToolbox/github-token-validator',
        ' Sponsor': 'https://github.com/sponsors/WolfSoftware',
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
    install_requires=required,
)
