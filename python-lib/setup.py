"""
https://packaging.python.org/installing/
https://github.com/pypa/sampleproject
"""
import os
from setuptools import setup, find_packages

# TEMP Fix for SSL troubles
# http://stackoverflow.com/questions/27835619/ssl-certificate-verify-failed-error
# https://github.com/mtschirs/quizduellapi/issues/2
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

long_description = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()

setup(
    name='pyquotes',
    author='Maarten Huijsmans',
    author_email='maarten@lukin.be',
    url='http://github.com/lukin0110/quotes',
    license='Apache Software License',
    version='0.0.1',
    description='Small python lib that contains a few quotes of famous people',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    package_data={
        'pyquotes': ['assets/*'],
    },
    test_suite='tests',
)
