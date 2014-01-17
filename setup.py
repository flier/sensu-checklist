#!/usr/bin/python
# -*- coding: utf-8 -*-
import ez_setup
ez_setup.use_setuptools()

__author__ = 'Flier Lu <flier.lu@gmail.com>'

from setuptools import setup, find_packages

setup(
    name="sensu-checklist",
    version="0.8",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sensu-checklist = sensu.checklist:run'
        ]
    },
    test_suite='sensu.tests',

    install_requires=[],

    author="Flier Lu",
    author_email="flier.lu@gmail.com",
    description="Template based checklist generator and runner for Sensu",
    license="MIT",
    keywords="sensu checklist monitoring devops",
    url="https://github.com/flier/sensu-checklist",
)