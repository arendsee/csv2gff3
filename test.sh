#!/bin/bash
./csv2gff3.py --guess-strand -c {0} 'blastn' . {5} {6} . . . . -i test-data/blast.tab
