#!/usr/bin/env python3

import argparse
import sys

def _parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'infile',
        help='input csv file (default STDIN)',
        type=argparse.FileType('r'),
        nargs='?',
        default=sys.stdin,
        metavar='FILE'
    )
    parser.add_argument(
        '--delimiter',
        help='csv delimiter (TAB by default)',
        default='\t',
        metavar='STR'
    )
    parser.add_argument(
        '-q', '--seqid',
        help='csv column corresponding to gff3 column 1',
        metavar='INT',
        type=int,
        default=-1
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
        type=int,
        default=-1
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
        type=int,
        default=-1
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
        type=int,
        default=-1
    )
    parser.add_argument(
        '-e', '--end',
        help='csv column corresponding to gff3 column 5',
        metavar='INT',
        type=int,
        default=-1
    )
    parser.add_argument(
        '-c', '--score',
        help='csv column corresponding to gff3 column 6',
        metavar='INT',
        type=int,
        default=-1
    )
    parser.add_argument(
        '-d', '--strand',
        help='csv column corresponding to gff3 column 7',
        metavar='INT',
        type=int,
        default=-1
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
        type=int,
        default=-1
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
        type=int,
        default=-1
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
    return(args)

def _process_line(args, inrow):
    outrow = ['.'] * 9

    if args.seqid >= 0:
        outrow[0] = inrow[args.seqid]
    elif args.seqids:
        outrow[0] = args.seqids

    if args.source >= 0:
        outrow[1] = inrow[args.source]
    elif args.sources:
        outrow[1] = args.sources

    if args.type >= 0:
        outrow[2] = inrow[args.type]
    elif args.types:
        outrow[2] = args.types

    try:
        start, end = inrow[args.start], inrow[args.end]
    except IndexError:
        print('You must provide bounds for the feature', file=sys.stderr)
        raise SystemExit

    outrow[3], outrow[4] = sorted([start, end])

    if args.score >= 0:
        outrow[5] = inrow[args.score]

    if args.strand >= 0:
        outrow[6] = inrow[args.strand]
    elif args.guess_strand:
        if end > start:
            outrow[6] = '+'
        elif end < start:
            outrow[6] = '-'
    elif args.strands:
        outrow[6] = args.strands

    if args.phase >= 0:
        outrow[7] = inrow[args.phase]
    elif args.phases:
        outrow[7] = args.phases

    if args.attribute >= 0:
        outrow[8] = inrow[args.attributes]
    elif args.attributes:
        outrow[8] = args.attributes
    if args.attr_name and (args.attribute or args.attributes):
        outrow[8] = "{}={}".format(args.attr_name, outrow[8])

    return(outrow)

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
