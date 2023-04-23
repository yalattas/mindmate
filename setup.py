from setuptools import setup, find_packages

setup(
    name='pygpt',
    author='Yasser Alattas',
    author_email='y.alattas@gmail.com',
    url='https://github.com/yalattas/pygpt',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click>8.1',
        'wheel'
    ],
    entry_points={
        'console_scripts': [
            'pygpt = pygpt.cli:cli',  # Update with your CLI entry point
        ],
    },
)
