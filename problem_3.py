#! /usr/bin/env python3

from collections import Counter

count = 0

hexamer_5 = Counter()
hexamer_3 = Counter()

import sys

filename = sys.argv[1]

for line in open(filename):
    line = line.rstrip()

    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

def fiveprime_hexamer(filename):

    hexamer_5 = seq[0:6]
    hexamers_5[hexamer_5] += 1

    for hexamer, count in hexamers_5.most_common(1):
        print("The most common 5'end hexamer sequence is", hexamer)

def threeprime_hexamer(filename):

    hexamer_3 = seq[-6:]
    hexamers_3[hexamer_3] += 1

    for hexamer, count in hexamers_3.most_common(1):
         print("The most common 3'end hexamer sequence is", hexamer)

fiveprime_hexamer(filename)
threeprime_hexamer(filename)



