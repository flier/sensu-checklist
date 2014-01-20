#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from sensu_plugin import SensuPluginCheck

__author__ = 'flier'


class ContentCheck(SensuPluginCheck):
    def setup(self):
        self.parser.add_argument(
            '-f',
            '--file',
            required=True,
            type=str,
            help='File to check'
        )
        self.parser.add_argument(
            '-r',
            '--regex',
            required=True,
            type=str,
            help='Regex to matching'
        )
        self.parser.add_argument(
            '-m',
            '--message',
            default='Found %d matching patterns; regex /%s/',
            type=str,
            help='Message to print'
        )

    def run(self):
        with open(self.options.file, 'r') as f:
            m = re.findall(self.options.regex, f.read(), re.MULTILINE | re.DOTALL)

            if m:
                self.ok(self.options.message % (len(m), self.options.regex))
            else:
                self.critical(self.options.message % (0, self.options.regex))

if __name__ == "__main__":
    ContentCheck()