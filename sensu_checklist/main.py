#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from sensu_checklist import __name__ as package_name
from sensu_checklist.parser import parse_checklist
from sensu_checklist.output import SUPPORT_OUTPUTS
from sensu_checklist.collector import Collector
from sensu_checklist.runner import run_checklist

__author__ = 'flier'


def parse_cmdline():
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser(prog=package_name)

    parser.add_argument('checklist', metavar='FILE', type=FileType('r'), nargs='+',
                        help='checklist files')

    group = parser.add_argument_group('logging options')

    group.add_argument('-v', '--verbose', dest='logging_level', action='store_const', const=logging.INFO,
                       help='output the verbose information')
    group.add_argument('-d', '--debug', dest='logging_level', action='store_const', const=logging.DEBUG,
                       help='output the debug information')
    group.add_argument('--log-level', dest='logging_level', choices=['ERROR', 'WARNING', 'INFO', 'DEBUG'],
                       default=logging.WARN, help='set root logger level (default: WARNING)')
    group.add_argument('--log-file', dest='logging_file', type=FileType('w'), default='-',
                       help='output the log to file (default: stdout)')

    group = parser.add_argument_group('output options')
    group.add_argument('-t', '--output-type', default='console', nargs=1,
                       choices=SUPPORT_OUTPUTS.keys(),
                       help='output result in type (default: console)')
    group.add_argument('-g', '--generate-config', metavar='FILE', type=FileType('w'),
                       help='generate Sensu config file')

    args = parser.parse_args()

    logging.basicConfig(level=args.logging_level,
                        stream=args.logging_file)

    return args


def run():
    args = parse_cmdline()

    checklists = [parse_checklist(f.read()) for f in args.checklist]

    if args.generate_config:
        args.generate_config.write(checklists.json())
    else:
        output = SUPPORT_OUTPUTS[args.output_type]()
        collector = Collector(output)

        for checklist in checklists:
            run_checklist(checklist, collector)

if __name__ == '__main__':
    run()