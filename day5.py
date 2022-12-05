import numpy as np
import re

# data = open('test5.txt', 'r').read().split('\n')
data = open('input5.txt', 'r').read().split('\n')

switch = 0
for i, d in enumerate(data):
    if d == '':
        switch = i
        break

n = int((len(data[0]) + 1) / 4)
stacks = [[] for i in range(n)]

for d in data[:switch - 1]:
    for i in range(n):
        cont = d[4 * i + 1:4 * i + 2]
        if cont != ' ':
            stacks[i].append(cont)

print(stacks)

for d in data[switch + 1:]:
    if d != '':
        spl = d.split(' ')
        amount = int(spl[1])
        from_c = int(spl[3])
        to_c = int(spl[5])
        """
        for _ in range(amount):
            subject = stacks[from_c - 1][0]
            stacks[from_c - 1] = stacks[from_c - 1][1:]
            stacks[to_c - 1] = [subject] + stacks[to_c - 1]
            """
        subject = stacks[from_c - 1][0:amount]
        stacks[from_c - 1] = stacks[from_c - 1][amount:]
        stacks[to_c - 1] = subject + stacks[to_c - 1]

print(stacks)
print(''.join(stacks[i][0] for i in range(n)))
