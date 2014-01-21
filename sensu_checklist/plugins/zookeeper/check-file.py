#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from kazoo.client import KazooClient

from sensu_plugin import SensuPluginCheck

__author__ = 'flier'


class ZookeeperCheck(SensuPluginCheck):
    def setup(self):
        self.parser.add_argument(
            '--host',
            default='localhost',
            type=str,
            help='Host or IP to connect'
        )
        self.parser.add_argument(
            '-p',
            '--port',
            default=2181,
            type=int,
            help='Port to connect'
        )
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
            default='Connect to zookeeper://{host}:{port}{file}; regex /{regex}/',
            type=str,
            help='Message to print'
        )

    def run(self):
        zk = KazooClient(hosts='%s:%d' % (self.options.host, self.options.port),
                         read_only=True, timeout=3)

        try:
            zk.start()

            content, stats = zk.get(self.options.file)

            m = re.findall(self.options.regex, content, re.MULTILINE | re.DOTALL)

            if m:
                self.ok(self.options.message.format(**vars(self.options)))
            else:
                self.critical(self.options.message.format(**vars(self.options)))
        except Exception as ex:
            self.critical(ex)
        finally:
            zk.stop()

if __name__ == "__main__":
    ZookeeperCheck()