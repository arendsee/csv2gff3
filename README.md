# csv2gff3.py

Extract info from csv files (such as BLAST output) to build gff3 files

## Example

```
$ cat myfile.tab
#seqid  score  x    x      x      start  end
seq1    9e-30  132  12718  12560  129    293
seq2    9e-24  113  224    75     293    134
$ csv2gff3.py -q 0 -c 1 -b 5 6 -T blasthit --guess-strand -A myatt myfile.tab
seq1    .    blasthit    129    293    9e-30    +    .    myatt
seq2    .    blasthit    134    293    9e-24    -    .    myatt
```

Currently the interface is a little cluncky, in the next version I'll find a simpler solution

Options can be accessed by calling `csv3gff3.py -h`
