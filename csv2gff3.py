#!/usr/bin/env python3

import argparse
import sys

__version__ = "0.0.1"

def _parser():
    parser = argparse.ArgumentParser(
        prog='csv2gff3',
        usage='csv2gff3 <options> FILE',
        description='Make gff3 files using data in csv files'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s {}'.format(__version__))
    parser.add_argument(
        '-c', '--cols',
        nargs=9,
        help='replacement string'
    )
    parser.add_argument(
        '-i', '--infile',
        help='input csv file (default STDIN)',
        type=argparse.FileType('r'),
        nargs='?',
        default=sys.stdin,
        metavar='FILE'
    )
    parser.add_argument(
        '-d', '--delimiter',
        help='csv delimiter (TAB by default)',
        default='\t',
        metavar='STR'
    )
    parser.add_argument(
        '-s', '--guess-strand',
        help='guess the strand',
        action='store_true',
        default=False
    )
    args = parser.parse_args()
    return(args)

def err(msg):
    print(msg, file=sys.stderr)
    raise SystemExit

def _process_line(args, inrow):

    try:
        out = [s.format(*inrow) for s in args.cols]
    except IndexError:
        err('Wrong number of columns in input csv')

    if args.guess_strand:
        try:
            start, end = out[3], out[4]
            out[3:5] = [x for x in sorted([int(start), int(end)])]
        except ValueError:
            err('Start and stop positions must be integers')
        if int(end) > int(start):
            out[6] = '+'
        elif end < start:
            out[6] = '-'

    return([str(x) for x in out])

def get_gff3(args):
    for line in args.infile:
        line = line.strip()
        if line[0] == '#':
            continue
        inrow = line.split(args.delimiter)
        outrow = _process_line(args, inrow)
        yield outrow


if __name__ == '__main__':
    args = _parser()
    gff3 = get_gff3(args)
    for line in gff3:
        print('\t'.join(line))
