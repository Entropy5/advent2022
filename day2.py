import numpy as np
import re

data = open('input2.txt', 'r').read().split('\n')
towin = {1: 2, 2: 3, 3: 1}
toloose = {1: 3, 2: 1, 3: 2}
score = 0

for d in data:
    if len(d) > 0:
        a, b = d.split(" ")
        a, b = ord(a) - 64, ord(b) - 87
        score += b
        score += 3 if a == b else 6 if (a, b) in towin.items() else 0
print(score)

score = 0
for d in data:
    if len(d) > 0:
        a, b = d.split(" ")
        a = ord(a) - 64
        if b == 'X':  # loose
            score += toloose[a]
        if b == 'Y':  # draw
            score += 3 + a
        if b == 'Z':  # win
            score += 6 + towin[a]
print(score)

