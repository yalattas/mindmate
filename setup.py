from setuptools import setup, find_packages

GITHUB_REPO = 'https://github.com/yalattas/mindmate'
setup(
    name='mindmate',
    version='0.0.3',
    author='Yasser Alattas',
    author_email='y.alattas@gmail.com',
    description="MindMate is a command-line tool that leverages the power of AI platforms to offer different use-cases to developers",
    long_description="MindMate is a powerful command-line tool that harnesses the capabilities of state-of-the-art artificial intelligence platforms to offer a wide range of use-cases to developers. With MindMate, developers can easily leverage advanced natural language processing (NLP) and machine learning (ML) functionalities to enable various applications",
    url=GITHUB_REPO,
    download_url=GITHUB_REPO,
    packages=find_packages(),
    keywords=['cli', 'ai', 'nlp', 'ml', 'developers', 'productivity', 'openai'],
    install_requires=[
        'wheel',
        'click>=8.1',
        'openai>=0.27',
        'PyYAML==6',
    ],
    entry_points={
        'console_scripts': [
            'mindmate = mindmate.cli:cli',  # Update with your CLI entry point
        ],
    },
    # reference: https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
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
