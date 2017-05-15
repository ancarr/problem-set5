#! /usr/bin/env python3

from collections import Counter

counts = Counter()

import sys

filename = sys.argv[1]

#count the number of times each chrom appears in associated with
#an interval, excluding the first line 

for line in open(filename):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chrom = fields[0]
    counts[chrom] += 1

#store chrom,count as count,chrom, sort, reverse
#access the first line of count, chrom and only print chrom 

for chrom, count in counts.items():
    sortme = [(v,k) for k,v in counts.items()]
    sortme.sort()
    sortme.reverse()
    print(sortme[0][1])

