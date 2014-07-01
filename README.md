# csv2gff3.py

Extract info from csv files (such as BLAST output) to build gff3 files

## Example

```
$ cat myfile.tab
#seqid  score  x    x      x      start  end
seq1    9e-30  132  12718  12560  129    293
seq2    9e-24  113  224    75     293    134
$ csv2gff3.py -sc {0} blastn . {5} {6} {1} . . 'hit({3}..{4})' -i test-data/blast.tab
seq1    .    blasthit    129    293    9e-30    +    .    myatt
seq2    .    blasthit    134    293    9e-24    -    .    myatt
```

The argument -c takes one value for each of the nine columns of a gff file. Columns from the csv file can be accessed by bracketed numbers. Values with spaces or other illegal characters must be quoted.

Options can be accessed by calling `csv3gff3.py -h`
