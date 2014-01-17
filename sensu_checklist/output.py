#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'flier'


class Output(object):
    pass


class ConsoleOutput(Output):
    def __init__(self):
        from colorama import init

        init()


class XmlOutput(Output):
    pass


class JsonOutput(Output):
    pass


class YamlOutput(Output):
    pass


SUPPORT_OUTPUTS = {
    'console': ConsoleOutput,
    'xml': XmlOutput,
    'json': JsonOutput,
    'yaml': YamlOutput,
}
