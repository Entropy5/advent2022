import numpy as np
import re

data = open('input1.txt', 'r').read().split('\n')
out = []

total = 0
for i, x in enumerate(data):
    if x == '':
        out.append(total)
        total = 0
    else:
        total += int(x)

print(max(out))
print(sum(sorted(out)[-3:]))
