#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

__author__ = 'flier'

log = logging.getLogger('parser')


def parse_checklist(text):
    import yaml

    checklist = yaml.load(text)