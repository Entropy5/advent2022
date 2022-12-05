import numpy as np
import re

data = open('input.txt', 'r').read().split('\n')
# data = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL']

total = 0
for s in data:
    num = int(len(s) / 2)
    a, b = s[:num], s[num:]
    seta = set([x for x in a])
    setb = set([x for x in b])
    inter = seta.intersection(setb)
    o = ord(inter.pop())
    total += o - 96 if o >= 97 else o - 38
print(total)

total = 0
gr = int(len(data) / 3)
for i in range(gr):
    seta = set([x for x in data[3 * i + 0]])
    setb = set([x for x in data[3 * i + 1]])
    setc = set([x for x in data[3 * i + 2]])
    inter = seta.intersection(setb).intersection(setc)
    o = ord(inter.pop())
    total += o - 96 if o >= 97 else o - 38

print(total)
