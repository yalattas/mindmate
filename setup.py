from mindmate import meta
from setuptools import setup, find_packages
try:
    # For pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # For pip <= 9.0.3
    from pip.req import parse_requirements

GITHUB_REPO = 'https://github.com/yalattas/mindmate'

# Function to parse requirements recursively
def parse_requirements_file(file_path):
    requirements = parse_requirements(file_path, session=False)
    sub_requirements = []
    for req in requirements:
        if req.req:
            sub_requirements.append(str(req.req))
    return sub_requirements

# Parsing requirements recursively from requirements.txt file
install_packages = parse_requirements_file('requirements.txt')

# Reading README.md file
with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme_contents = readme_file.read()

setup(
    name='mindmate',
    version=meta.VERSION,
    author='Yasser Alattas',
    author_email='y.alattas@gmail.com',
    description="MindMate is a command-line tool that leverages the power of AI platforms to offer different use-cases to developers",
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    url=GITHUB_REPO,
    download_url=GITHUB_REPO,
    packages=find_packages(),
    platforms='any',
    keywords=['cli', 'ai', 'nlp', 'ml', 'developers', 'productivity', 'openai', 'directory', 'manifest'],
    install_requires=[
        install_packages
    ],
    entry_points={
        'console_scripts': [
            'mindmate = mindmate.cli:cli',  # Update with your CLI entry point
        ],
    },
    # reference: https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development',
        'Topic :: System :: System Shells',
        'Topic :: Utilities',
    ],
    # platforms=[],
    license='LGPL-2.1 license',
)
