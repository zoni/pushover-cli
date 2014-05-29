import os
import pip
from setuptools import setup
from pip.req import parse_requirements

def read(file):
    """Read file in the given directory and return it's contents"""
    return open(os.path.join(os.path.dirname(__file__), file)).read()


def read_requirements(file):
    """Return a list of requirements from the given requirements file"""
    return [str(ir.req) for ir in parse_requirements(file)]


setup(
    name = "pushover-cli",
    version = "1.0.1",
    author = "Nick Groenen",
    author_email = "nick@groenen.me",
    description = "A simple command-line interface to send Pushover notifications",
    long_description = read('README.rst'),
    license = "MIT",
    keywords = "pushover api message push service phone android iphone",
    url = "https://github.com/zoni/pushover-cli",
    install_requires = read_requirements("requirements.in"),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: Utilities",
        "Topic :: Communications",
        "Topic :: Internet",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    py_modules=['pushover_cli'],
    entry_points={
        'console_scripts': ['pushover = pushover_cli:main']
    },
    include_package_data = True,
)
