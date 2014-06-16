#!/bin/bash

./csv2gff3.py -q 0 -c 1 -b 5 6 -T blasthit --guess-strand -A myatt test-data/blast.tab
