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
            default='Connect to telnet://{host}:{port}; regex /{regex}/',
            type=str,
            help='Message to print'
        )

    def run(self):
        telnet = telnetlib.Telnet()

        try:
            #telnet.set_debuglevel(3)
            telnet.open(self.options.host, self.options.port)

            telnet.write(self.options.command.decode('string_escape'))

            m = re.search(self.options.regex, telnet.read_all(), re.MULTILINE | re.DOTALL)

            if m:
                self.ok(self.options.message.format(**vars(self.options)))
            else:
                self.critical(self.options.message.format(**vars(self.options)))
        except socket.error as ex:
            self.critical(ex)
        finally:
            telnet.close()

if __name__ == "__main__":
    TelnetCheck()