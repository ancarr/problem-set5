#! /usr/bin/env python3

import sys
filename = sys.argv[1]

from collections import Counter
from pysam import AlignmentFile

counts = 0
strands = Counter()
mismatches = Counter()

bamfile = AlignmentFile(filename)


def stranded_alignements(bamfile):

    for record in bamfile:
        strand = record.flag
        strands[strand] += 1

    for strand, count in strands.items():

        if strand == 0:
            print("positive strand alignments =" , count)
        if strand == 16:
            print("negative strand alignment =" , count)

stranded_alignments(bamfile)

def aligned_mismatches(bamfile):

    for record in bamfile:
        nm = record.get_tag("NM")
        mismatches[nm] += 1

    for nm, count in mismatches.items():

        if nm == 0:
            print("alignments with no mismatches =" , count)
        else:
            global counts
            counts += count
            print("alignments with more than 0 mismatches =" , counts)

aligned_mismatches(bamfile)


