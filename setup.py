#!/usr/bin/python
# -*- coding: utf-8 -*-
import ez_setup
ez_setup.use_setuptools()

__author__ = 'Flier Lu <flier.lu@gmail.com>'

from setuptools import setup, find_packages

from sensu_checklist import __name__ as package_name, __version__ as package_version

setup(
    name=package_name,
    version=package_version,
    packages=find_packages(),
    package_data={

    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sensu-checklist = %s.main:run' % package_name
        ]
    },
    test_suite='%s.tests' % package_name,

    install_requires=[
        'pyyaml >= 3.10',
        'colorama >= 0.2.7',
        'jinja2 >= 2.7.2',
        'sensu_plugin >= 0.1.0',
        'kazoo >= 1.3.1',
    ],

    author="Flier Lu",
    author_email="flier.lu@gmail.com",
    description="Template based checklist generator and runner for Sensu",
    license="MIT",
    keywords="sensu checklist monitoring devops",
    url="https://github.com/flier/sensu-checklist",
)
