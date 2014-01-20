#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

from sensu_plugin import SensuPluginCheck

__author__ = 'flier'


class ConnectCheck(SensuPluginCheck):
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
            required=True,
            type=int,
            help='Port to check'
        )
        self.parser.add_argument(
            '--family',
            default=socket.AF_INET,
            choices=[socket.AF_INET, socket.AF_INET6, socket.AF_UNIX],
            help="Protocol family"
        )
        self.parser.add_argument(
            '-m',
            '--message',
            default='Connect to tcp://%s:%d',
            type=str,
            help='Message to print'
        )

    def run(self):
        sock = socket.socket(self.options.family, socket.SOCK_STREAM, socket.IPPROTO_IP)
        try:
            sock.connect((self.options.host, self.options.port))

            self.ok(self.options.message % (self.options.host, self.options.port))
        except socket.error:
            self.critical(self.options.message % (self.options.host, self.options.port))
        finally:
            sock.close()

if __name__ == "__main__":
    ConnectCheck()