#! usr/bin/env python3

from collections import Counter

import sys

filename = sys.argv[1]

#start base counting at 0 

count = 0
bases = Counter()

#parse and define each line type in the fastq file and count up the number
# of bases in each seq line

for line in open(filename):
    line = line.rstrip()

    if count == 0:
        name = line
        count += 1

    elif count ==1:
        seq = line
        count += 1

    elif count ==2:
        count += 1

    elif count ==3:
        qual = line
        count = 0

        for base in seq:
            bases[base] += 1

print(bases['C'])









