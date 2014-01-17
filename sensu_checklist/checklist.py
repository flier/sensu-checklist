#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

__author__ = 'flier'

log = logging.getLogger('checklist')


class Check(object):
    pass


class Metric(object):
    pass


class CheckList(object):
    def __init__(self):
        self.checks = {}
        self.metrics = {}
