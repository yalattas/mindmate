pip install -r requirements/dev.txt

python setup.py sdist bdist_wheel

twine upload dist/* -u __token__
