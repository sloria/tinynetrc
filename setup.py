# -*- coding: utf-8 -*-
import re
from setuptools import setup

EXTRAS_REQUIRE = {
    'tests': ['pytest'],
    'lint': [
        'flake8==3.9.2',
    ],
}
EXTRAS_REQUIRE['dev'] = (
    EXTRAS_REQUIRE['tests'] + EXTRAS_REQUIRE['lint'] + ['tox', 'konch']
)


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='tinynetrc',
    version=find_version('tinynetrc.py'),
    description='Read and write .netrc files.',
    long_description=read('README.rst'),
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/tinynetrc',
    install_requires=[],
    extras_require=EXTRAS_REQUIRE,
    license='MIT',
    zip_safe=False,
    keywords='netrc posix',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    py_modules=['tinynetrc'],
)
