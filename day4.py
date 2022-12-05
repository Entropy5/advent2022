import numpy as np
import re

data = open('input4.txt', 'r').read().split('\n')
hits = 0


def contained(start1, end1, start2, end2):
    # is 1 contained in 2
    return start1 >= start2 and end1 <= end2


def overlap(start1, end1, start2, end2):
    # is 1 contained in 2
    range1 = set(range(start1, end1 + 1))
    range2 = set(range(start2, end2 + 1))
    # is there overlap?
    return len(range1.intersection(range2)) > 0


for x in data:
    if len(x) < 1:
        continue
    print(x)
    a, b = x.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
    # if contained(a1, a2, b1, b2) or contained(b1, b2, a1, a2):
    if overlap(a1, a2, b1, b2):
        hits += 1
        print('hit')

print(hits)
