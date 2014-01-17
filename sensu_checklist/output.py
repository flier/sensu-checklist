#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import platform

__author__ = 'flier'


class Output(object):
    pass


class ConsoleOutput(Output):
    pass


class ColorConsoleOutput(ConsoleOutput):
    TERM_WITH_COLORS = ['xterm', 'xterm-color', 'xterm-256color', 'linux', 'screen', 'screen-256color', 'screen-bce']

    def __init__(self):
        from colorama import init

        init(wrap=ColorConsoleOutput.is_windows())

    @staticmethod
    def is_windows():
        return platform.system() == 'Windows'

    @staticmethod
    def term_with_colors():
        return ColorConsoleOutput.is_windows() or os.environ.get('TERM') in ColorConsoleOutput.TERM_WITH_COLORS


class XmlOutput(Output):
    pass


class JsonOutput(Output):
    pass


class YamlOutput(Output):
    pass


SUPPORT_OUTPUTS = {
    'console': ColorConsoleOutput if ColorConsoleOutput.term_with_colors() else ConsoleOutput,
    'xml': XmlOutput,
    'json': JsonOutput,
    'yaml': YamlOutput,
}
