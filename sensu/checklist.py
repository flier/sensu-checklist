#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'flier'


def parse_cmdline():
    from argparse import ArgumentParser

    parser = ArgumentParser()

    args = parser.parse_args()


def run():
    args = parse_cmdline()

if __name__ == '__main__':
    run()