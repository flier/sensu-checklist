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
            default='Found file {file} matched patterns; regex /{regex}/',
            type=str,
            help='Message to print'
        )

    def run(self):
        with open(self.options.file, 'r') as f:
            m = re.search(self.options.regex, f.read(), re.MULTILINE | re.DOTALL)

            options = vars(self.options)

            if m:
                options.update(m.groupdict())

                self.ok(self.options.message.format(**options))
            else:
                self.critical(self.options.message.format(**options))

if __name__ == "__main__":
    ContentCheck()