import numpy as np
import re

data = open('input.txt', 'r').read().split('\n')[0]
i = 0
size = 14

while True:
    s = set()
    for j in range(size):
        s.add(data[i + j])
    if len(s) == size:
        print(i + size)
        break
    i += 1





