#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import socket

import telnetlib

from sensu_plugin import SensuPluginCheck

__author__ = 'flier'


class TelnetCheck(SensuPluginCheck):
    def setup(self):
        self.parser.add_argument(
            '--host',
            default='localhost',
            type=str,
            help='Host or IP to check'
        )
        self.parser.add_argument(
            '-p',
            '--port',
            default=telnetlib.TELNET_PORT,
            type=int,
            help='Port to check'
        )
        self.parser.add_argument(
            '-c',
            '--command',
            required=True,
            type=str,
            help='Command to sending'
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
            default='Connect to telnet://%s:%d; regex /%s/',
            type=str,
            help='Message to print'
        )

    def run(self):
        telnet = telnetlib.Telnet()

        try:
            #telnet.set_debuglevel(3)
            telnet.open(self.options.host, self.options.port)

            telnet.write(self.options.command.decode('string_escape'))

            m = re.findall(self.options.regex, telnet.read_all(), re.MULTILINE | re.DOTALL)

            if m:
                self.ok(self.options.message % (self.options.host, self.options.port, self.options.regex))
            else:
                self.critical(self.options.message % (self.options.host, self.options.port, self.options.regex))
        except socket.error:
            self.critical(self.options.message % (self.options.host, self.options.port, self.options.regex))
        finally:
            telnet.close()

if __name__ == "__main__":
    TelnetCheck()