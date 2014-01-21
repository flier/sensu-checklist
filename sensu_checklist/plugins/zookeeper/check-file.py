#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import socket

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

            options = vars(self.options)
            options.update({
                'system.hostname': socket.gethostname()
            })

            if self.options.regex:
                content, stats = zk.get(self.options.file)

                options['stats'] = stats

                m = re.search(self.options.regex, content, re.MULTILINE | re.DOTALL)

                if m:
                    options.update(m.groupdict())

                    self.ok(self.options.message.format(**options))
                else:
                    self.critical(self.options.message.format(**options))
            elif zk.exists(self.options.file):
                self.ok(self.options.message.format(**options))
            else:
                self.critical(self.options.message.format(**options))
        except Exception as ex:
            self.critical(ex)
        finally:
            zk.stop()

if __name__ == "__main__":
    ZookeeperCheck()