#!/usr/bin/env python3

import argparse
import sys

def _parser(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        help='input csv file (default STDIN)',
        type=argparse.FileType('r'),
        nargs='?',
        default=sys.stdin,
        metavar='FILE'
    )
    parser.add_argument(
        '-q', '--seqid',
        help='csv column corresponding to gff3 column 1',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-Q', '--seqids',
        help='set all seqids to this value',
        metavar='STR',
        default='unknown'
    )
    parser.add_argument(
        '-r', '--source',
        help='csv column corresponding to gff3 column 2',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-R', '--sources',
        help='set all source to this value',
        metavar='STR',
        default='unknown'
    )
    parser.add_argument(
        '-t', '--type',
        help='csv column corresponding to gff3 column 3',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-T', '--types',
        help='set all type to this value',
        metavar='STR',
        default='unknown'
    )
    parser.add_argument(
        '-s', '--start',
        help='csv column corresponding to gff3 column 4',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-e', '--end',
        help='csv column corresponding to gff3 column 5',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-c', '--score',
        help='csv column corresponding to gff3 column 6',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-C', '--scores',
        help='set all score to this value',
        metavar='STR',
        default='.'
    )
    parser.add_argument(
        '-d', '--strand',
        help='csv column corresponding to gff3 column 7',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-D', '--strands',
        help='set all strand to this value',
        metavar='STR',
        default='.'
    )
    parser.add_argument(
        '--guess-strand',
        help="'+' if end>start, '-' if start>end",
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-p', '--phase',
        help='csv column corresponding to gff3 column 8',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-P', '--phases',
        help='set all phase to this value',
        metavar='STR',
        default='.'
    )
    parser.add_argument(
        '-a', '--attribute',
        help='csv column corresponding to gff3 column 9',
        metavar='INT',
        type=int
    )
    parser.add_argument(
        '-A', '--attributes',
        help='set all attribute to this value',
        metavar='STR',
        default='.'
    )
    parser.add_argument(
        '-n', '--attr-name',
        help='the name given to all attributes (e.g. query)',
        metavar='STR',
        default=''
    )
    args = parser.parse_args()

def get_gff3(args):
    pass

if __name__ == '__main__':

    args = _parser()

    gff3 = get_gff3(args)

    for line in gff3:
        print('\t'.join(line))
