# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='datetime_truncate',
    version='1.0.0',
    url='https://github.com/mediapop/datetime_truncate',
    author='Björn Andersson / Media Pop',
    author_email='bjorn@mediapop.co',
    description='Truncate datetime objects to a set level of precision',
    license='BSD',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=('tests',)),
    package_data={
        '': ['README']
        },
    test_suite='nose.collector',
    tests_require=['nose>=1.2.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
