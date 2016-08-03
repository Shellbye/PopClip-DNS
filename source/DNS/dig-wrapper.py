#!/usr/bin/python

import os
import re
import subprocess
import sys


NAMESERVER = os.environ.get('POPCLIP_OPTION_NAMESERVER', '8.8.8.8')
TEXT = os.environ['POPCLIP_TEXT']
RE_IPV4_ADDR = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')


def collect_result(options):
    for nameserver in NAMESERVER.split(','):
        nameserver.strip()
        args = ['/usr/bin/dig']
        args.extend(options)
        args.extend([
            TEXT.strip(), '@{0}'.format(nameserver.strip())])
        try:
            output = subprocess.check_output(args)
        except subprocess.CalledProcessError:
            continue
        yield output.strip('. \t\n\r')


def main():
    if RE_IPV4_ADDR.search(TEXT):
        results = collect_result(['+short', '-x'])
    else:
        results = collect_result(['+short'])
    sys.stdout.write(' '.join(set(r for r in results if r)))


if __name__ == '__main__':
    main()
