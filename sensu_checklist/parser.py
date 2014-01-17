#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'flier'


def parse_checklist(text):
    import yaml

    checklist = yaml.load(text)