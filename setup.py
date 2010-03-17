from setuptools import setup, find_packages

setup(
    name = 'mfstorage',
    version = '0.1',
    url = 'http://github.com/samueladam/django-mfstorage',
    license = 'BSD',
    description = 'Multi Folder FileSystem Storage for Django',
    author = 'Samuel Adam',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
