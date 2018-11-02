import io
from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name = 'deton',
    packages=['deton'],
    version = '1.0.0',
    license='BSD',
    author = "Eugene Korniichuk",
    author_email = "nutscracker.ua@gmail.com",
    description = "Better url shortener",
    long_description = readme,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    }
)