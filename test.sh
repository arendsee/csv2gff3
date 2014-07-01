#!/bin/bash
./csv2gff3.py -sc {0} blastn . {5} {6} {1} . . 'hit({3}..{4})' -i test-data/blast.tab
